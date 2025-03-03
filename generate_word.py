import random

class GeneratingRandomWord:
    @staticmethod
    def generate_Random():
        with open("words.txt", "r", encoding="utf-8") as f:
            numberGenerated = random.randint(1,len(f.readlines())) # generate a random number starting from line 1 to the maximum number of lines in the file
            return numberGenerated
        
    @staticmethod
    def readingFile():
        lineFile = GeneratingRandomWord.generate_Random()  # Llamada csorrecta al método estático
        cont = 0
        with open("words.txt", "r", encoding="utf-8") as f:
            for line in f:
                cont += 1
                if cont == lineFile:
                    return line.strip()
        return None
