
#Fill in the blanks
def fillBlanks(word):
    blanks = []
    
    for i in range(0,len(word)):
        blanks.append(' _ ')

    return blanks
    



# add a letter to blanks
def addLetter(letter, word, blanks):

     for i in range(0,len(word)):
        if letter == word[i]:
            blanks[i] = letter

     return blanks



#check to see if word is guessed

def wordGuessed(word, currentBlank):
    count = 0
    
    for i in range(0,len(word)):
        if word[i] == currentBlank[i]:
            count += 1

    if count == len(word):
        return 0
    else:
        return 1

def displayBlanks(blanks):
    print ("The word you are guessing looks like this: ")
    print (" ")
    print (''.join(blanks))
    print (" ")
    return



def main():
    word = input("Player 1 choose a word: ")

    currentBlank = fillBlanks(word)

    maxGuesses = 10
    guesses = 0
    found = 1

    while found == 1 and guesses < maxGuesses:
        displayBlanks(currentBlank)

        letter = input("Player 2 Enter a letter: ")
        if letter in word:
            currentBlank = addLetter(letter, word, currentBlank)

            found = wordGuessed(word, currentBlank)
        else:
            guesses += 1
    
        
    if found == 1 and guesses >= maxGuesses:
        print("Too many guesses. You Lose, the word was: ", word)
    elif found == 0:
        print("Nice job! You Win")
        print("The word is: ", word)


main()
        
        
    
    
            
            
