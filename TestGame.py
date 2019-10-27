#Random Character Generator
#Defining sets of character traits and character races
Ldic = {"Ctraits":["Sassy ","Bored ","Fabulous ","Fat ","Sweet ","Isosceles ","Swagulous ","Hot ","Angry ","Gently confused "],
        "Craces":["Elf","Witch","Ork","Dwarf","Tiefling","Aasimar","Tabaxi","Minotaur","Furball","Firbolg"],
        "OhNo":["Oh dear.","How unfortunate.","That's unfortunate.","How Sad.","Hmm...","Oh no!","Oh no.","Oh dear!"]}

Ndic = {"Elf":["Aeris","Cearil","Korn","Olrin","Seice"],
        "Witch":["Circe","Agnes","Beatrice","Norn","Rain"],
        "Ork":["Grum","Mugdruggeth","Kurgh","Gurng","Vrumgrudgery"],
        "Dwarf":["Oomloute","Pebblemuncher","Polepoach","Hehooregurts","Stonegulch"],
        "Tiefling":["Theriye","Drovian","Aasingove","Verosian","Malkaria"],
        "Aasimar":["Triulinan","Meealiman","Heaveintoe","Holden","Waesintol"],
        "Tabaxi":["Bartholemew","Kitkat","Tabbytha","Whispurr","Lucifurr"],
        "Minotaur":["Reovera","Noodor","Lannas","Duulno","Oennas"],
        "Furball":["Cotton","Woolryn","Yearin","Froofle","Poufe"],
        "Firbolg":["Waestris","Carran","Yelceran","Magxina","Xyrmoira"]}

#Random number for selecting random traits
import random
x = random.randint(0,len(Ldic["Ctraits"]))
y = random.randint(0,len(Ldic["Craces"]))
z = random.randint(0,len(Ldic["OhNo"]))
UglySobbing = random.randint(0,5)


def prompt(prompt):
    return input(prompt).lower()

def AgainPeasant():
    CT = Ldic["Ctraits"][random.randint(0,len(Ldic["Ctraits"]))]
    CR = Ldic["Craces"][random.randint(0,len(Ldic["Craces"]))]
    Again = CT + CR
    Save = open("Save.txt", "w")
    Save.write(CR)
    Save.close()
    return Again

def GameBegin():
    ans = prompt("Hello, Player. Are you ready to see your new self? ")
    if ans == "yes":
        PlayerC = Ldic["Ctraits"][x] + Ldic["Craces"][y]
        Key = Ldic["Craces"][y]
        Save = open("Save.txt", "w")
        Save.write(Key)
        Save.close()
        
        print(PlayerC)
        
        ans = prompt("Are you happy with your result? ")

        while ans == "no":
            PlayerC = AgainPeasant()
            ans = prompt("How does " + PlayerC + " sound to you, then? ")
                
        if ans == "yes":
            print("Now we need to get you a name.")
            prompt("What is your name, " + PlayerC + "? ")
            Save = open("Save.txt", "r")
            Key = Save.read()
            Save.close()
            PlayerName = Ndic[Key][UglySobbing]
            print("I don't really like that name. How about I call you " + PlayerName + " instead?")
            print(" ")
            print("Hello, " + PlayerName + ", the " + PlayerC + ", and welcome to my game! I hope you had fun~!")
            
        else:
            print("If you can't be bothered to follow my prompts, then I can't be bothered to play with you!")

    elif ans == "no":
        print(Ldic["OhNo"][z] + " Maybe next time, then!")

    else:
        print("Please enter yes or no!")
    return PlayerC

answer = GameBegin()