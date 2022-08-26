import datetime

# Player is a parent class

class Player:

    def __init__(self,fname,lname,birthyear):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birthyear

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

# create a child class

class CricketPlayer(Player):

    def __init__(self,fname,lname,birthyear,team):
        Player.__init__(self,fname,lname,birthyear) # calling parent class properties
        self.team = team
        self.scores = []

    def add_score(self,score):
        self.scores.append(score)

    def avg_score(self):
        return sum(self.scores)/len(self.scores)


class TennisPalyer(Player):
    def __init__(self,fname,lname,birthyear,winner):
        Player.__init__(self,fname,lname,birthyear)
        self.gslam = winner
        self.aces = []



virat = CricketPlayer('virat','kohli',1988,'India')
virat.add_score(80)
virat.add_score(100)

roger = TennisPalyer('Roger','federer',1978,20)

print(virat.get_age())
print("Virat age is:",virat.avg_score())
print("roger age is:",roger.get_age())

# BMW class

class BMW:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car ...")

    def stop(self):
        print("Stopping the car ...")

    def drive(self):
        pass


class ThreeClass(BMW):
    def __init__(self, CuriseAssistEnabled, name, model, year):
        BMW.__init__(self, name, model, year)
        self.CuriseAssistEnabled = CuriseAssistEnabled

    def display(self):
        print(self.CuriseAssistEnabled)

    def drive(self):
        print("Three Class is being driven..")


threeClass = ThreeClass(True, "BMW", "328i", 2018)
print(
    threeClass.CuriseAssistEnabled,
    threeClass.name,
    threeClass.model,
    threeClass.year
)

threeClass.start()
threeClass.drive()
threeClass.stop()

    
