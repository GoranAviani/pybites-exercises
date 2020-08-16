"""
    Calculate the dictionary word that would have the most value in Scrabble.
    There are 3 tasks to complete for this Bite:
        Done First write a function to read in the dictionary.txt file (= DICTIONARY constant), returning a list of words
        (note that the words are separated by new lines).
        Done Second write a function that receives a word and calculates its value. Use the scores stored in LETTER_SCORES.
        Letters that are not in LETTER_SCORES should be omitted (= get a 0 score).
        With these two pieces in place, write a third function that takes a list of words and returns the word with
        the highest value.
    Look at the TESTS tab to see what your code needs to pass. Enjoy!
"""

import os
import urllib.request

# PREWORK
def test_load_words():
    words = load_words()

    assert type(words) == list
    assert len(words) == 235886
    assert words[0] == 'A'
    assert words[-1] == 'Zyzzogeton'
    assert ' ' not in ''.join(words)
    print("Test passed")

def test_calc_word_value():
    assert calc_word_value('bob') == 7
    assert calc_word_value('JuliaN') == 13
    assert calc_word_value('PyBites') == 14
    assert calc_word_value('benzalphenylhydrazone') == 56
    print("Test passed!")

def test_max_word_value():
    test_words = ['bob', 'julian', 'pybites', 'quit', 'barbeque']
    assert max_word_value(test_words) == 'barbeque'
    words = load_words()
    assert max_word_value(words[20000:21000]) == 'benzalphenylhydrazone'

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# start coding
def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    result = []
    TMP = os.getenv("TMP", "/tmp")
    S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
    DICT = 'dictionary.txt'
    DICTIONARY = os.path.join(TMP, DICT)
    urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

    with open(DICTIONARY) as f:
        for word in f.read().split():
            result.append(word)

    return result

def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    result = {}
    value = 0
    for letter in word:
        for score in scrabble_scores:
            if letter.upper() in score[1]:
                value += score[0]
    result = value

    return result

def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    pass


def main():
    #words1 = load_words()
    #words2 = calc_word_value(words1)
    #tests = words2

    test_load_words()
    test_calc_word_value()

if __name__ == '__main__':
    main()




