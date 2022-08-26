import datetime

class CricketPlayer:
    def __init__(self,fname,lname,byear,team):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = byear
        self.scores = []
        self.team = team

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    def add_score(self,score):
        self.scores.append(score)

    def avg_score(self):
        return sum(self.scores)/len(self.scores)

    def __lt__(self,other):
        my_score = self.avg_score()
        other_score = self.avg_score()
        return my_score < other_score

    def __str__(self):
        return f'{self.first_name} the Indian team captain'




# creating object of class
# when we use any operator to compare two objects of class then it is called operator overloading

virat = CricketPlayer('virat','kohli',1988,'India')
virat.add_score(80)
virat.add_score(0)
virat.add_score(100)
virat.add_score(45)

david = CricketPlayer('david','warner',1986,'Australia')
david.add_score(60)
david.add_score(20)
david.add_score(102)
david.add_score(55)

print(virat < david)
print(virat)