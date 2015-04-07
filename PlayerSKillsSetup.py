import Appraisal
import OpenLock
import Search
import Swim
import ClimbSkill
import World2
import random
class player(object):
    def __init__(self,name):
        self.name=name
        self.status=""
        self.cash=100
    def appriaise(self):
        Skill=Appraisal.Appraise()
        Skill.Skill_Check()
    def OpenLock(self):
        if self.status == "Infront of Door":
            OpenLock.OpenLock()
    def Search(self):
        Search.hidden_item()
        Search.skill()
    def Climb(self):
        #if :
        dc=random.randrange(1,41)
        ClimbSkill.WeGotTheseSkillz=climbskill(dc)
        ClimbSKill.WeGotTheseSkillz.climb()
    def Swim(self):
            Dc=0
            waterConditions=["calm","rough","stormy"]
            water=waterConditions[random.randrange(0,3)]
            Swim.Swim_Dcs(water, Dc)
            Swim.SkillCheck(Dc)
            return Swim.SkillCheck(Dc)

player = player("Billy bob")
currentLocation = 0
world = World2.World(currentLocation)
world.createDungeon()
############# Simple UI ##############

print(world.getSurroundings(currentLocation))
moveWhere = input('Where would you like to move: ')
while moveWhere != 'q':
    tempLocation = currentLocation
    if moveWhere == 'n':
        currentLocation = world.movePlayerN(currentLocation)
    elif moveWhere == 'e':
        currentLocation = world.movePlayerE(currentLocation)
    elif moveWhere == 's':
        currentLocation = world.movePlayerS(currentLocation)
    elif moveWhere == 'w':
        currentLocation = world.movePlayerW(currentLocation)
    elif moveWhere == 'l':
        print(str(world.printLocation(currentLocation)))
    elif moveWhere == 'b':
        print(world.getPositionBiome(currentLocation))
    elif moveWhere == 'q':
        print('Goodbye')
        break
    else:
        print('Unknown Command')
    if world.map[currentLocation].BIOME == 9:
        decide = input('A dungeon appears before you! Would you like to enter it:')
        if decide == 'y':
            currentLocation = DungeonWorld.launchDungeon()
    if world.map[currentLocation].BIOME == 2:
        player.Swim()
        if Swim.SkillCheck == "Failure":
            currentLocation = tempLocation
    print(world.getSurroundings(currentLocation))
    moveWhere = input('Where would you like to move: ')
