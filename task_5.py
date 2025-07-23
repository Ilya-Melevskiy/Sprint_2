class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses
    
class Football(Results):

    def football_number_of_wins(self):
        return f"Футбольных побед: {self.victories}"

    def football_number_of_draws(self):
        return f"Футбольных ничьих: {self.draws}"
    
    def football_number_of_losses(self):
        return f"Футбольных поражений: {self.losses}" 
    
    def football_total_points(self):
        return f"Общее количество очков: {3 * self.victories + self.draws}"
    
class Hockey(Results):
    
    def hockey_number_of_wins(self):
        return f"Хоккейных побед: {self.victories}"

    def hockey_number_of_draws(self):
        return f"Хоккейных ничьих: {self.draws}"
    
    def hockey_number_of_losses(self):
        return f"Хоккейных поражений: {self.losses}" 
    
    def hockey_total_points(self):
        return f"Общее количество очков: {2 * self.victories + self.draws}"

football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)
for team in (football_team, hockey_team):
    if team is football_team:
        print(team.football_number_of_wins())
        print(team.football_number_of_draws())
        print(team.football_number_of_losses())
        print(team.football_total_points())
    else:
        print(team.hockey_number_of_wins())
        print(team.hockey_number_of_draws())
        print(team.hockey_number_of_losses())
        print(team.hockey_total_points())