class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    # use the @ symbol and cls in argument. it is similar to using self
    @classmethod
    def get_team_name(cls):
        return cls.teamName

    # a static method does not use reference to the object or class.
    @staticmethod
    def demo():
        print("I am a static method.")


print(Player.get_team_name())
p1 = Player('lol')
p1.demo()
Player.demo()
