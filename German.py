import random
import os

# prints the test files which are available
options = os.listdir("German Vocab/")
print('+++ available files +++')
for i in range(len(options)):
	print(f'[{i}] {options[i]}')
print('+++++++++++++++++++++++')

while True:
	name = str(input("Either return the file name or the number to the left of the file you would like to open: "))

	# checks if the inputed value is a number (corresponding to a specific file) or not (a manually types specific file)
	if name.isnumeric():

		if int(name) >= len(options):
			print('OOPS! INVALID FILE')
			continue

		file = "German Vocab/*" + options[int(name)]
		file = file.replace("*", "")
		break

	else:

		mistakeCount = 0
		for i in options:
			if i != name:
				mistakeCount += 1
		if mistakeCount >= 1:
			print('OOPS! INVALID FILE')
			continue

		file = "German Vocab/*" + name
		file = file.replace("*", "")
		break
print(f'Opening {file}...')

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
