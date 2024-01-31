from turtle import *

#we want to paint a house


#step 1: draw a square
speed(30)
width(7)

color("blue")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
forward(70)
end_fill()
#end of square

#drawing the door

color("green")
begin_fill()
left(90)
forward(120)     #hight of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end of the door

#drawing the roof
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
#end of the roof

#drawing a window
color("brown") 
width(3)
penup()
goto(15, 160)
pendown()


begin_fill()
color("yellow")
left(30)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()


#second window



penup()
goto(180, 160)
pendown()

begin_fill()
color("yellow")

forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

end_fill()


#end second window




exitonclick()