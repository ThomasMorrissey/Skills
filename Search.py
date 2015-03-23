# Search skill - Player searches an area and has a chance to find possible items.
# Waiting for world team to add items to test. (incomplete)

class hidden_item(object):
    def __init__(self):
        self.name = "goblet"
        self.DC = 10

class player(object):
    def race(self):
        if playerRace == "Elf":
            searchnumber = searchnumber + 2
        if playerRace == "Half-Elf":
            searchnumber = searchnumber + 1



class skill(object):

    def search(self,item):
        searchnumber = 15
        if searchnumber >= item.DC:
            print("You found a",item.name + "!")
        else:
            print("You found nothing.")




it = hidden_item()
skills = skill()

skills.search(it)

def main():
    hidden_item()
    player()
    skill()
main()
