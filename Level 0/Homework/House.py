from turtle import *

#we want to paint a house

#step 1:   draw a square
begin_fill()
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#drawing the window
penup()
left(30)
forward(60)
left(90)
forward(10)
pendown()
color("blue")
forward(45)
forward(10)
right(90)
forward(40)
right(90)
forward(65)
right(90)
forward(40)
right(90)
forward(10)

exitonclick()