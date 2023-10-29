import resend
import os

resend.api_key = os.getenv('EMAIL_API_KEY')

getdomain = resend.Domains.get(domain_id="2a595f8b-4ac3-4610-8c69-98e15f5683e5")
print(getdomain)

verify = resend.Domains.verify(domain_id="2a595f8b-4ac3-4610-8c69-98e15f5683e5")
print(verify)
# verify = resend.Domains.verify(domain_id="cfb7a984-a859-4411-a30d-c0bc8e13fce8")
# print(verify)

from google.cloud import bigquery

list_of_sent = []

# Initialize a BigQuery client
client = bigquery.Client()

# Define the BigQuery table names and project ID
project_id = "maggie-and-ollie-wedding"
invitations_table_name = "wedding_1805.invitations_table"
rsvp_table_name = "wedding_1805.RSVP_table"

# Create a list to store email addresses
email_addresses = []

# Query the invitations table for rows where Email_sent is false
query = f"""
    SELECT Invite_ID, Invite_Group_Name
    FROM `{project_id}.{invitations_table_name}`
    
"""
# WHERE Email_sent = false

# Execute the query and process the results
query_job = client.query(query)
for row in query_job:
    invite_id = row["Invite_ID"]
    print(invite_id)
    invite_group = row["Invite_Group_Name"]
    print(invite_group)

    # Query the RSVP table for rows with matching Invite_ID
    rsvp_query = f"""
        SELECT Email
        FROM `{project_id}.{rsvp_table_name}`
        WHERE Invite_ID = '{invite_id}'
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
    html_body_1="""<!DOCTYPE html>
            <html lang="en">

            <head>

              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <meta name="x-apple-disable-message-reformatting" />

              <link
                href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&family=Playfair+Display&family=Playfair+Display+SC&display=swap"
                rel="stylesheet">

              <style>
              



                body {
                  
                  text-align: center;
                  background-attachment: fixed;
                  background-position: center;
                  background-repeat: no-repeat;
                  width: 100vw;
                  max-width:800px;
                  background-color: white;
                  overflow-x: hidden;
                  overflow-y: scroll;
                  min-width: 400px;
                  height: auto;
                  margin: 0px;
                  font-family: "Playfair Display SC", serif;

                }



                html,
                body {
                  scroll-behavior: smooth;
                }



                h3 {
                  padding: 24px;
                  margin: 24px;
                }

                h4 {
                  padding: 14px;

                }

                h5 {
                  padding: 10px;

                }

                h6 {
                  padding: 0px;
                  margin: 0px;
                  font-size: small;
                }

                p {
                  font-family: "Open Sans", sans-serif;
                }


            

              </style>


              <!-- title: CHANGE ME -->
              <title>Maggie and Ollie's Wedding!</title>
            </head>

            <body>
              <div class="email-layout">
                <div>
                



                
                </div>
                <div class="email-content">
                  <div><p>Dear</p>
                    <p>"""
    html_body_2=""",</p></div>

                        <div class="div-display">
                        <a href="https://www.maggieandolliewedding.party"> <img
                            src="https://lh3.googleusercontent.com/drive-viewer/AK7aPaDS14085OBWeL6zvD1cKPonkSi-v0z3gdC3sqStnIXA6XAzz3EAB5La87I8gXnAKBSvcUFdcZxyJbFkrpnByUV5PDXY=s1600"
                            title="Logo" style="display:block" height="auto" width="100%" ></a>
                        </div>


                      </div>
                    </div>
                      </body>"""

    html_body = html_body_1+invite_group+html_body_2
    
    params = {
            "from": "rsvp-noreply@maggieandolliewedding.party",
            "to": email_addresses,
            "html": html_body,
            "cc": "maggie.and.ollie.wedding@gmail.com",
            "reply_to": "maggie.and.ollie.wedding@gmail.com",
            "subject": f"Invitiation to Maggie & Ollie's Wedding - {invite_group}",
        }

    r = resend.Emails.send(params)

    update_sent_query = f"""
        UPDATE `{project_id}.{invitations_table_name }`
        SET Email_sent = TRUE
        WHERE Invite_ID = '{invite_id}'
    """

    query_job_update_sent = client.query(update_sent_query)

    # Wait for the query to complete
    query_job_update_sent.result()
    list_of_sent.append(invite_id)

print(list_of_sent)
