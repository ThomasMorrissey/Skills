
#Climb Skill

import random

class Player(object):

    def __init__(self):
        self.mods = ["halfling", "lizardfamiliar", "Athletic"]

class climbskill(object):
    
    def __init__(self,dc):
        self.dc=dc

    def skillcheck(self):
        result = ""
        diceroll = random.randint(1, 41)
        player = Player()

        if "halfling" in player.mods:
            print("You recieved a +2 racial bonus on climb checks.")
            diceroll = diceroll + 2
        
        if "lizardfamiliar" in player.mods:
            print("You recieved a +3  bonus on climb checks.")
            diceroll = diceroll + 3

        if "Athletic" in player.mods:
            print("You recieved a +2 bonus on climb checks.")
            diceroll = diceroll + 2
    

        if self.dc > diceroll:
            print("Failure")
        else:
            print("Success")
        return result

    def climb(self):
        result=self.skillcheck()
        if result == "Success":
            print("You have successfully used climb")
        else:
            print("You were not able to use climb")

    

