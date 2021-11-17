"""
CS321 Project 4
Pong (Ball) - test code
11/16/2021
"""

import sys
sys.path.append("../after/")
import class_based_pong_after as pong


def test_init():
    ball = pong.Ball()

    assert ball.turt.shape() == "square"
    assert ball.turt.pencolor() == "white"
    assert ball.turt.shapesize()[0] == 1
    assert ball.turt.shapesize()[1] == 1
    assert ball.turt.pos() == (0.00, 0.00)

    assert ball.ball_d == {"dx": 0.0925, "dy": 0.0925}
    assert ball.ball_dx_inital == 0.0925
    assert ball.border == 290
    assert ball.x_position == 0
    assert ball.y_position == 0

def test_xcor():
    ball = pong.Ball()
    assert ball.xcor() == 0

def test_ycor():
    ball = pong.Ball()
    assert ball.ycor() == 0

def test_goto():
    ball = pong.Ball()
    ball.goto(-250, 155)
    assert ball.turt.pos() == (-250.00,155.00)
    assert ball.x_position == -250
    assert ball.y_position == 155

def test_move():
    ball = pong.Ball()
    ball.move()
    assert ball.turt.pos() == (0.0925, 0.0925)
    assert ball.x_position == 0.0925
    assert ball.y_position == 0.0925

def test_ifBorder():
    ball = pong.Ball()

    for i in range(3136):
        ball.move()

    assert ball.ycor() == 290
    assert ball.ball_d["dy"] == -0.0925
