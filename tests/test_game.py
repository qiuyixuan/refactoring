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
    assert game.paddle_2.y_position == 0
