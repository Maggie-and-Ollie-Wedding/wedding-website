from __future__ import print_function
from flask import Flask, render_template, request, jsonify, Response #imports functions to use python with html
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

treapp_url=os.getenv('TREEAPP_API_URL')
treeapp_key=os.getenv('TREEAPP_API_KEY')
resend.api_key = os.getenv('EMAIL_API_KEY')



app = Flask("maggie-and-ollie-wedding") #making an app
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
    payload = json.dumps({
        "quantity": 1
    })
    headers = {
        'Idempotency-Key': idempotency_key,
        'Content-Type': "application/json",
        'Accept': "application/json",
        'X-Treeapp-Api-Key': treeapp_key
    }
    conn.request("POST", "/v1/usage-records", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print("API Response:", data.decode('utf-8'), " status code: ", res.status)

    # Update Database
    increase_tree_number_query = "UPDATE `maggie-and-ollie-wedding.wedding_1805.other_numbers` SET value = value + 1 WHERE key = 'tree_count'"
    client.query(increase_tree_number_query)
    print("Database updated")

    return "Tree planted and database updated"




def email_confirmation(email_addresses, invite_group, email_content_list):
       
        email_content = ' '.join(str(rsvp) for rsvp in email_content_list)


        html_body_1="""<!DOCTYPE html>
<html>

<head>


  <link
    href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&family=Playfair+Display&family=Playfair+Display+SC&display=swap"
    rel="stylesheet">

    <style>
      :root {
        --cover-page-height: 40vh;
        --main-dark-colour: #091d36;
        --mid-dark-colour: #053c5c;
        --dark-colour-transparent: rgba(0, 0, 0, 0.5);
        --dark-colour-semitransparent: rgba(2, 9, 18, 0.4);
        --warm-colour-semitransparent: rgba(226, 196, 132, 0.5);
        --soft-dark-colour: #e1c892;
        --soft-background-colour: #ffffff;
        --light-colour: #fafaf7;
        --warm-colour: #f1e2c7;
        --gentle-mid-colour: #f6f0e5;
        --mid-colour: #053c5c;
        --border-width: 5px;
        --colour-4:  #e2c484;
      }
  
  
      body {
        background-size: cover;
        text-align: center;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        width: 90vw;
        background-color: var(--soft-background-colour);
        overflow-x: hidden;
        overflow-y: scroll;
        height: auto;
        margin: 0px;
  
      }
  
  
  
      .page-section {
        width: 75vw;
        transition: transform 0.5s ease-in-out;
      }
  
      #cover-page-gradient {
        z-index: -2;
        background: var(--soft-background-colour);
        background: linear-gradient(0deg,
            rgba(252, 250, 250, 0) 0%,
            rgb(2, 9, 18) 100%);
        height: var(--cover-page-height);
        width: 100vw;
        position: absolute;
        opacity: 1;
        z-index: 0;
  
      }
  
      .cover-page-image {
        z-index: -4;
        height: var(--cover-page-height);
        width: 100vw;
        object-fit: cover;
        opacity: 0.9;
      }
  
  
      #cover-page {
        position: absolute;
        z-index: 2;
        color: var(--soft-background-colour);
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100vw;
        height: var(--cover-page-height);
        justify-content: center;
      }
  
      #cover-page .centered-text {
        text-align: center;
      }
  
  
      html,
      body {
        scroll-behavior: smooth;
      }
  
  
  
      h1,
      h2,
      h5 {
        font-family: "Playfair Display SC", serif;
      }
  
      h3 {
        padding: 24px;
        font-family: "Playfair Display SC", serif;
      }
  
      h4 {
        padding: 14px;
        font-family: "Playfair Display SC", serif;
      }
  
      h5 {
        padding: 10px;
        font-family: "Playfair Display SC", serif;
      }
  
      h6 {
        padding: 0px;
        font-family: "Playfair Display SC", serif;
        font-size: small;
      }
  
      p {
        font-family: "Open Sans", sans-serif;
      }
  
      .carousel-display-home {
        height: var(--cover-page-height);
        width: 100vw;
        border-radius: 300px 300px 0px 0px;
        position: relative;
        z-index: -2;
      }
  
  
  
  
      .ceremony-and-reception-parent {
        display: flex;
        flex-direction: row;
        text-align: start;
  
      }
  
      .ceremony-and-reception-child {
        display: flex;
        justify-content: center;
        flex: 1
      }
  
      .ceremony-and-reception-grandchild {
        display: inline;
        justify-content: left;
        padding: 12px;
        flex: 1
      }
  
      .rsvp-button {
        border: var(--main-dark-colour);
        color: var(--main-dark-colour);
        border: 5px solid var(--main-dark-colour);
        /* Add border */
        display: flex;
        text-align: center;
        width: 50%;
      }
  
      .rsvp-button-link {
        color: var(--main-dark-colour);
        text-decoration: none;
        display: flex;
        margin-bottom: 0.5rem;
      }
  
      .rsvp-button:hover {
        background-color: var(--dark-colour-transparent)
      }
  
      .rsvp-button-link:link {
        color: var(--main-dark-colour);
        margin-top: 0.5rem;
      }
  
      .rsvp-button-link:hover:before {
        content: "";
      }
  
      .cover-page-container {
        position: relative;
        display: flex;
        height: var(--cover-page-height);
        width: 100vw;
      }
  
      .other-divs {
  
        display: flex;
        position: relative;
        justify-content: space-around;
      }
  
      .email-layout {
        display: flex;
        flex-direction: column;
        height: auto;
        width: 100vw;
  
      }
  
  
      .button-list-parent {
        display: flex;
        flex-direction: column;
        position: relative;
        width: 100%;
        color: var(--main-dark-colour);
      }
  
      .button-list-child {
        display: flex;
        align-self: center;
        margin: 10px;
        justify-content: center;
      }
  
      .bus-box-div {
        display: flex;
        justify-content: center;
      }
  
      .bus-box {
        border: var(--soft-dark-colour);
        width: 60%;
        height: auto;
        margin-bottom: 1rem;
        border-style: solid;
        border-width: var(--border-width);
        display: flex;
        margin-top: 0.5rem;
        padding: 20px;
  
      }
  
      @media only screen and (max-width: 800px) {
        :root {
          --cover-page-height: 40vh;
        }
  
        .ceremony-and-reception-parent {
          flex-direction: column;
  
        }
  
        h1 {
          font-size: xx-large;
        }
  
        h2 {
          font-size: x-large;
        }
  
        h3 {
          font-size: medium;
        }
  
        h4 {
          font-size: medium;
        }
  
        h5 {
          font-size: medium;
        }
  
        h6 {
          font-size: small;
          padding: 0px;
        }
  
        p {
          font-size: large;
        }
  
        .bus-box {
          width: 80%;
  
        }}

        .email-content {
      padding: 10px;
    }

    .dot:after{
  content: ".";
  display: inline-block;
  position: relative;
    bottom: 0.75em;
  left: 0;
  text-align: center;
  width: 100%;
  color: var(--colour-4);
}
      
    </style>

  <title>Maggie and Ollie's Wedding!</title>
</head>

<body>
  <div class="email-layout">
    <div class="cover-page-container">
      <div class="page-section" id="cover-page">
        <div>
          <div id="cover-page-gradient"></div>
          <div class="carousel-display-home">
            <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img class="d-block w-100 cover-page-image"
                    src="../static/images/EngagementPhotos/Maggie_OllieEngagement89_sq.jpg"
                    alt="Maggie and Ollie on bridge">
                </div>
              </div>

            </div>
          </div>
        </div>

        <div id="cover-page">
          <br>
          <h2>the wedding of</h2>
          <h1>Maggie Rose Prinn Hunt<br>&<br>Oliver John Benjamin Norman</h1>
          <h3>18th May 2024 | Bedfordshire, UK</h3>


        </div>
      </div>
    </div>
    <div class="email-content">
    <div>
      <h4>Dear """
       

        html_body_2="""
    </div>
    <div class="other-divs">
      <h2><span class="dot">Thank you for your response to our invitation.</span></h2></div>
      <div class="other-divs"><p>You have confirmed that:</p>
    </div>
    <div class="other-divs">
"""

  


        html_body_3="""
    </div>

    <div class="other-divs">
      <p>If anything changes with regard to your ability to attend please let us know as soon as you can.</p>
    </div>
    <div>

      <div class="other-divs">
        <p>In the meantime, if you need to remind yourself of the dress code, or other information, <br>further details can be found on our website.</p>
      </div>
      <div class="button-list-parent">
        <div class="rsvp-button button button-list-child" id="website">
          <a class="rsvp-button-link" href="https://www.maggieandolliewedding.party" target="_blank">
            <h2>website</h2>
          </a>
        </div>

       



      </div>
    </div>

<br>
  <div>
    <img src="../static/images/mologo.png" height="auto" width="100px">
  </div></div></div>
</body>
"""
        html_body=str(html_body_1+invite_group+html_body_2+email_content+html_body_3)


        r = resend.Emails.send({
        "from": "rsvp-noreply@maggieandolliewedding.party",
        "to":  email_addresses,
        "cc": "maggie.and.ollie.wedding@gmail.com",
        "subject": f"RSVP - {invite_group}",
        "reply_to": "maggie.and.ollie.wedding@gmail.com",
        "html": html_body
                })


        return "email conf sent"


#Homepage
@app.route("/")  
def landing_page():

    today = date.today()
    wedding = date(2024, 5, 18)
    time_left = wedding - today
    days_left = time_left.days
    
    number_of_years = str(today.year-2014)

    number_of_trees = number_of_trees_lookup()

    
    return render_template("index.html", days_left=days_left,  number_of_years=number_of_years, number_of_trees=number_of_trees)

#RSVPPage
@app.route("/RSVP")  
def RSVP():
        lookupData = {
        "numberofInvitees" : 0,
        "inviteGroup" : "Full list here"}
        #keep this or jinja2 will break
        invite_lookup_query_SQL = f'SELECT * FROM `maggie-and-ollie-wedding.wedding_1805.invitations_table`'

        number_of_trees=number_of_trees_lookup()
        
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
                "headocunt": invitees_count
                }
                
                list_results.append(invite_obj)
                invitationList.append(invite_names_list)

        
        return render_template("RSVP.html", lookupData=lookupData, invite=invite_obj, number_of_trees=number_of_trees, list_results=list_results, invitationList=invitationList, lookup_id=invite_id)


@app.route("/thankyou", methods=["POST"])
def RSVP_group():
        form_data = request.form
        responder_name = form_data['search-your-name']
        current_datetime = datetime.now()
        response_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
        invitation_ID = ""
        number_of_trees_original = number_of_trees_lookup()
        invitation_valid = None

        email_addresses = []
        email_content_list = []

        for i in range(1, 6):
                full_name =  str(form_data.get(f'invitee-form{i}'))
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
                                
                                RSVP_bool = "TRUE" if form_data.get(f'RSVPCheck{i}') == "on" else "FALSE"
                                choir_bool = "TRUE" if form_data.get(f'RSVPChoir{i}') == "on" else "FALSE"
                                choir_part = str(form_data.get(f'dropdownVocalPart{i}'))
                                dietary_bool = "TRUE" if form_data.get(f'RSVPDiet{i}') == "on" else "FALSE"
                                dietary_opt = str(form_data.get(f'dropdownDiet{i}'))
                                dietary_detail = str(form_data.get(f'dietDetail{i}'))
                                response_time = str(response_datetime)
                                responder = str(responder_name)
                                summary_string_basic = ( f"{full_name} RSVP'd {RSVP_bool}. Choir: {choir_bool}, {choir_part}. \
                                                  Dietary: {dietary_bool}, {dietary_opt}{dietary_detail}. Response at {response_time} from {responder}.")
                               
                                if RSVP_bool == "TRUE":  
                                       summary_string = f"{full_name} is able to attend the wedding."
                                       if choir_bool == "TRUE":
                                              summary_string = summary_string + f" They will be joining the choir, singing {choir_part}."
                                       else:
                                              summary_string = summary_string + " They would not like to join the choir."
                                       if dietary_bool == "TRUE":
                                               if dietary_opt == "Multiple/Other":
                                                      diet_text = dietary_detail
                                               else:
                                                      diet_text = dietary_opt
                                               summary_string = summary_string + f" They have the following dietary requirements: {diet_text}."
                                       else:
                                              summary_string = summary_string + " They have no dietary requirements."
                                        
                                else:
                                       summary_string = f"{full_name} is not able to attend the wedding."
                               

                                
                                email_content_list.append(f"<br>{summary_string}<br>")

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


  
        if invitation_valid:
                
                
                email_confirmation(email_addresses, invite_group, email_content_list)
                t = treeapp_plant()
                print(t)
        
 
                update_invitation_row_query = f"UPDATE `maggie-and-ollie-wedding.wedding_1805.invitations_table` SET Active = false, Email_Sent = TRUE WHERE Invite_ID = '{invitation_ID}';" 
                client.query(update_invitation_row_query)

                number_of_trees_now = number_of_trees_original+1
                
                return render_template("thankyou.html", number_of_trees=number_of_trees_now)
                        
        else:   
               print("response already received")
               number_of_trees=number_of_trees_lookup()
               return render_template("error.html", number_of_trees=number_of_trees)     
                
                       
        

#Info
@app.route("/info180524")  
def info():
        number_of_trees = number_of_trees()
        
        return render_template("info.html")


###debugging
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
###app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.
