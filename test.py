import random

def generate_Random():
    with open("words.txt", "r", encoding="utf-8") as f:
        numberGenerated = random.randint(1,len(f.readlines())) # generate a random number starting from line 1 to the maximum number of lines in the file
        closeFile()
        return numberGenerated

def readingFile():
    cont = 0
    with open("words.txt", "r", encoding="utf-8") as f:
        for line in f:
            cont += 1
            if cont == lineFile:
                randomWord = line.strip()
                break
    closeFile()
    return randomWord

def closeFile():
    f.close()


with open("words.txt", "r", encoding="utf-8") as f: # we open the file and we specify the mode we want to use. In this case, "r" stands for only read
    lineFile = generate_Random() 
    print(lineFile)
    #print(f.read(lineFile).strip())
    randomWordToGuess = readingFile()
    print(randomWordToGuess)
    closeFile()
