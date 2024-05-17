import sys


def frequencyScore(word):
    """Use to prioritise guesses.

    Calculate a score for each word.
    based on the frequency of the letters that occure in it.
    Multiple occurences of the same letter in the word will
    decrease the letters score.
    """
    frequencyTable = {
        'e': 12.02,
        't': 9.1,
        'a': 8.12,
        'o': 7.68,
        'i': 7.31,
        'n': 6.95,
        's': 6.28,
        'r': 6.02,
        'h': 5.92,
        'd': 4.32,
        'l': 3.98,
        'u': 2.88,
        'c': 2.71,
        'm': 2.61,
        'f': 2.3,
        'y': 2.11,
        'w': 2.09,
        'g': 2.03,
        'p': 1.82,
        'b': 1.49,
        'v': 1.11,
        'k': 0.69,
        'x': 0.17,
        'q': 0.11,
        'j': 0.1,
        'z': 0.07
        }
    letterCount = {}
    score = 0
    for letter in word:
        if letter in letterCount:
            letterCount[letter] += 1
        else:
            letterCount.update({letter: 1})
        score += frequencyTable[letter] / letterCount[letter]
        letterCount[letter] += 1
    return score

def sortCharGenFreq(words):
    return sorted(fiveLetterWords, key=frequencyScore, reverse=True)
