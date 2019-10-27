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

print("Now we need to get you a name.")
input("What is your name, bitch? ")
Key = open("Save.txt", "r")
print(Key.read())
Key.close()