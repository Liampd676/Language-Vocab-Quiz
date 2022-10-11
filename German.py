import random

name = str(input("what file do you want to open? ")).capitalize()
file = "German Vocab/*" + name
file = file.replace("*", "")

with open(file, "r") as f:
    german = [line.split("-", 1)[0] for line in f]
with open(file, "r") as f:
    english = [line.split("-", -1)[1] for line in f]

total = len(english)
score = 0

mode = int(input("German to English(1)\nEnglish to German(2)\n"))

if mode == 2:
	while len(english) > 0:
		word = random.choice(english)
		answer = str(input("\nWhat is "+word[1:-1]+" in German:\n"))
		if answer.replace(" ", "") == german[english.index(word)].replace(" ", ""):
			score = score + 1
			print("Correct, "+str(score)+"/"+str(total))
			german.remove(german[english.index(word)])
			english.remove(word)
		else:
			print("\nIncorrect. "+str(score)+"/"+str(total)+" The correct spelling of "+word[1:-1]+" is: \n"+german[english.index(word)]+"\nYour answer was: \n"+answer)

if mode == 1:
	while len(german) > 0:
		gword = random.choice(german)
		word = english[german.index(gword)]
		eword = word[1:-1]
		answer = str(input("\nWhat is "+gword[0:-1]+" in English:\n"))
		print(eword.replace(" ", "x"))
		print(answer.replace(" ", "x"))
		if answer.replace(" ", "") == eword.replace(" ", ""):
			score = score + 1
			print("Correct, "+str(score)+"/"+str(total))
			english.remove(word)
			german.remove(gword)
		else:
			print("\nIncorrect. "+str(score)+"/"+str(total)+" The correct spelling of "+gword[0:-1]+" is: \n"+eword+"\nYour answer was: \n"+answer)
