#Random Character Generator
#Defining sets of character traits and character races
CharacterTraits = ["Sassy ","Bored ","Fabulous ","Fat ","Sweet ","Isosceles ","Swagulous ","Hot ","Angry ","Gently confused "]
CharacterRace = ["Elf","Witch","Ork","Dwarf","Tiefling","Aasimar","Tabaxi","Minotaur","Furball","Furbolg"]

#Random number for selecting random traits
import random
x = random.randint(0,len(CharacterTraits))
y = random.randint(0,len(CharacterRace))

#Starting the game with a yes/no questiony
Answer = input("Hello, Player. Are you ready to see you're new self? ")
if Answer == "yes":
    print(CharacterTraits[x] + CharacterRace[y])

elif Answer == "no":
    print("I'm sorry to hear that. Maybe next time, then!")

else:
    print('"yes" or "no" only, please.')
