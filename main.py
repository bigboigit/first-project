# Title: ML Final
# Kiarash Jalali
# 2020-11-30
# This page is the main program for the ML prediction


from model import final_data
from turtle import Screen, Turtle

font_height = 8
FONT = ('Arial', font_height, 'normal')
BORDER = font_height

"""
    Basicly a function that draws a rectangle based on its inputs 
    while "printing" the value of the rectangle so it makes it 
    look like we have a bar graph with labels
"""
# I know I could havea put this draw function in a diffrent file
# But I wouldn't work for some weird reason
def drawBar(t, datum):
    label, height = datum

    t.left(90)

    t.begin_fill()
    t.forward(height)
    t.right(90)
    t.forward(20)

    # Checking if height is bigger than 0 then print the data
    if height > 0:
        t.write(height, align="center", font=FONT)
    
    t.forward(20)
    t.right(90)
    t.forward(height)
    t.end_fill()

    t.left(90)

    t.backward(40)
    t.forward(20)
    t.write(label, align="center", font=FONT)
    t.forward(20)

data = final_data

""" 
    Finding the max number in the data as well as 
    the len of the data (numner of the bars)
"""
maxheight = max(data.values())
numbars = len(data)

screen = Screen()
# Giving the program a title
screen.title('Bar Chart of Predicted Model')
# Nice bg color
screen.bgcolor('medium purple')

# Calculating the size of the screen according to the input size (number of bars)
screen.setworldcoordinates(-BORDER, -BORDER, 40 * numbars + BORDER, maxheight + BORDER)

# Initializing turtle settings, like speed, color and pensize  
turtle = Turtle()
turtle.speed('fast') 
turtle.fillcolor('red')
turtle.pensize(3)

# Going thru each item in the dict to draw it
for datum in data.items():
    drawBar(turtle, datum)

# Hiding the "turtle" when the drawing is done since its ugly
turtle.hideturtle()

# Cool little function that quits as soon as you click on the window
screen.exitonclick()