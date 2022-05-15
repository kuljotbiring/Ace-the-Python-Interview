class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    # use the @ symbol and cls in argument. it is similar to using self
    @classmethod
    def get_team_name(cls):
        return cls.teamName


print(Player.get_team_name())
