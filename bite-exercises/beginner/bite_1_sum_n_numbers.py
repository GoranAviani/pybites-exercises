"""
    Write a function that can sum up numbers:
        It should receive a list of n numbers.
        If no argument is provided, return sum of numbers 1..100.
        Look closely to the type of the function's default argument ...
    Have fun!
    :return:
"""

def sum_numbers(numbers=None):
    addition = 0
    if not numbers:
        for x in range(1, 100):
            addition += x
    else:
        for x in numbers:
            addition += x

    return addition


def main():
    sum_numbers([1, 2, 3])



if __name__ == '__main__':
    main()