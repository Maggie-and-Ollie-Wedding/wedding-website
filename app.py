from flask import Flask, render_template, request, Response #imports functions to use python with html
import os
from datetime import date, datetime
import json
from google.cloud import bigquery


app = Flask("maggie-and-ollie-wedding") #making an app
GCP_Credentials = ""
client = bigquery.Client()



#Homepage
@app.route("/")  
def landing_page():

    today = date.today()
    wedding = date(2024, 5, 18)
    time_left = wedding - today
    days_left = time_left.days
    print(days_left)
    
    return render_template("index.html", days_left=days_left)

#RSVPPage
@app.route("/RSVP")  
def RSVP():

        return render_template("RSVP.html")


def RSVP_form():

        def lookup_invite():
                invite_lookup_query_start = ' SELECT * FROM `maggie-and-ollie-wedding.wedding_1805.invitations_table` WHERE Invite_Group_Name LIKE "%'
                invite_lookup_search_value = request.form["search_your_name"]
                invite_lookup_query_end = '%'
                invite_lookup_query_SQL = invite_lookup_query_start+invite_lookup_search_value+invite_lookup_query_end
                

        # Execute the query
                invite_lookup_query_job = client.query(invite_lookup_query_SQL)

        # Fetch the results
                invite_lookup_results = invite_lookup_query_job.result().limit(1)        
                invite_id = invite_lookup_results["Invite_ID"]
                invite_names_list = invite_lookup_results["Invite_Group_Name"]
                invitees_count = invite_lookup_results["Headcount"]

                return invite_names_list,invite_id, invitees_count

        def invitees_liting(invite_number):
                invitees_query_SQL= "SELECT * FROM `maggie-and-ollie-wedding.wedding_1805.RSVP_table`WHERE Invite_ID = "+invite_number
                invitees_lookup_query_job = client.query(invitees_query_SQL)
                invitees_lookup_results = invitees_lookup_query_job.result()
                count=1
                invitees = []
                for invitee in invitees_lookup_results:
                        fullname= invitee["Full_Name"]
                        varname = f"invitee{count}"
                        invitees.append({varname: fullname})
                        count+=1
                return invitees

        
        #vars
        # lookupData = {
        # "numberofInvitees" : lookup_invite.invitees_count,
        # "invitee1" : f"invitees_listing.invitees[0]",
        # "invitee2" : f"invitees_listing.invitees[1]",
        # "invitee3" : f"invitees_listing.invitees[2]",
        # "invitee4" : f"invitees_listing.invitees[3]",
        # "invitee5" : f"invitees_listing.invitees[4]",
        # "invitee6" : f"invitees_listing.invitees[5]",
        # "inviteGroup" : lookup_invite.invitees_names_list}

        lookupData = {
        "numberofInvitees": lookup_invite.invitees_count,
         "inviteGroup": lookup_invite.invitees_names_list
        }

        # Assuming invitees_listing.invitees is the list of invitees
        for i, invitee in enumerate(lookup_invite.invitees[:6]):
                lookupData[f"invitee{i + 1}"] = invitee

        # If the invitees list has less than 6 items, the remaining keys will have empty strings as values
        for i in range(len(lookup_invite.invitees), 6):
                lookupData[f"invitee{i + 1}"] = ""


        return render_template("RSVP.html", lookupData=lookupData)
    
    
        # return render_template("RSVP.html", numberofInvitees=numberofInvitees, invitee1=invitee1,invitee2=invitee2,invitee3=invitee3,invitee4=invitee4,invitee5=invitee5,invitee6=invitee6, inviteGroup=inviteGroup)

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

##app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))