import random
import turtle

t = turtle.Turtle()
t.speed(20)
col =["red","black"]
turtle.bgcolor("lavender")
for i in range(1000):
    t.color(random.choice(col) )
    t.fd(i)
    t.right(230)
