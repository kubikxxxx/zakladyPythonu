from turtle import *
import tkinter as tk
import math


def virus():
    shape("triangle")
    penup()
    setposition(-300, 0)
    pendown()
    speed(0)
    for j in range(10):
        for i in range(10, 200):
            forward(10 - i)
            left(1 * j - i)
        forward(50)
    mainloop()

def pacman():
    right(150)
    forward(115)
    left(90)
    speed(0)
    for i in range(600):
        forward(1)
        left(0.5)
        pencolor("yellow")
        left(90)
        forward(115)
        backward(115)
        right(90)
        pencolor("black")
    left(90)
    forward(115)
    mainloop()

def oval():
    penup()
    setposition(300, 0)
    left(90)
    pendown()
    for _ in range(2):
        i = 0
        while i < 90:
            forward(i / 10)
            left(1)
            i += 1
        while i > 0:
            forward(i / 10)
            left(1)
            i -= 1
    mainloop()

def spiral():
    bgcolor("black")
    pen = Turtle()
    pen.speed(0)
    pen.width(2)
    pen.color("cyan")

    def drawSpiralCircles(size, angle, increment):
        for _ in range(200):
            pen.circle(size)
            pen.right(angle)
            size += increment

    drawSpiralCircles(10, 30, 2)
    mainloop()


def spustit_animaci(animace):
    root.destroy()
    animace()


root = tk.Tk()
root.title("Výběr animace")


label = tk.Label(root, text="Vyber animaci:", font=("Arial", 14))
label.pack(pady=10)


btn_virus = tk.Button(root, text="Virus", command=lambda: spustit_animaci(virus))
btn_virus.pack(pady=5)

btn_pacman = tk.Button(root, text="Pacman", command=lambda: spustit_animaci(pacman))
btn_pacman.pack(pady=5)

btn_oval = tk.Button(root, text="Oval", command=lambda: spustit_animaci(oval))
btn_oval.pack(pady=5)

btn_spiral = tk.Button(root, text="Spirálová kružnice", command=lambda: spustit_animaci(spiral))
btn_spiral.pack(pady=5)


root.mainloop()
