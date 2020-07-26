message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

def test_split_in_columns_default_message():
    # one line string but a nice way in Python to wrap over multiple lines
    expected = ('Hello world!|We hope that you are learning a lot of Python.|'
                'Have fun with our Bites of Py.|Keep calm and code in Python!'
                '|Become a PyBites ninja!')

    actual = split_in_columns()
    assert actual == expected

def test_split_in_columns_on_other_message():
    expected = 'Hello world:|I am coding in Python :)|How awesome!'

    message = 'Hello world:\nI am coding in Python :)\nHow awesome!'
    actual = split_in_columns(message)

    assert actual == expected

def main():
    result = split_in_columns(message)
    test_split_in_columns_default_message()
    test_split_in_columns_on_other_message()

def split_in_columns(message=message):
    """Split the message by newline (\n) and join it together on '|'
       (pipe), return the obtained output string"""
    message = message.split('\n')
    message = '|'.join(message)
    return message

if __name__ == '__main__':
    main()