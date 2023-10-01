import resend
import os

resend.api_key = "re_fnGQipwL_FmXaWvjPETUQQHXgKYFePUmH"
# os.getenv('EMAIL_API_KEY')


resend.Domains.verify(domain_id="cfb7a984-a859-4411-a30d-c0bc8e13fce8")


html_body="""<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="x-apple-disable-message-reformatting" />

  <link
    href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&family=Playfair+Display&family=Playfair+Display+SC&display=swap"
    rel="stylesheet">

  <style>
    :root {

      --main-dark-colour: #091d36;

      --soft-dark-colour: #e1c892;

      --soft-background-colour: #ffffff;

      --warm-colour: #f1e2c7;


      --border-width: 5px;
      --colour-4: #e2c484;
    }




    body {
      
      text-align: center;
      background-attachment: fixed;
      background-position: center;
      background-repeat: no-repeat;
      width: 100vw;
      background-color: var(--soft-background-colour);
      overflow-x: hidden;
      overflow-y: scroll;
      min-width: 400px;
      height: auto;
      margin: 0px;
      font-family: "Playfair Display SC", serif;
      background-position: top center;
    }



    .page-section {
      width: 75vw;
      transition: transform 0.5s ease-in-out;
    }



    .cover-page-image {
      min-width: 375px;
      align-self: center;
      left:0px;
      right:0px;
      width: 100vw;
      min-height: 200px;
      max-height: 1000px;
      object-fit: cover;
      position: relative;
      display:flex;
    }




    #cover-page {

      color: var(--soft-background-colour);
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100vw;
      justify-content: center;
    }


    #cover-page .centered-text {
      text-align: center;
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

    .banner {
      height: auto;
      width: 100vw;
      border-radius: 300px 300px 0px 0px;
      position: relative;
    }


    .ceremony-and-reception-parent {
      display: flex;
      flex-direction: row;
      text-align: start;
      width: 100vw;
    }

    .ceremony-and-reception-child {
      display: flex;
      justify-content: center;
      flex: 1;

    }

    .ceremony-and-reception-grandchild {
      display: inline;
      justify-content: left;
      padding: 12px;
      flex: 1;

    }

    .rsvp-button {
      border: var(--main-dark-colour);
      color: var(--main-dark-colour);
      border: 5px solid var(--main-dark-colour);
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



    .div-display {

      display: flex;
      position: relative;
      justify-content: space-around;
    }

    .email-layout {
      display: flex;
      flex-direction: column;
      height: auto;
      width: 100vw;
      flex: 2;
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

    .email-content {
      padding: 10px;
    }

    .dot:after {
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


  <!-- title: CHANGE ME -->
  <title>Maggie and Ollie's Wedding!</title>
</head>

<body>
  <div class="email-layout">
    <div>
     


        <div class="banner">

          <img class="cover-page-image" title="bridge" style="display:block"
            src="https://lh3.googleusercontent.com/drive-viewer/AK7aPaBbT5jpHNRANnnOU1Uo2MC8vOYOgnxrKTHwZfYnqjVZx7FZJUIuBMOhcrGEXpu_xjY7uJBqDSGtMFBxFeUG2P3S9Ta-=s1600"
            alt="Maggie and Ollie on bridge">






        </div>


     
    </div>
    <div class="email-content">
      <div>
        <h6>with great pleasure</h6>
        <h2><span class="dot">Maggie Rose Prinn Hunt<br>&<br>Oliver John Benjamin Norman</span></h2>
        <h6>invite</h6>
        <h2>{invite_group}</h2>
        <h6>to join them for the celebration of their marriage<br>
          on</h6>
        <h2><span class="dot">Saturday the Eighteenth of May 2024</span></h2>
      </div>

      <div class="div-display">


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
                Carriages at 11.45pm</h5>
            </div>
          </div>

        </div>
      </div>
      <div>

        <div class="div-display">
          <div class="bus-box-div">
            <h6 class="bus-box">There is no parking at the church.<br><br>Please note we are providing transport from
              the ceremony to the reception venue.</h6>
          </div>
        </div>
        <div class="div-display">
          <h5>We we kindly request you RSVP by Friday the 17th of November 2023</h5>
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
      <div class="div-display">
        <img
          src="https://lh3.googleusercontent.com/drive-viewer/AK7aPaCVXW4CZ9rp_-qTvUrGv0g_mmgzQBf5Cvqiw1OoukWjh2OlARCOP8By9CWsd3GQO4UVcZsW1EydriWxSIdDSuvyQW0ezw=s1600"
          title="Logo" style="display:block" height="auto" width="100px">
      </div>


    </div>
  </div>
</body>"""

r = resend.Emails.send(
    {
        "from": "rsvp-noreply@maggieandolliewedding.party",
        "to": 'maggie.rphunt@gmail.com',
        "html": html_body,
        "cc": "maggie.and.ollie.wedding@gmail.com",
        "reply_to": "maggie.and.ollie.wedding@gmail.com",
        "subject": f"RSVP",
    }
)