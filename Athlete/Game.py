import random
from Team import Team
from Sport import Sport
from Athlete import Athlete

class Game:
    '''
    Represent a game between two teams in a specific sport. It has two teams and a score
    '''
    def __init__(self, A: Team, B: Team):
        '''
        Custom constructor for the Game class
        '''
        self.team_A = A
        self.team_B = B
        self.score = {self.team_A.name: 0, self.team_B.name: 0}
        self.winner = None
        self.loser = None

    def play(self):
        '''
        Simulate the game between the two teams
        '''
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        self.score[self.team_A.name] = a
        self.score[self.team_B.name] = b
        if a > b:
            self.winner = self.team_A.name
            self.loser = self.team_B.name
        elif b > a:
            self.winner = self.team_B.name
            self.loser = self.team_A.name
        else:
            self.winner = "Draw"
            self.loser = "Draw"

    def __str__(self):
        '''
        Return a string representation of the game
        '''
        return f"{self.team_A.name:<20}: {self.score[self.team_A.name]}\n{self.team_B.name:<20}: {self.score[self.team_B.name]}"

    def display(self):
        '''
        Display the game results
        '''
        print(f"|{self.team_A.name:<10}|{self.score[self.team_A.name]:>3}|{self.team_B.name:<10}|{self.score[self.team_B.name]:>3}| Winner:{self.winner}|")

if __name__ == "__main__":
    a = Athlete("John", 25, "Baseball")
    b = Athlete("Jane", 22, "Baseball")
    c = Athlete("Mike", 28, "Baseball")
    d = Athlete("Sara", 24, "Baseball")
    e = Athlete("Tom", 26, "Baseball")
    f = Athlete("Lily", 23, "Baseball")

    team1 = Team("Dodgers", Sport("Baseball", 9, "MLB"))
    team2 = Team("RedSox", Sport("Baseball", 9, "MLB"))

    team1.add_athlete(a)
    team1.add_athlete(b)
    team1.add_athlete(c)
    team2.add_athlete(d)
    team2.add_athlete(e)
    team2.add_athlete(f)

    game = Game(team1, team2)
    game.play()
    game.display()
