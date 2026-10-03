#!/usr/bin/env python3

#beta 3

import random as rand
import time

def endgame():
	print("your stats: \n"+pcow.name+"\n"+pcow.gender+"\n"+str(pcow.age)+"\n"+pcow.mate)

mrec = ["the farmer looked at you", "nothing happened", "other cows mooed"]
locs = ["barn", "lake"]
npcnams = ["amooba", "moory", "moonathon", "super cow"]
npcgenders = ["male", "female", "nb"]
anpcs = []
npcres = ["moo", "moo moo", "MOO"]
onof = [0, 1]

class cow:
	def __init__(self, name, gender, hunger, loc, age, mate):
		self.name = name
		self.gender = gender
		self.hunger = hunger
		self.loc = loc
		self.age = age
		self.mate = mate
	
	def moo(self):
		print(self.name + " said moo")
		print(rand.choice(mrec))

class npcow:
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender

pcownam = input("input your name:	")
pcowgen = input("input your gender:	")
pcowhun = 100.0
pcowloc = "barn"
pcowage = 0
pcowmat = ""

n1n = rand.choice(npcnams)
n1g = rand.choice(npcgenders)
npc1 = npcow(n1n, n1g)
anpcs.append(npc1.name)

n2n = rand.choice(npcnams)
n2g = rand.choice(npcgenders)
npc2 = npcow(n2n, n2g)
anpcs.append(npc2.name)

n3n = rand.choice(npcnams)
n3g = rand.choice(npcgenders)
npc3 = npcow(n3n, n3g)
anpcs.append(npc3.name)

pcow = cow(pcownam, pcowgen, pcowhun, pcowloc, pcowage, pcowmat)

while True:
	act = input(">_	")
	pcow.hunger = pcow.hunger - 1
	if pcow.hunger == 0:
		print("you died of hunger")
		endgame()
		break
	pcow.age = pcow.age + 1
	if act == "char":
		print(pcow.name + "\n" + pcow.gender + "\n" + pcow.loc + "\n" +  str(int(pcow.hunger)) + "\n" + str(pcow.age) +"\n"+ pcow.mate)
	elif act == "eat":
		pcow.hunger = 100.0
	elif act == "moo":
		cow.moo(pcow)
	elif act == "quit":
		qu = input("are you sure? you will lose all of your progress. [N/y]")
		if qu == "Y" or qu == "yes" or qu == "Yes" or qu == "y":
			break
		else:
			print()
	elif act == "move":
		newloc = input("where to go?")
		if newloc in locs:
			pcow.loc = newloc
		else:
			print("invalid location")
	elif act == "herd":
		print(npc1.name + "\n" + npc1.gender + "\n" +  npc2.name + "\n" + npc2.gender + "\n" + npc3.name + "\n" + npc3.gender + "\n")
	elif act == "talk":
		tak = input("to who?")
		if tak in anpcs:
			print("you talked to " + tak)
			print(tak + " said " + rand.choice(npcres))
		else:
			print(tak + " is not a memeber of you herd")
	elif act == "mate":
		if pcow.mate != "":		
			print("you are already mated!")
		else:
			if pcow.age > 18:
				mte = input("who would you like to mate?")
				if mte in anpcs:
					mc = rand.choice(onof)
					if mc == 0:
						print(mte + " said no :(")
					else:	
						print(mte + " said yes :)")
						pcow.mate = mte
			else:
				print("you are too young!")
	elif act == "!cheats":
		cheat = input("?")
		if cheat == "set age":
			pcow.age = int(input("?"))
		elif cheat == "set hun":
			pcow.hunger = int(input("?"))
		elif cheat == "kill":
			endgame()	
			break
