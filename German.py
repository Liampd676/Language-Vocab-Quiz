import random
import os
import numpy as np

# prints the test files which are available
options = os.listdir("German Vocab/")
optionsNP = np.array(options)


if len(optionsNP) % 3 != 0:
    for i in range(3 - (len(optionsNP) % 3)):
        optionsNP = np.append(optionsNP, ["X"])

optionsNP = np.reshape(optionsNP, [int(len(optionsNP) / 3), 3])

print('+++++++++++++++++++++++++++++++++++++++++++ available files +++++++++++++++++++++++++++++++++++++++++++')
for y in range(9):
    for x in range(1):
        print("["+ str(x+y*3) + "]" + optionsNP[y,x] + (" " * (40 - (len(optionsNP[y,x]) + len("["+ str(x+y*3) + "]")))) +
              "["+ str(x+1+y*3) + "]" + optionsNP[y,x+1] +(" " * (40 - (len(optionsNP[y,x+1]) + len("["+ str(x+1+y*3) + "]")))) +
              "["+ str(x+2+y*3) + "]" + optionsNP[y,x+2])

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
