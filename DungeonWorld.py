#Dungeon test 1

import random


class dunWorld(object):
    def __init__(self, currentLocation):
        dungeonFile = open("dungeon1", "r")
        self.currentLocation = currentLocation
        self.dungeon = [dungeonLocation() for i in range(36)]
        for i in range(len(self.dungeon)):
            form = dungeonFile.readline()
            form = form.strip()
            form = form.split(',')
            self.dungeon[i].dungeonForm = form
            if self.dungeon[i].dungeonForm.count('1') == 1:
                self.dungeon[i].room = True
            try:
                if self.dungeon[i].dungeonForm[4]: #Check if square is final square
                    self.dungeon[i].final = True
            except IndexError:
                pass
    def possibleMoves(self, currentLocation):
        string = "You can move:\n"
        if self.dungeon[currentLocation].dungeonForm[0] == '1':
            string += "\t- North \n"
        if self.dungeon[currentLocation].dungeonForm[1] == '1':
            string += "\t- East \n"
        if self.dungeon[currentLocation].dungeonForm[2] == '1':
            string += "\t- South \n"
        if self.dungeon[currentLocation].dungeonForm[3] == '1':
            string += "\t- West \n"
        return string    
                
    def MovePlayerN(self, currentLocation): # Move player (N)orth
        if self.dungeon[currentLocation].dungeonForm[0] == '1':# Check to move up
            return currentLocation - 6
        else:
            return currentLocation
        
    def MovePlayerE(self, currentLocation):
        if self.dungeon[currentLocation].dungeonForm[1] == '1': # This is the check to see if you can move right.
            return currentLocation + 1
        else:
            return currentLocation
        
    def MovePlayerS(self, currentLocation): 
        if self.dungeon[currentLocation].dungeonForm[2] == '1': # Check to move south
            return currentLocation + 6
        else:
            return currentLocation
        
    def MovePlayerW(self, currentLocation): # Check to move west
        if self.dungeon[currentLocation].dungeonForm[3] == '1':
            return currentLocation - 1
        else:
            return currentLocation
        
class dungeonLocation(object):
    dungeonForm = []
    room = None #Defines if a square is a room
                #For example: [N, E, S, W] = [0,0,1,0] means the only exit is south, making it a room.
    final = False
            
#Main
def launchDungeon():
    print('You are in an eerie dungeon...')
    currentLocation = 0
    dungeonWorld = dunWorld(currentLocation)
    ################# Simple UI ##################
    inDungeon = True
    moveWhere = None
    while inDungeon == True:
        if moveWhere == 'n':
            currentLocation = dungeonWorld.MovePlayerN(currentLocation)
        elif moveWhere == 'e':
            currentLocation = dungeonWorld.MovePlayerE(currentLocation)
        elif moveWhere == 's':
            currentLocation = dungeonWorld.MovePlayerS(currentLocation)
        elif moveWhere == 'w':
            currentLocation = dungeonWorld.MovePlayerW(currentLocation)
        #elif moveWhere == 'q': Un-comment this to add a quit function that'll take you out of the dungeon
            #print('Goodbye')   and straight back where you were in the world
            #inDungeon = False
            #break
        elif moveWhere == None:
            pass
        else:
            print('Unknown Command')
        #print('You are on sqaure', currentLocation)
        if dungeonWorld.dungeon[currentLocation].final == True:
            print('You are in the exit square!')
            decide = input('Would you like to leave the dungeon:')
            if decide == 'y':
                currentLocation = random.randrange(35)
                inDungeon = False
                return currentLocation
        print(dungeonWorld.possibleMoves(currentLocation))
        moveWhere = input('Where would you like to move: ')


