import datetime
class  cricketplayer():
    def __init__(self, fname,lname,b_year,team):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = b_year
        self.team = team
        self.scores =[]
    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year
    def add_score(self,score):
        self.scores.append(score)
    def get_avg(self):
        return sum(self.scores)/len(self.scores)
    def __lt__(self, other):
        my_score = self.get_avg()
        other_score = other.get_avg()
        return my_score < other_score
    def __str__(self):
        return f'{self.first_name},{self.last_name},a player from {self.team}'

virat = cricketplayer('virat','Kohli',1988,'India')
virat.add_score(80)
virat.add_score(100)
virat.add_score(76)

David = cricketplayer('david','warner',1988,'Australia')
David.add_score(100)
David.add_score(76)
David.add_score(82)

print(virat.get_avg())
print(David.get_avg())
print(virat < David)
print(virat.__str__())


