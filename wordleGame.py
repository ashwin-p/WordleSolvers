import random

class WordleGame:
    def __init__(self, wordFile):
        self.wordFile = wordFile
        self.word = ""
        self.guessCount = 0
        self.selectWord()

    def selectWord(self):
        f = open(self.wordFile, 'r')
        self.words = f.readlines()
        wordIndex = random.randint(0, len(self.words))
        self.word = self.words[wordIndex].replace('\n', '')
        f.close()

    def evalGuess(self, guess):
        eval = [0, 0, 0, 0, 0]
        guess = list(guess)
        self.guessCount += 1
        tempWord = list(self.word)

        for i in range(0, 5):
            if guess[i] == tempWord[i]:
                eval[i] = 2
                tempWord[i] = '$'
                guess[i] = '$'

        for i in range(0, 5):
            if guess[i] == '$':
                continue
            if guess[i] in tempWord:
                eval[i] = 1

        if (eval == [2, 2, 2, 2, 2]):
            totalGuesses = self.guessCount
            self.reset()
            return eval, totalGuesses
        return eval, self.guessCount

    def countGuesses(self):
        return self.guessCount

    def reset(self):
        self.guessCount = 0
        wordIndex = random.randint(0, len(self.words))
        self.word = self.words[wordIndex].replace('\n', '')


def main():
    game = WordleGame('wordleWords.txt')
    print('Selected word is:', game.word)
    while True:
        eval, guessCount = game.evalGuess(input('Enter your guess: '))
        print(f'Evaluation of guess #{guessCount}: {eval}')
        if (eval == [2, 2, 2, 2, 2]):
            print('You win!')
            print('Game has reset')
            print('Selected word is', game.word)

if __name__ == '__main__':
    main()
