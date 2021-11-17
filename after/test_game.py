"""
CS321 Project 4
Pong (Game) - test code
11/16/2021
"""

import sys
sys.path.append("../after/")
import class_based_pong_after as pong


def test_init():
    game = pong.Game(800, 600, 350, 0)
    assert game.window.bgcolor() == "black"

    assert game.score_player1 == 0
    assert game.score_player2 == 0

    assert game.paddle_1.x_position == -350
    assert game.paddle_1.y_position == 0
    assert game.paddle_2.x_position == 350

    assert game.pen.shape() == "square"
    assert game.pen.pencolor() == "white"
    assert game.pen.shapesize()[0] == 1
    assert game.pen.shapesize()[1] == 1
    assert game.pen.pos() == (0.00, 260.00)
    assert game.pen.isvisible() == False

    assert game.border == 350

def test_player_win():
    game = pong.Game(800, 600, 350, 0)
    game.player_win()

    assert game.ball.x_position == 0
    assert game.ball.y_position == 0
    assert game.pen.pos() == (0.00, 0.00)
    assert game.ball.ball_d["dx"] == 0.0925

def test_collision():
    game = pong.Game(800, 600, 350, 0)
    game.collision(280)

    assert game.ball.x_position == 280
    assert game.ball.y_position == 0
    assert game.pen.pos() == (280.00, 0.00)
    assert game.ball.ball_d["dx"] == -1.5 * 0.0925
    assert game.ball.ball_dx_initial == -0.0925