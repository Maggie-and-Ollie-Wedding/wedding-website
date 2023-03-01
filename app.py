from flask import Flask, render_template, request, Response #imports functions to use python with html
import os
from datetime import date, datetime

app = Flask("maggie-and-ollie-wedding") #making an app

#Homepage
@app.route("/")  
def landing_page():

    today = date.today()
    wedding = date(2024, 5, 18)
    time_left = wedding - today
    days_left = time_left.days
    print(days_left)
    
    return render_template("index.html", days_left=days_left)

#Ceremony
@app.route("/ceremony")  
def ceremony_page():
        return render_template("ceremony.html")
#RSVP
@app.route("/rsvp")  
def rsvp_page():
        return render_template("RSVP.html")

#Transport and Accommodation
@app.route("/transport-and-accommodation")
def transport_and_accommodation_page():
    return render_template("transport_and_accommodation.html")

#Choir
@app.route("/choir")  
def choir_page():
        return render_template("choir.html")


###debugging
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
###app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.

##app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))