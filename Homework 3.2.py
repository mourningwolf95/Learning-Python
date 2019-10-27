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
        "Firbolg":["Waestris","Carran","Yelceran","Magxina","Xyrmoira"],}


#Random numbers for selecting random traits
import random
x = random.randint(0,len(Ldic["Ctraits"]))
y = random.randint(0,len(Ldic["Craces"]))
z = random.randint(0,len(Ldic["OhNo"]))
UglySobbing = random.randint(0,5)

#The game itself. Open with the option to recall previously saved character data.
Answer = input("Hello, Player. Are you ready to see your new self? ").lower()
if Answer == "yes":
    PlayerC = Ldic["Ctraits"][x] + Ldic["Craces"][y]
    Key = Ldic["Craces"][y]
    print(PlayerC)
    
    ans = input("Are you happy with your result? ").lower()

    if ans == "yes":
        print("Now we need to get you a name.")
        input("What is your name, " + PlayerC + "? ")
        PlayerName = Ndic[Key][UglySobbing]
        print("I don't really like that name. How about I call you " + PlayerName + " instead?")
        print(" ")
        print("Hello, " + PlayerName + ", the " + PlayerC + ", and welcome to my game! I hope you had fun~!")
            
    elif ans == "no":
        print(Ldic["OhNo"][z] + " I don't think I can help you anymore. Why don't you come back when you're ready to cooperate?")
        
    else:
        print("If you can't be bothered to follow my prompts, then I can't be bothered to play with you!")

elif Answer == "no":
    print(Ldic["OhNo"][z] + " Maybe next time, then!")

else:
    print("Please enter yes or no!")