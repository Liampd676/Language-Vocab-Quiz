import random
import os

# a function for the whole script. It is needed for restarting THIS IS NOT OBSELETE
def Program():
    # prints the test files which are available
    options = os.listdir("German Vocab/")
    optionsGUI = options

    rowLen = 3
    padding = 34

    if len(optionsGUI) % rowLen != 0:
        for i in range(rowLen - (len(optionsGUI) % rowLen)):
            optionsGUI.append("X")

    length = len(optionsGUI)

    print('+++++++++++++++++++++++++++++++++++++++++++ available files +++++++++++++++++++++++++++++++++++++++++++')

    for column in range(0, length, rowLen):
        row = []
        for i in range(rowLen):
            item = "["+ str(column+i) + "]" + optionsGUI[column+i]  # e.g [28]Media.txt
            row.append(item +(" " * (padding - len(item))))
        print(*row, sep='')

    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    # Choosing a file to open
    while True:
        name = input("Either return the file name or the number to the left of the file you would like to open: ")
        if name.lower() == 'r': Program()
        name = str(name)

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
    initialList = list(english)
    mode = input("English to German(1)\nGerman to English(2)\n")
    if mode.lower() == 'r': Program()
    batchSize = 5
    currentBatch = []
    perviousWord = ""

    if int(mode) == 1: # English To German
        if len(english)>=batchSize:
            for i in range(batchSize):
                batchWord = random.choice(initialList)
                initialList.remove(batchWord)
                currentBatch.append(batchWord)

        while len(english) > 0:
            englishWord = random.choice(currentBatch)

            while perviousWord == englishWord and len(english)>1:
                englishWord = random.choice(currentBatch)

            germanWord = german[english.index(englishWord)]
            perviousWord = englishWord
            answer = str(input(f'\nWhat is {englishWord} in German? '))
            answer = answer.strip()

            if answer.lower() == 'r': Program()

            if answer == germanWord:
                score = score + 1
                print(f'Correct! {score}/{total}')
                german.remove(germanWord)
                english.remove(englishWord)
                if len(english) == 0:
                    break
                currentBatch.remove(englishWord)
                newWord = random.choice(english)
                if len(english)>=batchSize:
                    while len(currentBatch)<batchSize:
                        while newWord in currentBatch:
                            newWord = random.choice(english)
                        currentBatch.append(newWord)

            else:
                print(f'Incorrect! {score}/{total}. \nThe correct spelling of {englishWord} is: {germanWord}')

    if int(mode) == 2:
        while len(german) > 0:
            germanWord = random.choice(german)
            englishWord = english[german.index(germanWord)]

            answer = str(input(f'\nWhat is {germanWord} in English? '))
            answer = answer.strip()

            if answer.lower() == 'r': Program()

            if answer == englishWord:
                score = score + 1
                print(f'Correct! {score}/{total}')
                german.remove(germanWord)
                english.remove(englishWord)
            else:
                print(f'Incorrect! {score}/{total}. The correct spelling of {germanWord} is: {englishWord} \nYour answer was: {answer}')

Program()

while True:
    playAgain = print('Yay, You Won!!!!!!!!!!!!!\nWould you like to play again? (y/n) ')
    if playAgain.lower() == "n":
        exit()
    if playAgain.lower == "y":
        Program()
    else:
        continue

