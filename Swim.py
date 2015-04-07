import random
class item(object):
    def __init__(self):
        self.value = 150.00
def Swim_Dcs(water, Dc):
    if water == "calm":
        print("The water is calm and easy to cross.")
        Dc=10
    elif water == "rough":
        print("The water is a bit rough but can still be crossed.\n")
        Dc=15
    else:
        print("The water is stormy, I wish you luck.")
        Dc=20
    return Dc
def SkillCheck(Dc):
    Verdict=""
    Roll = random.randint(1,41)
    if Roll >= Dc:
        Verdict = "Half-Speed"
    elif Roll >= Dc-4 and Roll < Dc:
        Verdict = "Quarter-Speed"
    else:
        Verdict ="Failure"
    return Verdict
#Swim Class
class Swim(object):
    def __init__(self):
        self.name="Swim"
        self.Dc=10
    def Skill_Check(self):
        Player=player()
        Verdict=SkillCheck(self.Dc)
        
class swim_speed(object):
    def __init__(self):
        playerspeed=1
        self.half_speed = playerspeed/2
        self.quarter_speed = playerspeed/4
        self.failure=playerspeed*0


