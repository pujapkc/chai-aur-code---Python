from turtle import Turtle,Screen

timmy_the_turtle = Turtle()

import random


#Draw a square

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

#Draw a Dashed line

# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

#Draw different shapes

# def draw_shape(num_of_side):
#     angle= 360/num_of_side

#     for _ in range(num_of_side):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)

    
# for shape_side in range(3,11):
#     draw_shape(shape_side)


#random walk
direction = [0,90,180,270]

timmy_the_turtle.pensize(3)
timmy_the_turtle.speed("fastest")

for _ in range(200):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.setheading(random.choice(direction))


screen = Screen()

screen.exitonclick()
