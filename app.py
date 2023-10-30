from __future__ import print_function
from twilio.rest import Client
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    Response,
)  # imports functions to use python with html
import os
from datetime import date, datetime
import json
from google.cloud import bigquery
import resend
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from email.message import EmailMessage
import uuid
import http.client

treapp_url = os.getenv("TREEAPP_API_URL")
treeapp_key = os.getenv("TREEAPP_API_KEY")
resend.api_key = os.getenv("EMAIL_API_KEY")
resend_domain_id=os.getenv('EMAIL_DOMAIN_ID')
twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_from = os.getenv('TWILIO_FROM')
twilio_to = os.getenv('TWILIO_TO')



app = Flask("maggie-and-ollie-wedding")  # making an app
client = bigquery.Client()


def number_of_trees_lookup():
    tree_query_SQL = "SELECT * FROM `maggie-and-ollie-wedding.wedding_1805.other_numbers` WHERE key = 'tree_count'"
    tree_query_job = client.query(tree_query_SQL)
    tree_lookup_results = list(tree_query_job)[0]
    number_of_trees_value = tree_lookup_results[1]
    return number_of_trees_value


def treeapp_plant():
    # Generate Idempotency Key
    idempotency_key = str(uuid.uuid4())
    print("Generated Idempotency Key:", idempotency_key)

    # API Request
    conn = http.client.HTTPSConnection(treapp_url)
    payload = json.dumps({"quantity": 1})
    headers = {
        "Idempotency-Key": idempotency_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Treeapp-Api-Key": treeapp_key,
    }
    conn.request("POST", "/v1/usage-records", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print("API Response:", data.decode("utf-8"), " status code: ", res.status)

    # Update Database
    increase_tree_number_query = "UPDATE `maggie-and-ollie-wedding.wedding_1805.other_numbers` SET value = value + 1 WHERE key = 'tree_count'"
    client.query(increase_tree_number_query)
    print("Database updated")

    return "Tree planted and database updated"


def email_confirmation(email_addresses, invite_group, email_content_list):
    email_content = " ".join(str(rsvp) for rsvp in email_content_list)

    print(email_content)
    getdomain = resend.Domains.get(domain_id=resend_domain_id)
    domain_status=getdomain['status']
    print(domain_status)

    html_body_1 = """<!DOCTYPE html>
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
                            width: 100vw;
                            text-align: left;
                            background-attachment: fixed;
                            background-position: center;
                            background-repeat: no-repeat;
                            max-width: 800px;
                            background-color: white;
                            overflow-x: hidden;
                            overflow-y: scroll;
                            min-width: 400px;
                            height: auto;
                            margin: 0px;
                            font-family: "Playfair Display SC", serif;
                          }

                          div-display {
                            width: 100vw;
                          }

                          html,
                          body {
                            scroll-behavior: smooth;
                          }

                          .other-divs {
                            padding: 20px;
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

                          .logo-div {
                            align-content: center;
                            justify-content: center;
                            width: 100vw;
                          }

                          img {
                            justify-self: center;
                            position: relative;
                            margin: 0 auto;
                          }
                        </style>

                        <title>Maggie and Ollie's Wedding!</title>
                      </head>

                      <body>
                        <div class="email-layout">
                          <div class="div-display">
                            <img
                              src="https://lh3.googleusercontent.com/drive-viewer/AK7aPaDUF4L4_-llNOmMB2jVlNdQJHK3wPwDAxtxS0lhqOWAYyyoUTrwQ2nG_V2olHzPXcJu20AECbVTgBMp4U0mFrg0LYHtaQ=s1600"
                              title="Logo" style="display:block" height="auto" width="100%">
                          </div>

                          <div class="email-content">

                            <div class="other-divs">
                              <div class="other-divs">
                                <p>You have confirmed that:</p>"""
    html_body_2 = """
                                <br>
                                <p>If anything changes with regard to your ability to attend please let us know as soon as you can.</p>

                                <p>In the meantime, if you need to join the choir WhatsApp, remind yourself of the dress code, or view other information,<br>further
                                  details can be found on our
                                  <a href="https://www.maggieandolliewedding.party" target="_blank">website</a>.
                                </p>
                              </div>
                            </div>
                          </div>
                          <div class="logo-div">

                            <a href="https://www.maggieandolliewedding.party" target="_blank">
                              <img
                                src="https://lh3.googleusercontent.com/drive-viewer/AK7aPaDLJFRyGMyBz3JGkdmUChdIFmxZ59b2TGggVBMUvVHJ6RN7tcYDhCPVfiM_JH3VN3AdQPLHiElBRNPK6vO6XAln1e0C2w=s1600"
                                title="Logo" style="display:block" height="auto" width="100px">

                            </a>

                          </div>
                      </body>"""

    email = html_body_1 + email_content + html_body_2

    if domain_status=="verified":
        
      r = resend.Emails.send(
              {
                  "from": "rsvp@maggieandolliewedding.party",
                  "to": email_addresses,
                  "cc": "maggie.and.ollie.wedding@gmail.com",
                  "subject": f"RSVP - {invite_group}",
                  "reply_to": "maggie.and.ollie.wedding@gmail.com",
                  "html": email
              }
          )



    

      return "email conf sent"
    else:
      print(email)

      message_content="Domain verification for resend api failed, reverification in process. RSVP confirmation failure for: "+email_addresses+" RSVP IS: "+email_content

      twilio_client = Client(twilio_account_sid, twilio_auth_token)

      message = twilio_client.messages.create(
        from_=twilio_from,
        body=message_content,
        to=twilio_to
      )

      print(message.sid)
      verify = resend.Domains.verify(domain_id=resend_domain_id)
      return email, ": email conf NOT SENT - domain in process of re-verifying"


# Homepage
@app.route("/")
def landing_page():
    today = date.today()
    wedding = date(2024, 5, 18)
    time_left = wedding - today
    days_left = time_left.days

    number_of_years = str(today.year - 2014)

    number_of_trees = number_of_trees_lookup()

    return render_template(
        "index.html",
        days_left=days_left,
        number_of_years=number_of_years,
        number_of_trees=number_of_trees,
    )


# RSVPPage
@app.route("/RSVP")
def RSVP():
    lookupData = {"numberofInvitees": 0, "inviteGroup": "Full list here"}
    # keep this or jinja2 will break
    invite_lookup_query_SQL = (
        f"SELECT * FROM `maggie-and-ollie-wedding.wedding_1805.invitations_table`"
    )

    number_of_trees = number_of_trees_lookup()

    invite_lookup_query_job = client.query(invite_lookup_query_SQL)
    invite_lookup_results = list(invite_lookup_query_job)
    list_results = []
    invitationList = []

    for invite in invite_lookup_results:
        invite_id = invite.Invite_ID
        invite_names_list = invite.Invite_Group_Name
        invitees_count = invite.Headcount

        invite_obj = {
            "id": invite_id,
            "people_on_invite": invite_names_list,
            "headocunt": invitees_count,
        }

        list_results.append(invite_obj)
        invitationList.append(invite_names_list)

    return render_template(
        "RSVP.html",
        lookupData=lookupData,
        invite=invite_obj,
        number_of_trees=number_of_trees,
        list_results=list_results,
        invitationList=invitationList,
        lookup_id=invite_id,
    )


@app.route("/thankyou", methods=["POST"])
def RSVP_group():
    form_data = request.form
    responder_name = form_data["search-your-name"]
    current_datetime = datetime.now()
    response_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    invitation_ID = ""
    number_of_trees_original = number_of_trees_lookup()
    invitation_valid = None

    email_addresses = []
    email_content_list = []
    email_sent = False

    for i in range(1, 6):
        full_name = str(form_data.get(f"invitee-form{i}"))
        if full_name:
            if not invitation_ID:
                invite_id_query = f"""
                                SELECT Invite_ID
                                FROM `maggie-and-ollie-wedding.wedding_1805.RSVP_table`
                                WHERE Full_Name = '{full_name}'
                                """
                invite_id_query_job = client.query(invite_id_query)
                invitation_ID = list(invite_id_query_job.result())[0][0]

                invitation_list_query = f'SELECT * FROM `maggie-and-ollie-wedding.wedding_1805.invitations_table` WHERE Invite_ID = "{invitation_ID}"'
                invitation_list_query_job = client.query(invitation_list_query)
                invite_group = list(invitation_list_query_job.result())[0][1]

            if invitation_valid is None:
                invitation_valid_query = f'SELECT * FROM `maggie-and-ollie-wedding.wedding_1805.invitations_table` WHERE Invite_ID = "{invitation_ID}"'

                invitation_valid_query_job = client.query(invitation_valid_query)
                invitation_valid_rows = list(invitation_valid_query_job.result())

                if invitation_valid_rows:
                    invitation_valid = invitation_valid_rows[0][3]

            if invitation_valid:
                RSVP_bool = (
                    "TRUE" if form_data.get(f"RSVPCheck{i}") == "on" else "FALSE"
                )
                choir_bool = (
                    "TRUE" if form_data.get(f"RSVPChoir{i}") == "on" else "FALSE"
                )
                choir_part = str(form_data.get(f"dropdownVocalPart{i}"))
                dietary_bool = (
                    "TRUE" if form_data.get(f"RSVPDiet{i}") == "on" else "FALSE"
                )
                dietary_opt = str(form_data.get(f"dropdownDiet{i}"))
                dietary_detail = str(form_data.get(f"dietDetail{i}"))
                response_time = str(response_datetime)
                responder = str(responder_name)
                summary_string_basic = f"{full_name} RSVP'd {RSVP_bool}. Choir: {choir_bool}, {choir_part}. \
                                                  Dietary: {dietary_bool}, {dietary_opt}{dietary_detail}. Response at {response_time} from {responder}."

                if RSVP_bool == "TRUE":
                    summary_string = f"<b>{full_name}</b> is able to attend the wedding."
                    if choir_bool == "TRUE":
                        summary_string = (
                            summary_string
                            + f" They will be joining the choir, singing {choir_part}."
                        )
                    else:
                        summary_string = (
                            summary_string + " They would not like to join the choir."
                        )
                    if dietary_bool == "TRUE":
                        if dietary_opt == "Multiple/Other":
                            diet_text = dietary_detail
                        else:
                            diet_text = dietary_opt
                        summary_string = (
                            summary_string
                            + f" They have the following dietary requirements: {diet_text}."
                        )
                    else:
                        summary_string = (
                            summary_string + " They have no dietary requirements."
                        )

                else:
                    summary_string = f"<b>{full_name}</b> is not able to attend the wedding."

                email_content_list.append(f"<p>{summary_string}</p>")

                update_invite_query = f"""
                                        UPDATE `maggie-and-ollie-wedding.wedding_1805.RSVP_table`
                                        SET Choir_BOOL = {choir_bool}, Choir_Part = '{choir_part}',
                                        Dietary_BOOL = {dietary_bool}, Dietary_Detail_Long = '{dietary_detail}',
                                        RSVP_BOOL = {RSVP_bool}, Dietary_Detail = '{dietary_opt}',
                                        RSVP_Datetime = '{response_datetime}', RSVP_Responder = '{responder_name}'
                                        WHERE Full_Name = '{full_name}'
                                        """
                client.query(update_invite_query)

                email_query = f"""
                                SELECT Email
                                FROM `maggie-and-ollie-wedding.wedding_1805.RSVP_table`
                                WHERE Full_Name = '{full_name}'
                                """
                email_query_job = client.query(email_query)
                email = list(email_query_job.result())[0][0]

                email_addresses.append(email)

    while email_sent == False:
      if invitation_valid:
          email_confirmation(email_addresses, invite_group, email_content_list)
          t = treeapp_plant()
          print(t)

          update_invitation_row_query = f"UPDATE `maggie-and-ollie-wedding.wedding_1805.invitations_table` SET Active = false, Email_Sent = TRUE WHERE Invite_ID = '{invitation_ID}';"
          client.query(update_invitation_row_query)

          number_of_trees_now = number_of_trees_original + 1
          email_sent == True

          return render_template("thankyou.html", number_of_trees=number_of_trees_now)

      else:
          print("response already received")
          number_of_trees = number_of_trees_lookup()
          return render_template("error.html", number_of_trees=number_of_trees)


# Info
@app.route("/info180524")
def info():
    number_of_trees = number_of_trees()

    return render_template("info.html")


###debugging
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
###app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.
