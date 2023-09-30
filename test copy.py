import resend
import os

resend.api_key = os.getenv('EMAIL_API_KEY')
email_address1 = "maggie.rphunt@gmail.com"
email_address2 = "maggie.hunt@paconsulting.com"
email_address3 = "maggie.rph@hotmail.co.uk"

email_addresses = []
email_content_list = []

email_addresses.append(email_address1)
email_content_list.append('xyz')

invite_group = "Testing 1 & 2"
email_content = ' '.join(str(rsvp) for rsvp in email_content_list)


html_body=f"<p> Dear {invite_group},<br><br>Thank you for your RSVP!<br><br> Please see summary confirmation below:<br><br>\
        {email_content} <br><br>\
        Please <a href='mailto:maggie.and.ollie.wedding@gmail.com'>get in touch</a> if any of this is incorrect.<br><br>\
        We can't wait to celebrate with you! You can return to our <a href='www.maggieandolliewedding.party'>wedding website</a>\
        if you would like to review the ceremony details, dress code, and other details.<br><br>\
        Love,<br><br>\
        Maggie & Ollie</p>"

r = resend.Emails.send({
  "from": "rsvp-noreply@maggieandolliewedding.party",
  "to":  email_addresses,
  "cc": "maggie.and.ollie.wedding@gmail.com",
  "subject": f"RSVP - {invite_group}",
  "reply_to": "maggie.and.ollie.wedding@gmail.com",
  "html": html_body
        })