import turtle
import time
from playsound import playsound
from multiprocessing import Process


class Maze:
    def __init__(self, x_offset, y_offset, tile_size, steps):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.tile_size = tile_size
        self.steps = steps
        self.turt = None
        self.window = None
        self.grid = []

    def make_window(self, bgcolor="slate gray"):
        """ this function creates a screen object """
        self.window = turtle.getscreen()
        self.window.bgcolor(bgcolor)

    def make_turtle(self, shape="square", shape_width=2.5, shape_length=2.5):
        """ creates a turtle and sets initial position """
        self.turt = turtle.Turtle()
        turtle.hideturtle()
        self.turt.hideturtle()
        self.turt.shape(shape)
        self.turt.shapesize(shape_width, shape_length)

    def teleport(self, x_pos, y_pos):
        """ sends turtle to x_pos, y_pos """
        self.turt.up()
        self.turt.goto(x_pos, y_pos)
        self.turt.down()

    def draw_grid(self, x_pos, y_pos):
        """ draws a grid at x_pos, y_pos with a specific tile_size """

        self.window.tracer(False)  # turn off tracer for fast drawing

        self.teleport(x_pos, y_pos)

        # go over every cell in the grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):

                # move turtle to the position of the cell in the grid
                self.teleport(
                    x_pos + col * self.tile_size, y_pos - row * self.tile_size
                )

                # if the cell is an obstacle (X) draw a black dot
                if self.grid[row][col] == "X":
                    self.turt.color("grey", "black")

                # if the cell is the start drawing position (S) draw a yellow dot
                elif self.grid[row][col] == "S":
                    self.turt.color("grey", "yellow")

                # if the cell is the End position (E) draw a Red dot
                elif self.grid[row][col] == "E":
                    self.turt.color("grey", "red")

                # if the cell is part of a path (P) draw a royalblue dot
                elif self.grid[row][col] == "P":
                    self.turt.color("grey", "royalblue")

                # if the cell has been tried before (T) draw a light blue dot
                elif self.grid[row][col] == "T":
                    self.turt.color("grey", "light blue")

                # if the cell is part of a deadend (D) draw a gray dot
                elif self.grid[row][col] == "D":
                    self.turt.color("gainsboro", "gray")

                # else draw a white dot
                else:
                    self.turt.color("grey", "white")

                self.turt.stamp()

        # turn tracer back on
        self.window.tracer(True)

    def find_start(self):
        """ finds the start position (S) in the grid
        returns a tuple of start row and col
        """

        # go over every cell in the grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):

                # cell at row, col is 'S' return row and col as a tuple
                if self.grid[row][col] == "S":
                    return (row, col)

    def read_grid(self, file_name):
        """ reads a maze file and initializes a gird with its contents """

        # create an empty grid (an empty list called grid)
        # grid = []

        # open the text file
        file = open(file_name)

        # read a line from the file
        line = file.readline()

        # replace \n with nothing
        line = line.replace("\n", "")

        while line:
            # split the line into tokens
            tokens = line.split(",")

            # add the tokens to the grid as a single row
            self.grid.append(tokens)

            line = file.readline()

            # replace \n with nothing
            line = line.replace("\n", "")

    def search_from(self, row, col):
        """ recursive function to search the grid for the end (E) """

        self.steps += 1

        # make sure row and col are valid points on the grid
        if row < 0 or col < 0 or row == len(self.grid) or col == len(self.grid[0]):
            # return False if not valid
            return False

        # check that the grid cell at row and col is not obstacle, tried, or deadend
        if (
            self.grid[row][col] == "X"
            or self.grid[row][col] == "T"
            or self.grid[row][col] == "D"
        ):
            # return False if obstacle, tried, or deadend
            return False

        # If end is found at row, col return True
        if self.grid[row][col] == "E":
            return True

        # If the cell at row, col is not the start cell, mark the cell as tried (T)
        if self.grid[row][col] != "S":
            self.grid[row][col] = "T"

        # draw the grid
        self.draw_grid(self.x_offset, self.y_offset)

        # pause the program for a short duration, try 0.5 and 0.01 seconds
        time.sleep(0.25)

        # recursively search differnt directions adjacent to current row, col (up, down, left, right)
        # self.found_end(row, col)
        found = (
            self.search_from(row - 1, col)
            or self.search_from(row + 1, col)
            or self.search_from(row, col - 1)
            or self.search_from(row, col + 1)
        )

        # if any of the 4 directions returns True, mark the cel at row, col as part of the path and return True
        if found and self.grid[row][col] != "S":
            self.grid[row][col] = "P"
            return True

        # else, if the cell at row, col is not the start cell (S), mark it as a deadend
        elif self.grid[row][col] != "S":
            self.grid[row][col] = "D"

    def get_path_length(self):
        """ create a list of tuples representing the path
        and return path length"""

        path = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == "P":
                    path.append((row, col))

        print("path length:", len(path))


def background_music():
    """ plays tetris music in the background """

    playsound("Tetris.mp3")


def main():
    """ reads a maze file and sets the search parameters """
    maze = Maze(x_offset=-150, y_offset=200, tile_size=50, steps=0)

    # create a turtle and a window for drawing
    maze.make_window(bgcolor="slate gray")
    maze.make_turtle(shape="square", shape_width=2.5, shape_length=2.5)

    # read maze file and create playground grid
    maze.read_grid("maze3.txt")

    # find start position
    row, col = maze.find_start()

    # call the search function, it takes the grid, row, column, and steps
    maze.search_from(row, col)

    maze.get_path_length()

    # draw the final grid
    maze.draw_grid(maze.x_offset, maze.y_offset)

    # pause the grid drawing for 4 seconds
    time.sleep(4)

    # print the number of steps taken to find the path
    print("number of steps taken to reach answer:", maze.steps)


if __name__ == "__main__":
    p = Process(target=background_music, args=())
    p.start()
    main()
    p.terminate()
