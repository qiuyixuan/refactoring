'''
CS321 Project 4
Yixuan Qiu
Connect 4 - Refactored
11/13/2021
'''

import turtle

class Connect4:

    window = None
    grid = []
    turt = None
    x_offset = 0
    y_offset = 0
    tile_size = 1

    def __init__(self, x_offset, y_offset, tile_size, turn):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.tile_size = tile_size
        self.turn = turn

    def make_window(self, window_title, bgcolor, width, height):
        ''' this function creates a screen object and returns it '''

        self.window = turtle.getscreen() # Set the window size
        self.window.title(window_title)
        self.window.bgcolor(bgcolor)
        self.window.setup(width, height)
        self.window.tracer(0) #turns off screen updates for the window Speeds up the game
        return self.window


    def make_turtle(self, shape, color, stretch_width, stretch_length, x_pos, y_pos):
        ''' creates a turtle and sets initial position '''

        self.turt = turtle.Turtle()
        self.turt.speed(0)    # Speed of animation, 0 is max
        self.turt.shape(shape)
        self.turt.color(color)
        self.turt.shapesize(stretch_width, stretch_length) 
        self.turt.penup()
        self.turt.goto(x_pos, y_pos) # Start position
        return self.turt

    def teleport(self, x_pos, y_pos):
        self.turt.up()
        self.turt.goto(x_pos, y_pos)
        self.turt.down()

    def draw_grid(self, x_pos, y_pos):
        ''' draws a grid at x, y with a specific tile_size '''

        self.teleport(x_pos, y_pos)

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):

                self.teleport(x_pos + col * self.tile_size, y_pos -row * self.tile_size)

                if self.grid[row][col] == 1:
                    self.turt.dot(self.tile_size-5, "red")
                
                elif self.grid[row][col] == 2:
                    self.turt.dot(self.tile_size-5, "yellow")
                
                else:
                    self.turt.dot(self.tile_size-5, "white")

    def check_win(self, grid, player):
        ''' checks the winner in the grid
        returns true if player won
        returns false if player lost
        '''

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
                    if self.grid[row][col] == 1\
                    and self.grid[row+1][col+1] == 1\
                    and self.grid[row+2][col+2] == 1\
                    and self.grid[row+3][col+3] == 1:
                        return True

    def play(self, x_pos, y_pos):
        ''' '''
        # global turn
        row = int(abs((y_pos - self.y_offset - 25) // (50) + 1))
        col = int(abs((x_pos - self.x_offset - 25) // (50) + 1))
        print(row, col)
        self.grid[row][col] = self.turn
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


def main():
    ''' the main function where the game events take place '''

    game = Connect4(x_offset=-150, y_offset=200, tile_size=50, turn=1)

    game.window = game.make_window("Connect 4", "light sky blue", 800, 600)

    for row in range(5):
        game.grid.append([0]*7)

    game.turt = game.make_turtle('classic', "white", 1, 1, 0, 0 )
    
    game.draw_grid(game.x_offset, game.y_offset)

    while True:

        game.window.onscreenclick(game.play)
        game.window.listen()

        # grid[1][0] = 1
        # grid[2][1] = 1
        # grid[3][2] = 1
        # grid[4][3] = 1

        selected_row = int(input("enter row, player "+ str(game.turn) +": "))
        selected_col = int(input("enter col, player "+ str(game.turn) +": "))

        if game.grid[selected_row][selected_col] == 0:

            if game.turn == 1:
                game.grid[selected_row][selected_col] = 1
            else:
                game.grid[selected_row][selected_col] = 2

        game.draw_grid(-150, 200)
        game.window.update()

        if game.check_win(game.grid, 1):
            print("player 1 won")

        elif game.check_win(game.grid, 2):
            print("player 2 won")

        if game.turn == 1:
            game.turn = 2
        else:
            game.turn = 1


    # window.exitonclick()

if __name__ == "__main__":
	main()

