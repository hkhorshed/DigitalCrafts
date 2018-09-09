#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self , health , power):
        self.health = health
        self.power = power

    def alive():
        print("You have {} health and {} power.".format(self.health, self.power))
    
    def attack(enemy):
        enemy.health -= self.power
        print("The {} does {} damage to you.".format(enemy , self.power))
        if self.health <= 0:
            print("You are dead.")

    
  

class Hero(Character):
    def __init__(self):
        super().__init__(health , power)

class Goblin(Character):
    def __init__(self):
        super().__init__(health , power)


def main():
    Character(self.health) = 10
    Character(self.power) = 5
    Character(enemy.health) = 6
    Character(enemy.power) = 2

    while goblin.alive() and hero.alive():
        print(Hero.alive())
        print(Goblin.alive())
        print(Hero.print_status())
       
        print("What do you want to do?")
        print("1. fight {}".format(enemy))
        print("2. do nothing")
        print("3. flee")

        raw_input = input()
        if raw_input == "1":
            enemy.health -= self.power

        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))



main()