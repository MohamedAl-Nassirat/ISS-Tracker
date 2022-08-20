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
# Register ISS as a shape to be able to move
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45) # 45 Deg
iss.penup()

input("start")


# Update the location on the screen
while True:
    url = "http://api.open-notify.org/iss-now.json" # Fetch API
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    latitude = float(result["iss_position"]["latitude"])
    longitude =  float(result["iss_position"]["longitude"]) 
    iss.goto(longitude,latitude) #update shape position with the new long, 
    time.sleep(5) # Update every 5s =
    iss.write(longitude,font=("Arial", 8, "normal") , align="center")


    

