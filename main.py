from flask import Flask, render_template, request, Response #imports functions to use python with html
import os

app = Flask("magie-and-ollie-wedding") #making an app

#Homepage
@app.route("/")  
def landing_page():
        return render_template("index.html")

#RSVP
@app.route("/rsvp")  
def rsvp_page():
        return render_template("RSVP.html")

#Ceremony
@app.route("/ceremony")  
def ceremony_page():
        return render_template("ceremony.html")

#Choir
@app.route("/choir")  
def choir_page():
        return render_template("choir.html")

###debugging
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
###app.run(debug=True) #runs the app. the debug part - unlocks debugging feature.
##app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
