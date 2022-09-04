from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 230)
        self.color('white')
        self.update_score()

    def update_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def add_new_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALIGNMENT, font=('Courier', 20, 'bold'))
