from flask import Flask, render_template, request, jsonify, Response #imports functions to use python with html
import os
from datetime import date, datetime
import json
from google.cloud import bigquery

app = Flask("maggie-and-ollie-wedding") #making an app
client = bigquery.Client()
number_of_trees = 24

rsvp_field_mapping = {
    'Full_Name': 0,
    'Invite_ID': 1,
    'Choir_BOOL': 2,
    'Choir_Part': 3,
    'Dietary_BOOL': 4,
    'Dietary_Detail_Long': 5,
    'RSVP_BOOL': 6,
    'Email': 7,
    'Guest_Category': 8,
    'Dietary_Detail': 9,
    'Primary_Key': 10,
    'RSVP_Datetime': 11,
    'Uploaded_Datetime': 12,
    'RSVP_Confirmation_Sent_BOOL': 13,
    'RSVP_Responder': 14
}




# invitees_listing(lookup_invite("Testing Person18"))
#Homepage
@app.route("/")  
def landing_page():

    today = date.today()
    wedding = date(2024, 5, 18)
    time_left = wedding - today
    days_left = time_left.days
    
    number_of_years = str(today.year-2014)
    print(number_of_years)
    
    return render_template("index.html", days_left=days_left,  number_of_years=number_of_years, number_of_trees=number_of_trees)

#RSVPPage
@app.route("/RSVP")  
def RSVP():
        lookupData = {
        "numberofInvitees" : 0,
        "inviteGroup" : "Full list here"}
        #keep this or jinja2 will break
        invite_lookup_query_SQL = f'SELECT * FROM `maggie-and-ollie-wedding.wedding_1805.invitations_table`'

        
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


@app.route("/thankyou", methods=['POST'])
def RSVP_group():
        print(number_of_trees)
        number_of_trees +=1
        print(number_of_trees)
        return render_template("thankyou.html", number_of_trees=number_of_trees)

@app.route('/rsvp_list', methods=['POST'])
def rsvp_list():
    selected_option = request.json['selectedOption']

    result = RSVP_list(selected_option)

    return jsonify({'result': result})

def RSVP_list(invite_guestlist):
        
    
        invite_lookup_query_start = ' SELECT * FROM `maggie-and-ollie-wedding.wedding_1805.invitations_table` WHERE Invite_Group_Name = "'
        invite_lookup_search_value = invite_guestlist
        invite_lookup_query_end = '"'
        invite_lookup_query_SQL = invite_lookup_query_start+invite_lookup_search_value+invite_lookup_query_end
                
# Execute the query
        invite_lookup_query_job = client.query(invite_lookup_query_SQL)

# Fetch the results
        invite_lookup_results = list(invite_lookup_query_job)[0]
        print(invite_lookup_results)     
        invite_id = invite_lookup_results[0]
        invite_group_name = invite_lookup_results[1]
        invitees_count = invite_lookup_results[2]
        invite_active = invite_lookup_results[3]

        lookupData = {
        "numberofInvitees" : invitees_count,
        "inviteGroup" : invite_group_name}

        if invite_active:
               print("response already received")
               return render_template("error.html", number_of_trees=number_of_trees)
        else:
                print("new response")
                lookupData = {
                        "inviteID": invite_id,
                        "numberofInvitees": invitees_count,
                        "inviteGroup": invite_guestlist
                }       
                print("invite id:", invite_id)
                print("invitee count", invitees_count)
                print(lookupData)
                invitees_query_SQL= 'SELECT * FROM `maggie-and-ollie-wedding.wedding_1805.RSVP_table`WHERE Invite_ID = "'+invite_id+'"'
                invitees_lookup_query_job = client.query(invitees_query_SQL)
                invitees_lookup_results = list(invitees_lookup_query_job)
                print(invitees_lookup_results)
                count=1
                invitees = []

                for invitee in invitees_lookup_results:
                        fullname= invitee["Full_Name"]
                        varname = f"invitee{count}"
                        count+=1
                        invitees.append({varname: fullname})

                print(invitees)

                for i, invitee in enumerate(invite_guestlist[:6]):
                        lookupData[f"invitee{i + 1}"] = invitee

                # If the invitees list has less than 6 items, the remaining keys will have empty strings as values
                for i in range(len(invite_guestlist), 6):
                        lookupData[f"invitee{i + 1}"] = ""

    
                return render_template("RSVP.html", invitees_count=invitees_count, number_of_trees=number_of_trees, lookupData=lookupData, invitees=invitees)


@app.route("/thank-you")  
def RSVP_form(number_of_trees):

        # def lookup_invite():
        

        #         return invite_names_list,invite_id, invitees_count

        # def invitees_liting(invite_number):
        #         invitees_query_SQL= "SELECT * FROM `maggie-and-ollie-wedding.wedding_1805.RSVP_table`WHERE Invite_ID = "+invite_number
        #         invitees_lookup_query_job = client.query(invitees_query_SQL)
        #         invitees_lookup_results = invitees_lookup_query_job.result()
        #         count=1
        #         invitees = []
        #         for invitee in invitees_lookup_results:
        #                 fullname= invitee["Full_Name"]
        #                 varname = f"invitee{count}"
        #                 invitees.append({varname: fullname})
        #                 count+=1
        #         return invitees

        
        # #vars
        # # lookupData = {
        # # "numberofInvitees" : lookup_invite.invitees_count,
        # # "invitee1" : f"invitees_listing.invitees[0]",
        # # "invitee2" : f"invitees_listing.invitees[1]",
        # # "invitee3" : f"invitees_listing.invitees[2]",
        # # "invitee4" : f"invitees_listing.invitees[3]",
        # # "invitee5" : f"invitees_listing.invitees[4]",
        # # "invitee6" : f"invitees_listing.invitees[5]",
        # # "inviteGroup" : lookup_invite.invitees_names_list}

        # lookupData = {
        # "numberofInvitees": lookup_invite.invitees_count,
        #  "inviteGroup": lookup_invite.invitees_names_list
        # }

        # for i, invitee in enumerate(lookup_invite.invitees[:6]):
        #         lookupData[f"invitee{i + 1}"] = invitee

        # # If the invitees list has less than 6 items, the remaining keys will have empty strings as values
        # for i in range(len(lookup_invite.invitees), 6):
        #         lookupData[f"invitee{i + 1}"] = ""

        # print(lookupData)
        # return render_template("RSVP.html", lookupData=lookupData)
    
       
       #create json object per row in form
       #pair with row from query
       #mailgun responses too all
       #treeapp planting
       #update tree count
        number_of_trees+=1
        return render_template("thank-you.html", number_of_trees=number_of_trees)

#OrderofEvents
@app.route("/order-of-events")  
def order_of_events():
        return render_template("orderofevents.html")

#SeatingPlan
@app.route("/seating-plan")  
def seating_plan():
        return render_template("seatingplan.html")


###debugging
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
###app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.
