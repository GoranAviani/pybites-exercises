"""
    Write a function that can sum up numbers:
        It should receive a list of n numbers.
        If no argument is provided, return sum of numbers 1..100.
        Look closely to the type of the function's default argument ...
    Have fun!
    :return:
"""
def test_sum_numbers_default_args():
    assert sum_numbers() == 5050
    assert sum_numbers(numbers=None) == 5050


def test_sum_numbers_various_inputs():
    assert sum_numbers(range(1, 11)) == 55
    assert sum_numbers([1, 2, 3]) == 6
    assert sum_numbers((1, 2, 3)) == 6
    assert sum_numbers([]) == 0  # !! [] not the same as None

def sum_numbers(numbers=None):
    if numbers == []:
        return 0
    elif not numbers:
        addition = sum(range(1, 101))
    else:
        addition = sum(numbers)

    return addition


def main():
    test_sum_numbers_default_args()
    test_sum_numbers_various_inputs()



if __name__ == '__main__':
    main()