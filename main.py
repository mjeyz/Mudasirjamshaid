from turtle import Turtle, Screen, colormode
import random

# Initialize the turtle and screen
timmy = Turtle()
timmy.speed("fastest")
timmy.pensize(15)
colormode(255)

# Function to generate random colors
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Define possible directions
directions = [0, 90, 180, 270]

# Random walk loop
for num_steps in range(300):
    timmy.color(random_colors())  # Use the random_colors function
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

# Keep the screen open
screen = Screen()
screen.mainloop()
