import resend
import os

resend.api_key = "re_fnGQipwL_FmXaWvjPETUQQHXgKYFePUmH"
# os.getenv('EMAIL_API_KEY')


resend.Domains.verify(domain_id="cfb7a984-a859-4411-a30d-c0bc8e13fce8")

r = resend.Emails.send(
    {
        "from": "rsvp-noreply@maggieandolliewedding.party",
        "to": "maggie.rphunt@gmail.com",
        "html": "<p>hi</p>",
        "subject": "hi",
    }
)


from google.cloud import bigquery

list_of_sent = []

# Initialize a BigQuery client
client = bigquery.Client()

# Define the BigQuery table names and project ID
project_id = "maggie-and-ollie-wedding.wedding_1805."
invitations_table_name = "invitations_table"
rsvp_table_name = "RSVP_table"

# Create a list to store email addresses
email_addresses = []

# Query the invitations table for rows where Email_sent is false
query = f"""
    SELECT Invite_ID, Invite_Group_Name
    FROM `{project_id}.{invitations_table_name}`
    WHERE Email_sent = false
"""

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

    # Execute the RSVP query
    rsvp_query_job = client.query(rsvp_query)

    # Append unique email addresses to the list
    for rsvp_row in rsvp_query_job:
        email = rsvp_row["Email"]
        if email not in email_addresses:
            email_addresses.append(email)

    # Set the value of Invite_Group_Name to a variable called invitation_group

    print(email_addresses)

    html_body_part_1 = """
    <html>

    <head>

      <!-- stylesheets -->

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
          width: 100vw;
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
          width: 100vw;
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

          }
        }
      </style>


      <!-- title: CHANGE ME -->
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
        <div>
          <h6>with great pleasure</h6>
          <h2>Maggie Rose Prinn Hunt<br>&<br>Oliver John Benjamin Norman</h2>
          <h6>invite</h6>
          <h2>"""

    html_body_part_2 = """</h2>
          <h6>to join them for the celebration of their marriage<br>
            on</h6>
          <h2>Saturday the Eighteenth of May 2024</h2>
        </div>

        <div class="other-divs">


          <div class="page-section ceremony-and-reception-parent" id="ceremony-and-reception">
            <div class="ceremony-and-reception-child" id="ceremony">
              <h3>Ceremony</h3>
              <div class="ceremony-and-reception-grandchild">
                <h5>The Parish Church of <br>St Mary The Virgin,<br>Gamlingay<br><br>2pm
                </h5>
              </div>
            </div>
            <div class="ceremony-and-reception-child" id="reception">
              <h3>Reception</h3>
              <div class="ceremony-and-reception-grandchild">
                <h5>Wrest Park, <br>Silsoe<br><br>
                  Drinks, dinner and dancing from 4pm<br>
                  Carriages at 11.30pm</h5>
              </div>
            </div>

          </div>
        </div>
        <div>

          <div class="other-divs">
            <div class="bus-box-div">
              <h6 class="bus-box">There is no parking at the church.<br><br>Please note we are providing transport from
                the ceremony to the reception venue.</h6>
            </div>
          </div>
          <div class="other-divs">
            <h5>We we kindly request you RSVP by 17/11/23.</h5>
          </div>
          <div class="button-list-parent">
            <div class="rsvp-button button button-list-child" id="website">
              <a class="rsvp-button-link" href="https://www.maggieandolliewedding.party" target="_blank">
                <h2>Details and RSVP</h2>
              </a>
            </div>

            <br><br>



          </div>
        </div>


      </div>
    </body>
    """

    html_body = str(html_body_part_1 + invite_group + html_body_part_2)

    r = resend.Emails.send(
        {
            "from": "rsvp-noreply@maggieandolliewedding.party",
            "to": email_addresses,
            "html": html_body,
            "cc": "maggie.and.ollie.wedding@gmail.com",
            "reply_to": "maggie.and.ollie.wedding@gmail.com",
            "subject": f"RSVP - {invite_group}",
        }
    )

    update_sent_query = f"""
        UPDATE `{project_id}.{dataset_name}.{table_name}`
        SET Email_sent = TRUE
        WHERE Invite_ID = '{invite_id}'
    """

    query_job_update_sent = client.query(update_sent_query)

    # Wait for the query to complete
    query_job_update_sent.result()
    list_of_sent.append(invite_id)

print(list_of_sent)
