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
		englishPart = englishPart.lower()
		newLine = germanPart + "-" + englishPart
		newFile.append(newLine)
	newFile = "".join(newFile)#list to string
	openedFile.seek(0)#wipe old file
	openedFile.write(newFile)#write new file
	openedFile.truncate()