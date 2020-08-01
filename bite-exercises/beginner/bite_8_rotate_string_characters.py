"""
    Write a function that rotates characters in a string, in both directions:
        if n is positive move characters from beginning to end, e.g.: rotate('hello', 2)
        would return llohe
        if n is negative move characters to the start of the string, e.g.: rotate('hello', -2)
        would return lohel
    See tests for more info. Have fun!

"""
def test_small_rotate():
    assert rotate('hello', 2) == 'llohe'
    assert rotate('hello', -2) == 'lohel'

def test_bigger_rotation_of_positive_n():
    string = 'bob and julian love pybites!'
    expected = 'love pybites!bob and julian '
    assert rotate(string, 15) == expected

def test_bigger_rotation_of_negative_n():
    string = 'pybites loves julian and bob!'
    expected = 'julian and bob!pybites loves '
    assert rotate(string, -15) == expected



def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    if n > 0:
        return string[n: len(string)] + string[0: n]
    else:
        return string[len(string) + n: len(string)] + string[0: len(string) + n]

def main():
    result = rotate('hello', 2)
    result = rotate('hello', -2)
    test_small_rotate()
    test_bigger_rotation_of_positive_n()
    test_bigger_rotation_of_negative_n()


if __name__ == '__main__':
    main()


