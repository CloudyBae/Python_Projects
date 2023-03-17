import random
import turtle

screen = turtle.Screen()
screen.colormode(255)

crush = turtle.Turtle()
crush.shape("turtle")
crush.speed("fastest")
crush.up()
crush.hideturtle()

color_list = [(226, 226, 225), (236, 236, 239), (182, 65, 34), (213, 149, 97), (14, 24, 42), (230, 237, 233), (239, 208, 94), (241, 234, 238), (237, 62, 33), (157, 26, 19), (72, 29, 32), (84, 94, 115), (166, 141, 66), (67, 41, 35), (120, 32, 37), (183, 85, 94), (135, 152, 164), (49, 52, 127), (229, 175, 161), (165, 64, 70)]

crush.setheading(225)
crush.forward(320)
crush.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    crush.dot(20, random.choice(color_list))
    crush.forward(50)

    if dot_count % 10 == 0:
        crush.setheading(90)
        crush.forward(50)
        crush.setheading(180)
        crush.forward(500)
        crush.setheading(0)

turtle.exitonclick()






