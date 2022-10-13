import random
import os

# prints the test files which are available
options = os.listdir("German Vocab/")
optionsGUI = options


if len(optionsGUI) % 3 != 0:
    for i in range(3 - (len(optionsGUI) % 3)):
        optionsGUI.append("X")

print(optionsGUI)

length = len(optionsGUI)

print('+++++++++++++++++++++++++++++++++++++++++++ available files +++++++++++++++++++++++++++++++++++++++++++')

for x in range(0, length, 3):
    print("["+ str(x) + "]" + optionsGUI[x] + (" " * (40 - (len(optionsGUI[x]) + len("["+ str(x) + "]")))) +
          "["+ str(x+1) + "]" + optionsGUI[x+1] +(" " * (40 - (len(optionsGUI[x+1]) + len("["+ str(x+1) + "]")))) +
          "["+ str(x+2) + "]" + optionsGUI[x+2])

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')


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
    german = [(line.split("-", 1)[0]).strip() for line in f]
with open(file, "r") as f:
    english = [(line.split("-", 1)[1]).strip() for line in f]

total = len(english)
score = 0

mode = int(input("English to German(1)\nGerman to English(2)\n"))

if mode == 1: # English To German
    while len(english) > 0:
        englishWord = random.choice(english)
        germanWord = german[english.index(englishWord)]

        answer = str(input(f'\nWhat is {englishWord} in German? '))
        answer = answer.strip()

        if answer == germanWord:
            score = score + 1
            print(f'Correct! {score}/{total}')
            german.remove(germanWord)
            english.remove(englishWord)
        else:
            print(f'Incorrect! {score}/{total}. The correct spelling of {englishWord} is: {germanWord}. Your answer was: {answer}')

if mode == 2:
    while len(german) > 0:
        germanWord = random.choice(german)
        englishWord = english[german.index(germanWord)]

        answer = str(input(f'\nWhat is {germanWord} in English? '))
        answer = answer.strip()

        if answer == englishWord:
            score = score + 1
            print(f'Correct! {score}/{total}')
            german.remove(germanWord)
            english.remove(englishWord)
        else:
            print(f'Incorrect! {score}/{total}. The correct spelling of {germanWord} is: {englishWord}. Your answer was: {answer}')
