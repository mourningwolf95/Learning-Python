#Random Character Generator
#Defining sets of character traits and character races
CharacterTraits = ["Sassy ","Bored ","Fabulous ","Fat ","Sweet ","Isosceles ","Swagulous ","Hot ","Angry ","Gently confused "]
CharacterRace = ["Elf","Witch","Ork","Dwarf","Tiefling","Aasimar","Tabaxi","Minotaur","Furball","Furbolg"]

#Random number for selecting random traits
import random
x = random.randint(-12,12)

#Starting the game with a yes/no question
Answer = input("Hello, Player. Are you ready to see you're new self? ")
if Answer == "yes":
    print(CharacterTraits[x] + CharacterRace[x])

elif Answer == "no":
    print("I'm sorry to hear that. Maybe next time, then!")

else:
    print('"yes" or "no" only, please.')
