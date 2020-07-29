import pytest






def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""
    pass





def main():
    pass

if __name__ == '__main__':
    main()










@pytest.mark.parametrize("numerator, denominator, expected", [
    (1, 2, 0.5),
    (8, 2, 4),
    # strings that look like ints are converted (casted) fine
    ('3', '2', 1.5),
    # floats work too but when casted to int they are rounded down!
    (8.2, 2, 4),
    (1, 2.9, 0.5),
])
def test_divide_numbers_good_inputs(numerator, denominator, expected):
    assert divide_numbers(numerator, denominator) == expected


@pytest.mark.parametrize("numerator, denominator", [
    # ignoring dict/set/list to keep it simple, those would actually
    # throw a TypeError when passed into int()
    (2, 's'),
    ('s', 2),
    ('v', 'w'),
])
def test_divide_numbers_raises_value_error(numerator, denominator):
    with pytest.raises(ValueError):
        divide_numbers(numerator, denominator)


def test_divide_by_zero_does_not_raise_zero_division_exception():
    assert divide_numbers(10, 0) == 0