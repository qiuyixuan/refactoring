"""
CS321 Project 4
Pong (Paddle) - test code
11/16/2021
"""

import sys
sys.path.append("../after/")
import class_based_pong_after as pong


def test_make_window():
    window = pong.make_window("Pong", "light sky blue", 800, 600)
    assert window.bgcolor() == "light sky blue"
    assert window.tracer() == 0


def test_make_turtle():
    turt = pong.make_turtle("classic", "white", 1, 1, 0, 0)
    assert turt.speed() == 0
    assert turt.shape() == "classic"
    assert turt.pencolor() == "white"
    assert turt.shapesize()[0] == 1
    assert turt.shapesize()[1] == 1
    assert turt.pos() == (0.00, 0.00)

def test_init():
    paddle = pong.Paddle(100, -200)

    assert paddle.distance == 20
    paddle.x_position = 100
    paddle.y_position = -200

    assert paddle.turt.shape() == "square"
    assert paddle.turt.pencolor() == "white"
    assert paddle.turt.shapesize()[0] == 5
    assert paddle.turt.shapesize()[1] == 1
    assert paddle.turt.pos() == (100.00, -200.00)

def test__up():
    paddle = pong.Paddle(0, 0)
    paddle.up()
    assert paddle.turt.pos() == (0.00, 20.00)
    assert paddle.y_position == 20

def test_down():
    paddle = pong.Paddle(0, 0)
    paddle.down()
    assert paddle.turt.pos() == (0.00, -20.00)
    assert paddle.y_position == -20

def test_xcor():
    paddle = pong.Paddle(10, 20)
    assert paddle.xcor() == 10

def test_ycor():
    paddle = pong.Paddle(-10, -30)
    assert paddle.ycor() == -30
