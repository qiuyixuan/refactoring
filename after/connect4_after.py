"""
CS321 Project 4
Yixuan Qiu and Xiangxi Mu
Connect 4 - Refactored
11/13/2021
"""

import turtle


class Connect4:
    def __init__(self, x_offset, y_offset, tile_size, turn):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.tile_size = tile_size
        self.turn = turn

        self.window = None
        self.turt = None
        self.grid = []

        for row in range(5):
            self.grid.append([0] * 7)

    def make_window(self, window_title, bgcolor, width, height):
        """ this function creates a screen object """

        self.window = turtle.getscreen()  # Set the window size
        self.window.title(window_title)
        self.window.bgcolor(bgcolor)
        self.window.setup(width, height)
        # turns off screen updates for the window Speeds up the game
        self.window.tracer(0)

    def make_turtle(self, shape, color, stretch_width, stretch_length, x_pos, y_pos):
        """ creates a turtle and sets initial position """

        self.turt = turtle.Turtle()
        self.turt.speed(0)  # Speed of animation, 0 is max
        self.turt.shape(shape)
        self.turt.color(color)
        self.turt.shapesize(stretch_width, stretch_length)
        self.teleport(x_pos, y_pos)

    def teleport(self, x_pos, y_pos):
        """ sends turtle to x_pos, y_pos """
        self.turt.up()
        self.turt.goto(x_pos, y_pos)
        self.turt.down()

    def draw_circle(self, row, col):
        """ draws a colored circle depending on the position"""
        if self.grid[row][col] == 1:
            self.turt.dot(self.tile_size - 5, "red")

        elif self.grid[row][col] == 2:
            self.turt.dot(self.tile_size - 5, "yellow")

        else:
            self.turt.dot(self.tile_size - 5, "white")

    def draw_grid(self, x_pos, y_pos):
        """ draws a grid at x, y with a specific tile_size """

        self.teleport(x_pos, y_pos)

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                self.teleport(
                    x_pos + col * self.tile_size, y_pos - row * self.tile_size
                )
                self.draw_circle(row, col)

    def check_win(self, grid, player):
        """ checks the winner in the grid
        returns true if player won
        returns false if player lost
        """

        count = 0

        # check rows
        for row in range(len(self.grid)):
            count = 0
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == player:
                    count += 1

                    if count == 4:
                        return True
                else:
                    count = 0

        # check columns
        for col in range(len(grid[0])):
            count = 0
            for row in range(len(self.grid)):
                if self.grid[row][col] == player:
                    count += 1

                    if count == 4:
                        return True
                else:
                    count = 0

        # check diagonal
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):

                if row + 3 < len(grid) and col + 3 < len(grid[row]):
                    if (
                        self.grid[row][col] == 1
                        and self.grid[row + 1][col + 1] == 1
                        and self.grid[row + 2][col + 2] == 1
                        and self.grid[row + 3][col + 3] == 1
                    ):
                        return True

    def get_coords_in_grid(self, x_pos, y_pos):
        """ convert coordinates to row and col """
        row = int(abs((y_pos - self.y_offset - 25) // (50) + 1))
        col = int(abs((x_pos - self.x_offset - 25) // (50) + 1))
        print(f"({row}, {col})")
        return row, col

    def set_turn(self, row, col):
        """ set a the value of self.turn """
        # change the clicked cell in the self.grid to hold value self.turn
        if self.grid[row][col] == 0:
            self.grid[row][col] = self.turn

    def update_move(self):
        """ updates window, switches player turn and checks who wins """
        self.draw_grid(self.x_offset, self.y_offset)
        self.window.update()

        if self.check_win(self.grid, 1):
            print("player 1 won")

        elif self.check_win(self.grid, 2):
            print("player 2 won")

        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def check_bounds(self, row, col):
        """ checks invalid movements (out of bounds) """
        if row > 4 or col > 6:
            print(f"Invalid position: ({row}, {col})")
        else:
            self.set_turn(row, col)
            self.update_move()

    def play(self, x_pos, y_pos):
        """ plays the game """
        row, col = self.get_coords_in_grid(x_pos, y_pos)
        self.check_bounds(row, col)


def main():
    """ the main function where the game events take place """

    game = Connect4(x_offset=-150, y_offset=200, tile_size=50, turn=1)
    game.make_window("Connect 4", "light sky blue", 800, 600)
    game.make_turtle("classic", "white", 1, 1, 0, 0)

    game.draw_grid(game.x_offset, game.y_offset)

    game.window.onscreenclick(game.play)
    game.window.listen()

    while True:

        input_row = int(input("enter row, player " + str(game.turn) + ": "))
        input_col = int(input("enter col, player " + str(game.turn) + ": "))

        game.check_bounds(input_row, input_col)


if __name__ == "__main__":
    main()
