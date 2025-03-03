word = str("hola")
listChar = list(word) # converts every letter given into a list
listWord = word.split() # converts each word given into a list
underScoreList = []
attempts = 6
for char in listChar:
    underScoreList.append("_ ")
for i in range(attempts):
    answer = input("Give a letter: ")
    for i in range (len(listChar)):
        if answer == listChar[i]:
            underScoreList[i] = answer + " "
    print("".join(underScoreList))