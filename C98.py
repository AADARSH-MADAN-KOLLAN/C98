def readFile():
    fileName = input("Enter File Name: ")
    f = open(fileName, "r")
    no_of_words = 0
    for line in f:
        words= line.split()
        no_of_words = no_of_words+len(words)
        print(no_of_words)

readFile()


    