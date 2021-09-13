import random
from turtle import Turtle, Screen


def goto_start_position(turtle, x_axis, y_axis):
    turtle.goto(x_axis, y_axis)


def create_turtle(racer_color):
    x = Turtle(shape='turtle')
    x.color(racer_color)
    return x


is_race_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "purple"]
turtles = [create_turtle(x) for x in colors]

if user_bet:
    is_race_on = True

# temp_x = -230
y = -100
for racer in turtles:
    racer.penup()
    goto_start_position(racer, x_axis=-230, y_axis=y)
    y += 30

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()
            msg = f"You Won! The {user_bet} turtle is the winner" if winner_color == user_bet\
                else f"You Lost! The {winner_color} turtle is the winner"
            print(msg)
            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

my_screen.exitonclick()
