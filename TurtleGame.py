# Turtle Game using the package 'turtle'!

# Import relevant modules
import turtle
import random
import time

# setting up a nice screen for our game!
screen = turtle.Screen()
screen.bgcolor('lightblue')  # Background- light blue colour

# We want 2 players in this game and the idea is that
# whoever gets to the otherside wins!

player_one = turtle.Turtle()
# Colour of player one
player_one.color('blue')
# Make this player look like a turtle
player_one.shape('turtle')

# Player two- basic set up
player_two = player_one.clone()
# Colour of player two
player_two.color('red')

# Let's position our players!
player_one.penup()
player_one.goto(-300, 200)
player_two.penup()
player_two.goto(-300, -200)

# Draw a Finish Line
player_one.goto(300, -250)
player_one.left(90)
player_one.pendown()
player_one.color('black')
player_one.forward(500)
player_one.write('Finish!', font=48)

# Returns Player One to return to starting position
player_one.penup()
player_one.color('blue')
player_one.left(90)
player_one.goto(-300, 200)
player_one.right(180)

# Make sure pens are down
player_one.pendown()
player_two.pendown()

# Die values
die = [1, 2, 3, 4, 5, 6]

# Let's create the game!!
for i in range(30):
    if player_one.pos() >= (300, 250):
        print("Player One Wins the Race!")
        player_one.penup()
        player_one.goto(0, 0)
        player_one.write('I Won the Race!', font=72)
        break
    elif player_two.pos() >= (300, 250):
        print("Player Two Wins the Race!")
        player_two.penup()
        player_two.goto(0, 0)
        player_two.pendown()
        player_two.write('I Won the Race!', font=72)
        break
    else:
        die_roll = random.choice(die)
        player_one.forward(die_roll * 30)
        time.sleep(1)
        die_roll2 = random.choice(die)
        player_two.forward(die_roll2 * 30)
        time.sleep(1)

# This keeps the turtle drawing on the screen
turtle.done()
