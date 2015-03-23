import random
class Player(object):
    def __init__(self):
        self.Mods=["Nimble Fingers", "Thieves' tools", "Master Thieves' Tools"]
def Skillcheck(Dc):
    Result=""
    player=Player()
    YourRoll=random.randrange(1,41)
    print("Your Roll:",YourRoll)
    if "Nimble Fingers" in player.Mods:
        YourRoll += 2
    print("Your Roll:",YourRoll)
    if "Thieves' tools" not in player.Mods:
        YourRoll -= 2
    print("Your Roll:",YourRoll)
    if "Master Thieves' Tools" in player.Mods:
        YourRoll += 2
    print("Your Roll:",YourRoll)
    if Dc > YourRoll:
        Result = "Failure"
    else:
        Result = "Success"
    return Result
def OpenLock():
    Dc=random.randrange(20,40)
    Result=Skillcheck(Dc)
    if Result == "Failure":
        print("The Lock can not be opened.")
    else:
        print("The lock has been open.")
def main():
    OpenLock()
main()
