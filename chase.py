from google.cloud import bigquery

list_to_chase = []
list_of_invites = []
invite_count = 0
invitee_count = 0

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
    WHERE Active = true
"""
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

        
        # Execute the RSVP query
        rsvp_query_job = client.query(rsvp_query)

        # Append unique email addresses to the list
        for rsvp_row in rsvp_query_job:
            email = rsvp_row["Email"]
            invitee_count+=1
            if email not in list_to_chase:
                list_to_chase.append(email)
                
            if invite_id not in list_of_invites:
                list_of_invites.append(invite_id)
                invite_count+=1

print(list_to_chase)
print(invitee_count)
print(list_of_invites)
print(invite_count)