from turtle import Turtle
from turtle import Screen


yoon = Turtle()
screen = Screen()


def moves_forward():
    yoon.forward(10)

def moves_backward():
    yoon.backward(10)
    
def counter_clockwise():
    yoon.left(25)

def clockwise():
    yoon.right(25)
    
def clear_drawing():
    screen.resetscreen()





screen.onkey(moves_forward, "w")
screen.listen()
screen.onkey(moves_backward, "s")
screen.listen()
screen.onkey(counter_clockwise, "a")
screen.listen()
screen.onkey(clockwise, "d")
screen.listen()
screen.onkey(clear_drawing, "c")
screen.listen()

screen.exitonclick()