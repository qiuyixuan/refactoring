"""
CS321 Project 4
Xiangxi Mu and Yixuan Qiu
Class Based Pong - Refactored
11/13/2021
"""

import turtle


class Paddle:
    # implements a Pong game paddle

    def __init__(self, x_position, y_position):
        """ initializes a paddle with a position """

        self.distance = 20
        self.x_position = x_position
        self.y_position = y_position
        self.turt = make_turtle(
            "square", "white", 5, 1, self.x_position, self.y_position
        )

    def up(self):
        y = self.turt.ycor() + self.distance
        self.turt.sety(y)
        self.y_position = y

    def down(self):
        y = self.turt.ycor() - self.distance
        self.turt.sety(y)
        self.y_position = y

    def xcor(self):
        """ returns turtle x_cord """
        return self.turt.xcor()

    def ycor(self):
        """ returns turtle y_cord """
        return self.turt.ycor()


class Ball:
    # implements a Pong game ball

    def __init__(self):
        """ intializes a ball with default direction and position """

        self.turt = make_turtle("square", "white", 1, 1, 0, 0)
        self.ball_d = {"dx": 0.0925, "dy": 0.0925}
        self.ball_dx_initial = 0.0925
        self.border = 290
        self.x_position = 0
        self.y_position = 0

    def move(self):
        x_cor = self.turt.xcor() + self.ball_d["dx"]
        y_cor = self.turt.ycor() + self.ball_d["dy"]
        self.goto(x_cor, y_cor)

        self.ifBorder()

    def ifBorder(self):
        if self.turt.ycor() > self.border:
            self.turt.sety(self.border)
            self.ball_d["dy"] *= -1

        elif self.turt.ycor() < -self.border:
            self.turt.sety(-self.border)
            self.ball_d["dy"] *= -1

    def xcor(self):
        """ returns turtle x_cord """
        return self.turt.xcor()

    def ycor(self):
        """ returns turtle y_cord """
        return self.turt.ycor()

    def goto(self, x_pos, y_pos):
        """ moves ball to new x, y positions """
        self.turt.goto(x_pos, y_pos)
        self.x_position = x_pos
        self.y_position = y_pos


class Game:
    def __init__(self, width, height, x_pos_paddle, y_pos_paddle):
        self.window = make_window(
            "Pong - A CS151 Reproduction!", "black", width, height
        )

        # Score
        self.score_player1 = 0
        self.score_player2 = 0

        # Paddels
        self.paddle_1 = Paddle(-x_pos_paddle, y_pos_paddle)
        self.paddle_2 = Paddle(x_pos_paddle, y_pos_paddle)

        # Balls
        self.ball = Ball()

        # Pen
        self.pen = make_turtle("square", "white", 1, 1, 0, 260)
        self.pen.write(
            "Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal")
        )
        self.pen.hideturtle()

        # Keyboard bindings

        self.window.listen()  # Listen for keyboard input
        self.window.onkeypress(
            self.paddle_1.up, "w"
        )  # when you press w run paddle_a_up
        self.window.onkeypress(self.paddle_1.down, "s")
        self.window.onkeypress(self.paddle_2.up, "Up")
        self.window.onkeypress(self.paddle_2.down, "Down")

        # Paddle x position
        self.border = x_pos_paddle

    def game_loop(self):
        self.window.update()
        self.ball.move()
        # Border checking
        # Left and right

        if self.ball.xcor() > self.border:
            self.score_player1 += 1
            self.player_win()
        elif self.ball.xcor() < -self.border:
            self.score_player2 += 1
            self.player_win()

        # Paddle and ball collisions
        if (
            self.ball.xcor() < -(self.border - 10)
            and self.ball.xcor() > -self.border
            and self.ball.ycor() < self.paddle_1.ycor() + 50
            and self.ball.ycor() > self.paddle_1.ycor() - 50
        ):
            self.collision(-(self.border - 10))
        elif (
            self.ball.xcor() > self.border - 10
            and self.ball.xcor() < self.border
            and self.ball.ycor() < self.paddle_2.ycor() + 50
            and self.ball.ycor() > self.paddle_2.ycor() - 50
        ):
            self.collision(self.border - 10)

    def player_win(self):
        self.pen.clear()
        self.pen.write(
            "Player A: "
            + str(self.score_player1)
            + "  Player B: "
            + str(self.score_player2),
            align="center",
            font=("Courier", 24, "normal"),
        )
        self.ball.goto(0, 0)
        self.ball.ball_dx_initial *= -1
        self.ball.ball_d["dx"] = self.ball.ball_dx_initial

    def collision(self, border):
        self.ball.goto(border, self.ball.ycor())
        self.ball.ball_d["dx"] *= -1.5
        self.ball.ball_dx_initial *= -1


def make_window(window_title, bgcolor, width, height):
    """this function creates a screen object and returns it"""

    window = turtle.getscreen()  # Set the window size
    window.title(window_title)
    window.bgcolor(bgcolor)
    window.setup(width, height)
    window.tracer(0)  # turns off screen updates for the window Speeds up the game
    return window


def make_turtle(shape, color, stretch_width, stretch_length, x_pos, y_pos):
    """ creates a turtle and sets initial position """

    turt = turtle.Turtle()
    turt.speed(0)  # Speed of animation, 0 is max
    turt.shape(shape)  # square defualt is 20,20
    turt.color(color)
    turt.shapesize(stretch_width, stretch_length)
    turt.penup()
    turt.goto(x_pos, y_pos)  # Start position
    return turt


def main():
    """ the main function where the game events take place """

    my_game = Game(800, 600, 350, 0)
    while True:
        my_game.game_loop()


if __name__ == "__main__":
    main()
