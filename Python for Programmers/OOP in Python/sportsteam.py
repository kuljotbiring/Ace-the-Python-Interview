"""
You have to implement 3 classes, School, Team, and Player, such that an instance of a School should contain instances of
Team objects. Similarly, a Team object can contain instances of Player class.

You have to implement a School class containing a list of Team objects and a Team class comprising a list of Player
objects.
Task 1#

    The Player class should have three properties that will be set using an initializer:
        ID
        name
        teamName

Task 2#

    The Team class will have two properties that will be set using an initializer:
        name
        players: a list with player class objects in it

    It will have two methods:

        addPlayer(), which will add new player objects in the players list

        getNumberOfPlayers(), which will return the total number of players in the players list

Task 3#

    The School class will contain two properties that will be set using an initializer:
        teams, a list of team class objects
        name

    It will have two methods:
        addTeam, which will add new team objects in the teams list
        getTotalPlayersInSchool(), which will count the total players in all of the teams in the School and return the
        count

So, your school should have these players in their respective teams:
Player ID’s 	Player Names 	Teams
1 	Harris 	Red
2 	Carol 	Red
1 	Johnny 	Blue
2 	Sarah 	Blue
"""


# Player class
class Player:
    def __init__(self, ID, name, teamName):
        self.ID = ID
        self.name = name
        self.teamName = teamName
    # Complete the implementation


# Team class contains a list of Player
# Objects
class Team:
    def __init__(self, name):
        self.players = []
        self.name = name

    # Complete the implementation
    def addPlayer(self, player):
        self.players.append(player)

    def getNumberOfPlayers(self):
        return len(self.players)

# School class contains a list of Team
# objects.
class School:
    def __init__(self, name):
        self.teams = []
        self.name = name

    def addTeam(self, team):
        self.teams.append(team)

    def getTotalPlayersInSchool(self):
        length = 0
        for n in self.teams:
            length = length + (n.getNumberOfPlayers())
        return length


# Complete the implementation
p1 = Player(1, "Harris", "Red")
p2 = Player(2, "Carol", "Red")
p3 = Player(1, "Johnny", "Blue")
p4 = Player(2, "Sarah", "Blue")

red_team = Team("Red Team")
red_team.addPlayer(p1)
red_team.addPlayer(p2)

blue_team = Team("Blue Team")
blue_team.addPlayer(p2)
blue_team.addPlayer(p3)

mySchool = School("My School")
mySchool.addTeam(red_team)
mySchool.addTeam(blue_team)