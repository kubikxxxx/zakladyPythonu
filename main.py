from turtle import *
import random
shape("turtle")
penup()
backward(200)
right(90)
forward(300)
left(90)
pendown()
speed(0)
for j in range(0,10):
    for i in range(0,360):
        forward(3)
        left(1)
        i+=1

    forward(50)
mainloop()