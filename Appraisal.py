import random
class item(object):
    def __init__(self):
        self.value = 150.00
def SkillCheck(Dc):
    Verdict=""
    Roll = random.randint(1,41)
    if Roll > Dc:
        Verdict = "Success"
    else:
        Verdict = "Failure"
    return Verdict
class Appraise(object):
    def __init__(self):
        self.name="Appraise"
        self.Dc=12
    def Skill_Check(self):
        Player=player()
        Verdict=SkillCheck(self.Dc)
        Item=item()
        if Verdict == "Success":
            print(self.name,"was a success.")
            Player.money=Appraise.Success(Player.money,Item.value)
        else:
            print(self.name,"was a faliure.")
            Appraise.Failure(Player.money,Item.value)
    def Success(money,itemValue):
        money+=itemValue
        return money
    def Failure(money,itemValue):
        Value=random.randrange(2,13)
        Value=(Value+3)/100
        TrueValue=Value*itemValue
        money=money+TrueValue
        return money

class player(object):
    def __init__(self):
        self.money=100.00
def main():
    Player=player()
    Skill=Appraise()
    Skill.Skill_Check()
    print("YEAH, it works!")
main()
