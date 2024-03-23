import resend
import os
from twilio.rest import Client

resend.api_key = os.getenv("EMAIL_API_KEY")
resend_domain_id = os.getenv("EMAIL_DOMAIN_ID")
twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_from = os.getenv("TWILIO_FROM")
twilio_to = os.getenv("TWILIO_TO")

invite_count = 0

getdomain = resend.Domains.get(domain_id=resend_domain_id)
domain_status = getdomain["status"]
print(domain_status)

twilio_client = Client(twilio_account_sid, twilio_auth_token)


if domain_status != "verified":
    verify = resend.Domains.verify(domain_id=resend_domain_id)
    print("verification in progress. try again later")

    message = twilio_client.messages.create(
        from_=twilio_from, body="verification in progress", to=twilio_to
    )

else:
    from google.cloud import bigquery

    list_of_sent = []

    # Initialize a BigQuery client
    client = bigquery.Client()

    # Define the BigQuery table names and project ID
    project_id = "maggie-and-ollie-wedding"
    invitations_table_name = "wedding_1805.invitations_table"
    rsvp_table_name = "wedding_1805.RSVP_table"

    # Query the invitations table for rows where Email_sent is false
    query = f"""
      SELECT Invite_ID, Invite_Group_Name
      FROM `{project_id}.{invitations_table_name}`
      WHERE Reminder_sent = FALSE
  """

    # Execute the query and process the results
    query_job = client.query(query)

    for row in query_job:
          email_addresses = []
          invite_id = row["Invite_ID"]
          print(invite_id)
          invite_group = row["Invite_Group_Name"]
          print(invite_group)

         
          # Query the RSVP table for rows with matching Invite_ID
          rsvp_query = f"""
          SELECT Email
          FROM `{project_id}.{rsvp_table_name}`
          WHERE Invite_ID = '{invite_id}
          AND RSVP_BOOL = true'
    """

          #
          # Execute the RSVP query
          rsvp_query_job = client.query(rsvp_query)

          # Append unique email addresses to the list
          for rsvp_row in rsvp_query_job:
              email = rsvp_row["Email"]
              if email not in email_addresses:
                  email_addresses.append(email)

          # Set the value of Invite_Group_Name to a variable called invitation_group

          print(email_addresses)
          html_body_1 = """ """
          html_body_2 = """ """

          html_body = html_body_1 + invite_group + html_body_2

          params = {
              "from": "rsvp@maggieandolliewedding.party",
              "to": email_addresses,
              "html": html_body,
              "cc": "maggie.and.ollie.wedding@gmail.com",
              "reply_to": "maggie.and.ollie.wedding@gmail.com",
              "subject": f"Maggie & Ollie's Wedding - Reminder",
          }

          r = resend.Emails.send(params)

          update_sent_query = f"""
          UPDATE `{project_id}.{invitations_table_name }`
          SET Reminder_sent = TRUE 
          WHERE Invite_ID = '{invite_id}'
      """
#todo: add Reminder_sent column; group invitees. Test with us
          
          query_job_update_sent = client.query(update_sent_query)

          # Wait for the query to complete
          query_job_update_sent.result()
          list_of_sent.append(invite_id)

          invitation_text = invite_group + " invite sent"

          message = twilio_client.messages.create(
              from_=twilio_from, body=invitation_text, to=twilio_to
          )
          invite_count += 1
          print("invtations sent:", invite_count)

    print(list_of_sent)


