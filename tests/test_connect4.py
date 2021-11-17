"""
CS321 Project 4
Yixuan Qiu and Xiangxi Mu
Connect 4 - test code
11/15/2021
"""

import sys
sys.path.append("../after/")
import connect4_after as connect4


def test_init():
    game = connect4.Connect4(x_offset=-150, y_offset=200, tile_size=50, turn=1)

    assert game.window == None
    assert game.window == None
    assert len(game.grid) == 5
    assert len(game.grid[0]) == 7
    assert game.x_offset == -150
    assert game.y_offset == 200
    assert game.tile_size == 50
    assert game.turn == 1


def test_make_window():
    game = connect4.Connect4(-150, 200, 50, 1)
    game.make_window("Connect 4", "light sky blue", 800, 600)
    game.window.bgcolor() == "light sky blue"
    game.window.screensize() == (800, 600)
    game.window.tracer() == 0


def test_make_turtle():
    game = connect4.Connect4(-150, 200, 50, 1)
    game.make_turtle("classic", "white", 1, 1, 0, 0)
    assert game.turt.speed() == 0
    assert game.turt.shape() == "classic"
    assert game.turt.pencolor() == "white"
    assert game.turt.shapesize()[0] == 1
    assert game.turt.shapesize()[1] == 1
    assert game.turt.pos() == (0.00, 0.00)


def test_teleport():
    game = connect4.Connect4(-150, 200, 50, 1)
    game.make_window("Connect 4", "light sky blue", 800, 600)
    game.make_turtle("classic", "white", 1, 1, 0, 0)
    game.teleport(150, -200)
    assert game.turt.isdown() == True
    assert game.turt.pos() == (150.00, -200.00)


def test_draw_grid():
    game = connect4.Connect4(-150, 200, 50, 1)
    game.make_window("Connect 4", "light sky blue", 800, 600)
    game.make_turtle("classic", "white", 1, 1, 0, 0)

    game.draw_grid(-150, 200)
    assert game.turt.pos() == (-150 + 6 * 50, 200 - 4 * 50)


def test_get_coords_in_grid():
    game = connect4.Connect4(-150, 200, 50, 1)
    game.make_window("Connect 4", "light sky blue", 800, 600)
    game.make_turtle("classic", "white", 1, 1, 0, 0)

    assert game.get_coords_in_grid(100, 100) == (2, 5)


def test_set_turn():
    game = connect4.Connect4(-150, 200, 50, 1)
    game.make_window("Connect 4", "light sky blue", 800, 600)
    game.make_turtle("classic", "white", 1, 1, 0, 0)

    game.turn = 1
    game.grid[1][1] = 0
    game.set_turn(1, 1)
    assert game.grid[1][1] == 1

    game.turn = 2
    game.grid[2][2] = 0
    game.set_turn(2, 2)
    assert game.grid[2][2] == 2


def test_update_move():
    game = connect4.Connect4(-150, 200, 50, 1)
    game.make_window("Connect 4", "light sky blue", 800, 600)
    game.make_turtle("classic", "white", 1, 1, 0, 0)

    assert game.turn == 1

    game.update_move()
    assert game.turn == 2

    game.update_move()
    assert game.turn == 1


def test_check_bounds():
    game = connect4.Connect4(-150, 200, 50, 1)
    game.make_window("Connect 4", "light sky blue", 800, 600)
    game.make_turtle("classic", "white", 1, 1, 0, 0)

    game.check_bounds(0, 0)
    assert game.grid[0][0] == 1
    assert game.turn == 2

    game.check_bounds(1, 1)
    assert game.grid[1][1] == 2
    assert game.turn == 1

    game.check_bounds(5, 2)
    assert game.turn == 1, "Invalid position: (5, 2)"

    game.check_bounds(3, 7)
    assert game.turn == 1, "Invalid position: (3, 7)"


def test_play():
    game = connect4.Connect4(-150, 200, 50, 1)
    game.make_window("Connect 4", "light sky blue", 800, 600)
    game.make_turtle("classic", "white", 1, 1, 0, 0)

    game.play(100, 100)
    assert game.grid[2][5] == 1
    assert game.turn == 2
