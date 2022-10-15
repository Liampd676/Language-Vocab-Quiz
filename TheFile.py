import os

options = os.listdir("German Vocab/")
file = "German Vocab/"
germanArticle = ["der", "die", "das"]

for i in range(len(options)):
	newFile = []
	textFile = file+options[i]
	openedFile =  open(textFile, "r+")

	for j in openedFile:
		englishPart = j.split("-")[1]
		germanPart = j.split("-")[0]
		if (j[0:3] in germanArticle) and (englishPart[1:4] != "the"):
			correctedLine = germanPart + "-" + " the" + englishPart
			newFile.append(correctedLine)

		else:
			newFile.append(j)
	newFile = "".join(newFile)
	openedFile.seek(0)
	openedFile.write(newFile)
	openedFile.truncate()