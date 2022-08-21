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
longt = turtle.Turtle()
longt.penup()
longt.hideturtle()
line = turtle.Turtle()
line.penup()
line.hideturtle()
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45) # 45 Deg
iss.penup()
#input("start")


# Update the location on the screen
while True:
    url = "http://api.open-notify.org/iss-now.json" # Fetch API
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    latitude = float(result["iss_position"]["latitude"])
    longitude =  float(result["iss_position"]["longitude"]) 
    longt.goto(0,-75)
    iss.goto(longitude,latitude) #update shape position with the new long, 
    line.goto(longitude,latitude)
    line.pencolor("red")
    line.pendown()
    time.sleep(5) # Update every 5s =
    longt.clear()
    longt.write("longitude: "+str(longitude),font=("Arial", 15, "normal") , align="center")


    

    