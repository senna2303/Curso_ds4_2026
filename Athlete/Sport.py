class Sport:
    """ Sport class represents a sport in a thournament"""
    max_score = {
        "Soccer":20,
        "Baseball":50,
        "Football":70,
        "Basketball":150,
        "Voleyball":3,
        "Tennis":3
    }
    def __init__(self, sport_name:str, num_players:int, league:str):
        if sport_name in self.max_score:
            self.sport_name = sport_name
            self.num_players = num_players
            self.league = league
        else:
            raise ValueError(
                f"Sport name should be:{', '.join(self.max_score.keys())}"
            )
    def __str__(self):
        return f"{self.sport_name} with {self.num_players} in leage: {self.league}"

    def __repr__(self) -> str:
        return f"Sport(sport_name={self.sport_name},{self.num_players},{self.league})"

    def display(self):
        print(f"|{self.sport_name:^12} | {self.num_players:^4} | {self.league:^10}|")

if __name__ == "__main__":
    s = Sport('Soccer',11,'Liga MX')
    b = Sport('Baseball',9,'MLB')
    print(b)
    print(s)
    s.display()
    b.display()    