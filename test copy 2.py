import resend
import os

resend.api_key = "re_fnGQipwL_FmXaWvjPETUQQHXgKYFePUmH"
# os.getenv('EMAIL_API_KEY')


resend.Domains.verify(domain_id="cfb7a984-a859-4411-a30d-c0bc8e13fce8")

invite_group = "test"
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
      <div><p>Dear </p>
        <p>"""
html_body_2="""</p></div>

      <div class="div-display">
       <a href="https://www.maggieandolliewedding.party"> <img
          src="https://lh3.googleusercontent.com/drive-viewer/AK7aPaDS14085OBWeL6zvD1cKPonkSi-v0z3gdC3sqStnIXA6XAzz3EAB5La87I8gXnAKBSvcUFdcZxyJbFkrpnByUV5PDXY=s1600"
          title="Logo" style="display:block" height="auto" width="100%" ></a>
      </div>


    </div>
  </div>
</body>"""

email = html_body_1+invite_group+html_body_2
r = resend.Emails.send(
    {
        "from": "rsvp-noreply@maggieandolliewedding.party",
        "to": 'maggie.rphunt@gmail.com',
        "html": email,
        "cc": "maggie.and.ollie.wedding@gmail.com",
        "reply_to": "maggie.and.ollie.wedding@gmail.com",
        "subject": f"RSVP - {invite_group}",
    }
)