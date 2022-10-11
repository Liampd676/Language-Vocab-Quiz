import random

name = str(input("what file do you want to open? ")).capitalize()
file = r"C:\German Vocab\*"+name
file = file.replace("*", "")

with open(file, "r") as f:
    german = [line.split("-", 1)[0] for line in f]
with open(file, "r") as f:
    english = [line.split("-", -1)[1] for line in f]

total = len(english)
score = 0
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