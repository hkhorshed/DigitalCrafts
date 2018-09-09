#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Hero:
    def __init__(self, hero_health , hero_power):
        self.power = hero_power
        self.health = hero_health
        print(self.power , self.health)

    def testDataTypes(self , goblin):
        print(goblin.power , goblin.health)

player_1 = Hero(10 , 5)
my_variable = 'Hussein'
myList = [1 , 2 , 3 , 4]
veronica = Goblin(4 , 5)


    def attack(enemy):
        self.goblin_health -= self.hero_power
        print("You do {} damage to the goblin.".format(self.hero_power))

class Hero:
    def __init__(self, goblihn_health , gooblin_power):
        self.power = goblin_power
        self.health = goblin_health
        print(self.power , self.health)

goblin_1 = Hero(10 , 5)
    
    def attack(enemy):
        self.hero_health -= self.goblin_power
        print("The goblin does {} damage to you.".format(self.goblin_power))
    
    

def main():
    hero_1 = Hero()
    goblin_1 = Goblin()


    while goblin_1.health > 0 and hero_1.health > 0:
        print("You have {} health and {} power.".format(hero_1.health, hero_1.power))
        print("The goblin has {} health and {} power.".format(goblin_1.health, goblin_1.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(enemy)
            if goblin_1.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin_1.health > 0:
            # Goblin attacks hero
            goblin_1.attack(enemy)
            if hero_1.health <= 0:
                print("You are dead.")

main()