# Zachary Niehoff, Tucker Cooper, Wesley Wolff, Joshua Hueber
# SDEV 220
# Hangman Project: Group 5
# Due October 12th, 2021

import random

class HangMan():
    def __init__(self):
        self.word = None
        self.guessedLetters = []
        self.length = 0
        self.playerGuess = ''
        self.playerScore = ''
        self.lives = 0
        self.checkWord = ''

    # Opens a text file containing the words to use in our hang man game.
    # It chooses a random word from the list and returns it. 
    def getNewWord(self):
        wordList = open('hangmanwords.txt', 'r')
        hmwNum = random.randint(0,24)
        for i, line in enumerate(wordList):
            if i == hmwNum:
                self.word = line.strip()
                self.length = len(line)

    # Prints the word and shows asterisks for letters that have yet to be guessed
    def wordCheck(self):
        wordStatus = []
        for i in range(0,(self.length-1)):
            if self.word[i] not in self.guessedLetters:
                wordStatus.append('*')
            else:
                wordStatus.append(self.word[i])
        self.checkWord = ''.join(wordStatus)

    # Checks the guess to see if the letter is a match or 
    def checkGuess(self):
        if self.playerGuess not in self.word:
            if (self.lives - 1) != 0:
                self.lives -= 1
                self.gameTurn()
            else:
                self.gameOver(result = False)
        else:
            self.wordCheck()
            if ''.join(self.checkWord) == self.word:
                print("You win!")
                self.gameOver(result = True)
            else:
                self.gameTurn()

    # creates a loop to play the game            
    def gameTurn(self):
        # self.displayHouse()
        self.wordCheck()
        print(self.checkWord)
        self.guessLetter()
        self.checkGuess()

    # Function that calls for the player to input a letter then checks to make sure it is:
    #  1. a letter 
    #  2. only 1 letter 
    #  3. not already guessed
    #  If it doesn't meet all three criteria then it returns "Invalid Input" and loops the function until
    #   a valid input is intered.
    def guessLetter(self):
        pGuess = str(input("Guess a letter: "))
        if pGuess.isalpha() and len(pGuess) == 1 and pGuess not in self.guessedLetters:
            self.guessedLetters.append(pGuess)
            self.playerGuess = pGuess
        else:
            print("Invalid Input.")
            self.guessLetter()
    
    # Initializes a new game.
    def newGame(self):
        self.getNewWord()
        self.guessedLetters = ['a', 'i', 'e', 'o', 'u']
        self.lives = 7
        print("New Game Started!\n")
        self.gameTurn()


    # The gameover prompt.  If the player loses they can chose to start again or quit.
    def gameOver(self, result):
        if result:
            print("Game over! \n You win! \n Play again? (y/n)")
        else:
            print("Game over! \n You lose! \n Play again? (y/n)")
        def playAgain():
            choice = input('')
            if choice == 'y':
                self.newGame()
            elif choice == 'n':
                quit()
            else:
                print("Invalid Input \n Play again? (y/n)")
                playAgain()
        playAgain()

        



def main():
    game = HangMan()
    game.newGame()


main()