#Random Character Generator
#Defining sets of character traits and character races
CharacterTraits = ["Sassy ","Bored ","Fabulous ","Fat ","Sweet ","Isosceles ","Swagulous ","Hot ","Angry ","Gently confused "]
CharacterRace = ["Elf","Witch","Ork","Dwarf","Tiefling","Aasimar","Tabaxi","Minotaur","Furball","Furbolg"]
OhNo = ["Oh dear.","How unfortunate.","That's unfortunate.","How Sad.","Hmm...","Oh no!","Oh no.","Oh dear!"]
Names = ["Adair","Bellamy","Cyprian","Devereaux","Emlyn","Fifer","Gaiwan","Hyeon","Irie","Jayden","Kaelin","Landen","Myles","Nox","Ori","Payton","Quinn","Remi","Sawyer","Tyree","Uri","Vian","Wynn","Xola","Yancy","Zaire"]

#Random number for selecting random traits
import random
x = random.randint(0,len(CharacterTraits))
y = random.randint(0,len(CharacterRace))
z = random.randint(0,len(OhNo))
a = random.randint(0,len(Names))

#Starting the game by assigning the player a trait and race
Answer = input("Hello, Player. Are you ready to see you're new self? ").lower()
if Answer == "yes":
    print(CharacterTraits[x] + CharacterRace[y])
    
    ans = input("Are you happy with your result? ").lower()

    if ans == "yes":
        print("Well I'm not. You are now an Awkward Adolescent.")
        name = input("What is your name, awkward adolescent? ")    
        PlayerName = Names[a]
        print("I don't really like that name, either. How about I call you " + PlayerName + " instead?")
        print(" ")
        print("Hello, " + PlayerName + ", the Awkward Adolescent, and welcome to my game! I hope you had fun~!")
            
    elif ans == "no":
        print(OhNo[z] + " I don't think I can help you anymore. Why don't you come back when you're ready to cooperate?")
        
    else:
        print("If you can't be bothered to follow my prompts, then I can't be bothered to play with you!")

elif Answer == "no":
    print(OhNo[z] + " Maybe next time, then!")

else:
    print("Please enter yes or no!")