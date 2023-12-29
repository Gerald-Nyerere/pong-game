from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score = 0 
        self.r_score = 0
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.goto(-180,280)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(180,280)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
       

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
       
    def l_point(self):   
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):   
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
            