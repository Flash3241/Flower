import turtle

# Function to draw the main stem and recursive branching
def draw_flower(i):
    if i < 5:  # Base condition to stop recursion, adjusted for smaller flowers
        return
    
    # Draw the main stem
    turtle.color("green")
    turtle.forward(i)
    
    # Draw a smaller flower branch recursively
    turtle.left(30)
    draw_flower(3 * i / 4)
    
    # Turn to the right and draw another flower branch
    turtle.right(60)
    draw_flower(3 * i / 4)
    
    # Turn back to the left to the original angle and draw petals
    turtle.left(30)
    draw_petals(i)
    
    # Move back down the stem
    turtle.backward(i)

# Function to draw petals at the end of each stem
def draw_petals(size):
    turtle.color("white")  # Change color to white for petals
    for _ in range(6):  # Drawing a simple flower shape with 6 petals
        turtle.forward(size / 4)
        turtle.backward(size / 4)
        turtle.right(60)
    turtle.color("green")  # Switch back to green for the stem

# Function to write text on the screen
def write_text():
    text = turtle.Turtle()
    text.hideturtle()
    text.speed(100)
    text.penup()
    text.goto(0, -150)  # Position the text at the bottom, adjusted for smaller bouquet
    text.color("white")
    text.write("I Love You", align="center", font=("Arial", 16, "normal"))


# Set up the turtle graphics
turtle.speed(1000)  # Increase drawing speed
turtle.bgcolor("black")
turtle.color("green")
turtle.left(90)  # Start facing upwards


#instantly draw the flower
#turtle.speed(0)           # Fastest speed
#turtle.hideturtle()       # Hide turtle icon
#turtle.tracer(0, 0)       # Disable auto-refresh
#turtle.bgcolor("black")
#turtle.left(90)           # Point upwards

# Draw the flower pattern starting from the root with a smaller initial size
draw_flower(60)

# Write the text on the screen
write_text()

# Keep the window open until it is closed by the user
turtle.done()
