"""
CS321 Project 4
Pong (Paddle) - test code
11/16/2021
"""

import sys
sys.path.append("../after/")
import class_based_pong_after as pong


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


def test_make_window():
    pong.make_window("Connect 4", "light sky blue", 800, 600)
    pong.window.bgcolor() == "light sky blue"
    game.window.screensize() == (800, 600)
    game.window.tracer() == 0


# def test_make_turtle():
#     game = connect4.Connect4(-150, 200, 50, 1)
#     game.make_turtle("classic", "white", 1, 1, 0, 0)
#     assert game.turt.speed() == 0
#     assert game.turt.shape() == "classic"
#     assert game.turt.pencolor() == "white"
#     assert game.turt.shapesize()[0] == 1
#     assert game.turt.shapesize()[1] == 1
#     assert game.turt.pos() == (0.00, 0.00)