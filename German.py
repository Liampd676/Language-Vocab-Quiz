import random
import os
import re

# turns something like (u) or (ss) into its proper form
def textToAccent(string):
    accentDict = {
        '(ss)' : 'ß',
        '(a)' : 'ä',
        '(o)' : 'ö',
        '(u)' : 'ü',
        '(A)' : 'Ä',
        '(O)' : 'Ö',
        '(U)' : 'Ü'
    }
    startPoint = 0
    endPoint = 0
    for i in range(len(string)):
        if string[i] == '(':
            startPoint = i
        elif string[i] == ')':
            endPoint = i

    if endPoint != 0:
        point = string[startPoint:endPoint + 1]
        accent = accentDict[point]
        if string[-1] != ')':
            newWord = string[0:startPoint] + accent + string[endPoint + 1:-1] + string[-1]
        else:
            newWord = string[0:startPoint] + accent + string[endPoint + 1:-1]
        return newWord
    else:
        return string

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
        if name.lower() == 'r':
            Program()
            return
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
    initialEnglishList = list(english)
    initialGermanList = list(german)

    while True:
        mode = input("English to German(1)\nGerman to English(2)\n")
        if not mode.isnumeric():
            print('OOPS INVALID INPUT')
            continue
        elif int(mode) == 1 or int(mode) == 2:
            break
        elif mode.lower() == 'r':
            Program()
            return
        else:
            print('OOPS! INVALID INPUT')
            continue

    batchSize = 5
    currentBatch = []
    perviousWord = ""

    # English To German
    if int(mode) == 1:
        if len(english)>=batchSize:
            for i in range(batchSize):
                batchWord = random.choice(initialEnglishList)
                initialEnglishList.remove(batchWord)
                currentBatch.append(batchWord)

        while len(english) > 0:
            englishWord = random.choice(currentBatch)

            while perviousWord == englishWord and len(english)>1:
                englishWord = random.choice(currentBatch)

            germanWord = german[english.index(englishWord)]
            AccentGermanWord = textToAccent(germanWord)
            perviousWord = englishWord
            answer = str(input(f'\nWhat is {englishWord} in German? '))
            answer = answer.strip()

            if answer.lower() == 'r':
                Program()
                return

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
                print(f'Incorrect! {score}/{total}. \nThe correct spelling of {englishWord} is: {AccentGermanWord}')

    # German to English
    if int(mode) == 2:
        if len(german)>=batchSize:  # initialises a batch with German words
            for i in range(batchSize):
                batchWord = random.choice(initialGermanList)
                initialGermanList.remove(batchWord)
                currentBatch.append(batchWord)

        while len(german) > 0:  # chooses a german word from the batch
            germanWord = random.choice(currentBatch)
            while perviousWord == germanWord and len(german) > 1:  # if the picked word is the same as before then it picks another
                germanWord = random.choice(currentBatch)

            englishWord = english[german.index(germanWord)]  # list
            englishWordList = re.split(', |/|; ', englishWord)
            correctEnglishList = []


            if (englishWordList[0][0:3]) == 'the':
                correctEnglishList.append(englishWordList[0])
                for i in range(1, len(englishWordList)):
                    correctEnglishList.append('the ' + englishWordList[i])

            elif (englishWordList[0][0:2]) == 'to':
                correctEnglishList.append(englishWordList[0])
                for i in range(1, len(englishWordList)):
                    correctEnglishList.append('to ' + englishWordList[i])

            else:
                correctEnglishList.append(englishWordList[0])
                for i in range(1, len(englishWordList)):
                    correctEnglishList.append(englishWordList[i])
            correctEnglishList.append(englishWord)

            perviousWord = germanWord
            AccentGermanWord = textToAccent(germanWord)
            answer = str(input(f'\nWhat is {AccentGermanWord} in English? '))
            answer = answer.strip()

            if answer.lower() == 'r':
                Program()
                return

            if answer in correctEnglishList:
                score = score + 1
                print(f'Correct! {score}/{total}')
                german.remove(germanWord)
                english.remove(englishWord)
                if len(german) == 0:
                    break
                currentBatch.remove(germanWord)
                newWord = random.choice(german)
                if len(german)>=batchSize:
                    while len(currentBatch)<batchSize:
                        while newWord in currentBatch:
                            newWord = random.choice(german)
                        currentBatch.append(newWord)
            else:
                print(f'Incorrect! {score}/{total}. The correct spelling of {AccentGermanWord} is: {englishWord}')

Program()

while True:
    playAgain = input('Yay, You Won!!!!!!!!!!!!!\nWould you like to play again? (y/n) ')
    if playAgain.lower() == "n":
        exit()
    if playAgain.lower() == "y":
        Program()
    else:
        continue

