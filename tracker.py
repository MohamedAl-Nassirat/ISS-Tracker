import json
import turtle
import urllib.request
import time

# Initalize the turtle screen
screen = turtle.Screen()
screen.setup(1280,720)
screen.setworldcoordinates(-180,-90,180,90)

# Load in the map and the ISS
screen.bgpic("map.gif")
screen.register_shape("iss.gif")

# Long text
longt = turtle.Turtle()
longt.penup()
longt.hideturtle()

# Lat text
latit = turtle.Turtle()
latit.penup()
latit.hideturtle()

# Line draw
line = turtle.Turtle()
line.penup()
line.hideturtle()

# ISS Shape
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45) 
iss.penup()

#Velocity Text
velocityText = turtle.Turtle()
velocityText.penup()
velocityText.hideturtle()




font= ("Arial", 15, "normal") 


# Update the location on  the screen
while True:
    try:
        # ISS Long + Lat API
        url = "http://api.open-notify.org/iss-now.json"
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())

        # Orbital Velocity API 
        url2 = "https://api.wheretheiss.at/v1/satellites/25544"
        response2= urllib.request.urlopen(url2)
        result2 = json.loads(response2.read())
    except:
        print("API fetching failed.")
    # Load in values from the API
    latitude = float(result["iss_position"]["latitude"])
    longitude =  float(result["iss_position"]["longitude"])
    velocity = float(result2["velocity"])
    longt.goto(0,-80)
    latit.goto(0,-75)
    velocityText.goto(0,-85)
    iss.goto(longitude,latitude) #update shape position with the new long, 
    line.goto(longitude,latitude)

    line.pencolor("red")
    line.pendown()

    longt.clear()
    longt.write("Longitude: "+str(longitude),font, align="left")
    latit.clear()
    latit.write("Latitude: " + str(latitude),font, align="left")
    velocityText.clear()
    velocityText.write("Velocity: "+ str(velocity) + " km/h",font, align="left")
    time.sleep(5) # Update every 5s =


    

    