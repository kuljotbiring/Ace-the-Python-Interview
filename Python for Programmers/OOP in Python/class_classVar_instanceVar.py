class Player:

    # class variable
    teamName = "Liverpool"

    def __init__(self, name):
        # instance variables
        self.name = name
        self.formerTeams = []


p1 = Player("Mark")
p1.formerTeams.append("Barcelona")

p2 = Player("Steve")
p2.formerTeams.append("Madrid")
p2.formerTeams.append("Argentina")

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print(p1.formerTeams)
print("Name:", p2.name)
print("Team Name:", p2.teamName)
print(p2.formerTeams)
