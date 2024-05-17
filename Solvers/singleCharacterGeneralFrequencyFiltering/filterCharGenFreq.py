class WordleHelper:
    def __init__(self, wordsListPath):
        f = open(wordsListPath, 'r')
        self.words = [x.replace('\n', '') for x in f]
        f.close()
        self.confirmedLetters = set(())
    def reset(self):
        self.confirmedLetters = set(())
        

def main():
    f = open('wordleWords.txt', 'r')
    words = [x.replace('\n', '') for x in f]
    f.close()
    confirmedLetters = set(())
    guess = 1
    status = [-1, -1, -1, -1, -1]
    guessedWord = words[0]
    print(f'Guess #{guess}: {guessedWord}')
    while True:
        status = input().replace(' ', '')
        status = [int(x) for x in status]
        for i in range(0, 5):
            if status[i] == 0:
                if (guessedWord[i] in confirmedLetters):
                    words = list(filter(lambda x: guessedWord[i] != x[i], words))
                else:
                    words = list(filter(lambda x: guessedWord[i] not in x, words))
            elif status[i] == 1:
                words = list(filter(lambda x: guessedWord[i] in x, words))
                words = list(filter(lambda x: guessedWord[i] != x[i], words))
            elif status[i] == 2:
                confirmedLetters.add(guessedWord[i])
                words = list(filter(lambda x: guessedWord[i] == x[i], words))
        if len(words) == 1:
            print(f'Answer: {words[0]}')
            break
        if len(words) == 0:
            print('Word not found!')
            break
        guess += 1
        guessedWord = words[0]
        print(f'Guess #{guess}: {guessedWord}')


if __name__ == '__main__':
    main()
