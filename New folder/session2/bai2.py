from turtle import *
shape("turtle")
speed(-2)
length = 1
for i in range(1, 10000, 5):
    #length = length + 5
    length += 5
    forward(length)
    left(90)



mainloop()
