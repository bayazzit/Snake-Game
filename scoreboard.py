from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt') as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 185)
        self.color('white')
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def add_new_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as file:
                file.write(f'{self.high_score}')
        self.update_score()
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALIGNMENT, font=('Courier', 20, 'bold'))
