from __future__ import print_function
from flask import Flask, render_template, request, jsonify, Response #imports functions to use python with html
import os
from datetime import date, datetime
import json
from google.cloud import bigquery

from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from email.message import EmailMessage
import base64

import http.client

treapp_url=os.getenv('TREEAPP_API_URL')
treeapp_key=os.getenv('TREEAPP_API_KEY')




app = Flask("maggie-and-ollie-wedding") #making an app
client = bigquery.Client()


def number_of_trees_lookup():
    tree_query_SQL = "SELECT * FROM `maggie-and-ollie-wedding.wedding_1805.other_numbers` WHERE key = 'tree_count'"
    tree_query_job = client.query(tree_query_SQL)
    tree_lookup_results = list(tree_query_job)[0]
    number_of_trees_value = tree_lookup_results[1]
    return number_of_trees_value

def treeapp():
        conn = http.client.HTTPSConnection(treapp_url)

        payload = "{\n  \"quantity\": 1\n}"

        headers = {
        'Idempotency-Key': "",
        'Content-Type': "application/json",
        'Accept': "application/json",
        'X-Treeapp-Api-Key': treeapp_key

        }

        conn.request("POST", "/v1/usage-records", payload, headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))

        increase_tree_number_query = "UPDATE `maggie-and-ollie-wedding.wedding_1805.other_numbers` SET value = value + 1 WHERE key = 'tree_count'"
        client.query(increase_tree_number_query)

        print("ok")

        return "ok"


#Homepage
@app.route("/")  
def landing_page():

    today = date.today()
    wedding = date(2024, 5, 18)
    time_left = wedding - today
    days_left = time_left.days
    
    number_of_years = str(today.year-2014)
    print(number_of_years)
    number_of_trees = number_of_trees_lookup()
    print(number_of_trees)
    
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
                                print(invitation_ID)
                        
                        if invitation_valid is None:
                                invitation_valid_query = f'SELECT * FROM `maggie-and-ollie-wedding.wedding_1805.invitations_table` WHERE Invite_ID = "{invitation_ID}"'

                                print(invitation_valid_query)
                            
                                invitation_valid_query_job = client.query(invitation_valid_query)
                                invitation_valid_rows = list(invitation_valid_query_job.result())
                                print(invitation_valid_rows)
                                
                                if invitation_valid_rows:
                                        invitation_valid = invitation_valid_rows[0][3]
                                        print("invitation valid? ", invitation_valid)
                                else:
                                        print("No matching rows found for invitation ID:", invitation_ID)

                        
                        if invitation_valid:
                                
                                RSVP_bool = "TRUE" if form_data.get(f'RSVPCheck{i}') == "on" else "FALSE"
                                choir_bool = "TRUE" if form_data.get(f'RSVPChoir{i}') == "on" else "FALSE"
                                choir_part = str(form_data.get(f'dropdownVocalPart{i}'))
                                dietary_bool = "TRUE" if form_data.get(f'RSVPDiet{i}') == "on" else "FALSE"
                                dietary_opt = str(form_data.get(f'dropdownDiet{i}'))
                                dietary_detail = str(form_data.get(f'dietDetail{i}'))
                                response_time = str(response_datetime)
                                responder = str(responder_name)
                                summary_string = ( f"{full_name} RSVP'd {RSVP_bool}. Choir: {choir_bool}, {choir_part}. Dietary: {dietary_bool}, {dietary_opt}{dietary_detail}. Response at {response_time} from {responder}.")

                                print(summary_string)

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
                                print(email)



        print(invitation_valid, "valid")
        if invitation_valid:

                treeapp()
 
                update_invitation_row_query = f"UPDATE `maggie-and-ollie-wedding.wedding_1805.invitations_table` SET Active = false, Email_Sent = TRUE WHERE Invite_ID = '{invitation_ID}';" 
                update_invitation_row = client.query(update_invitation_row_query)

                number_of_trees_now = number_of_trees_original+1
                
                return render_template("thankyou.html", number_of_trees=number_of_trees_now)
                        
        else:   
               print("response already received")
               number_of_trees=number_of_trees_lookup()
               return render_template("error.html", number_of_trees=number_of_trees)     
                
                       

# @app.route('/rsvp_list', methods=['POST'])
# def rsvp_list():
#     selected_option = request.json['selectedOption']

#     result = RSVP_list(selected_option)

#     return jsonify({'result': result})

# def RSVP_list(invite_guestlist):
        
    
#         invite_lookup_query_start = ' SELECT * FROM `maggie-and-ollie-wedding.wedding_1805.invitations_table` WHERE Invite_Group_Name = "'
#         invite_lookup_search_value = invite_guestlist
#         invite_lookup_query_end = '"'
#         invite_lookup_query_SQL = invite_lookup_query_start+invite_lookup_search_value+invite_lookup_query_end
                
# # Execute the query
#         invite_lookup_query_job = client.query(invite_lookup_query_SQL)

# # Fetch the results
#         invite_lookup_results = list(invite_lookup_query_job)[0]
#         print(invite_lookup_results)     
#         invite_id = invite_lookup_results[0]
#         invite_group_name = invite_lookup_results[1]
#         invitees_count = invite_lookup_results[2]
#         invite_active = invite_lookup_results[3]
#         print(invite_active, "invite active")

#         lookupData = {
#         "numberofInvitees" : invitees_count,
#         "inviteGroup" : invite_group_name}

#         if invite_active:
               
#                 print("new response")
#                 lookupData = {
#                         "inviteID": invite_id,
#                         "numberofInvitees": invitees_count,
#                         "inviteGroup": invite_guestlist
#                 }       
#                 print("invite id:", invite_id)
#                 print("invitee count", invitees_count)
#                 print(lookupData)
#                 invitees_query_SQL= 'SELECT * FROM `maggie-and-ollie-wedding.wedding_1805.RSVP_table`WHERE Invite_ID = "'+invite_id+'"'
#                 invitees_lookup_query_job = client.query(invitees_query_SQL)
#                 invitees_lookup_results = list(invitees_lookup_query_job)
#                 print(invitees_lookup_results)
#                 count=1
#                 invitees = []

#                 for invitee in invitees_lookup_results:
#                         fullname= invitee["Full_Name"]
#                         varname = f"invitee{count}"
#                         count+=1
#                         invitees.append({varname: fullname})

#                 print(invitees)

#                 for i, invitee in enumerate(invite_guestlist[:6]):
#                         lookupData[f"invitee{i + 1}"] = invitee

#                 # If the invitees list has less than 6 items, the remaining keys will have empty strings as values
#                 for i in range(len(invite_guestlist), 6):
#                         lookupData[f"invitee{i + 1}"] = ""

    
#                 return render_template("RSVP.html", invitees_count=invitees_count, number_of_trees=number_of_trees, lookupData=lookupData, invitees=invitees)
        
        

#OrderofEvents
@app.route("/order-of-events")  
def order_of_events():
        number_of_trees = number_of_trees()
        print(number_of_trees)
        return render_template("orderofevents.html")

#SeatingPlan
@app.route("/seating-plan")  
def seating_plan():
        number_of_trees = number_of_trees()
        print(number_of_trees)
        return render_template("seatingplan.html")


###debugging
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
###app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.
