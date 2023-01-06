
# import turtle as p
from turtle import *

#1. Shapes and colors:
#shape("arrow") # changes to arrow
#print(shape())  #default is classic
# help(color) #details about colors
# color("yellow") #changed color amd line both
# color("yellow","black") #line and then turtle
 
#2. bgcolor, title, bgpic:
# bgpic("file name from within the folder")  # to change background pic
# bgcolor("black") #background color , can be (r,g,b) too
# title("Prajwal") #changing the title of window


#3. turtle movement: fd bd rt lt sethheading:
# forward(200) #200 pixels , use forward or Fd
# right(90) #90 deg right
# setheading(180)  or seth #turtle pointer heading angle



#4. square shapes,fill color, speed , hide:

# speed(1) # sets speed of the turtle
# help(speed) #know the info the speeds
''' begin_fill()  # beginning and ending of the color fill should be metioned
fillcolor("red")
for i in range(4):  # square
    forward(100)
    left(90) 
end_fill() '''
# hideturtle() # hides the turtle pointer


#5 circles ans steps:
# circle(100) #(radius,degree)
# circle(100, steps=5)  #draws a particular steps within the circumference of the circle


#6 Drawing at different positions: goto, setpos,setposition
# for i in range(1,5):
'''up()
goto(100,100)  # goes to that position without drawing the line
down()
circle(50)
'''

#7 Drawing circle at different locations
speed(0)

for i in range(10):
    if(i%2==0):

        color('green')
        circle(3*i+50)

    else:
        circle(3*i+50)












screensize(canvwidth=1000, canvheight=2000, bg=None)
# reset() # resets everything
# pensize # to increase the size of outer line
# home() # sets the turtle to the initial position

done() #holding screen

