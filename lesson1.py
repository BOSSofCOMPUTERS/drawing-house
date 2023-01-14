from turtle import *    


#we want to paint a house

#step 1: draw a square

speed(40)
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
end_fill()
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows
#windowvnumber 1
penup()
goto(200,130)
pendown()

begin_fill()
color("green")
right(150)
forward (55)
left(90)
   
forward (55)
left(90)
   
forward (55)
left(90)

forward (55)
left(90)
end_fill()


#window number 2
begin_fill()
penup()
goto(0,130)
pendown()

color("green")

forward (55)
right(90)
   
forward (55)
right(90)
   
forward (55)
right(90)

forward (55)
right(90)
end_fill()
   

exitonclick()