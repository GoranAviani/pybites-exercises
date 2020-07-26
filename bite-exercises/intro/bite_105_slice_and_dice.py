"""
    Take the block of text provided and strip off the whitespace at both ends.
    Split the text by newline (\n).
    Loop through the lines, for each line:
        strip off any leading spaces,
        check if the first character is lowercase,
        if so, split the line into words and get the last word,
        strip off BOTH the trailing dot (.) and exclamation mark (!) from this last word,
        and finally add it to the results list.
    Return the results list.

"""
text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""
another_text = """
Take the block of text provided and strip() off the whitespace at the ends.
Split the whole block up by newline (\n).
 if the first character is lowercase, split it into words and add the last word
of that line to the results list.
Strip the trailing dot (.) and exclamation mark (!) from the word first.
  finally return the results list!
"""


def test_slice_and_dice_default_text():
    expected = ['objects', 'y', 'too', ':)', 'bites']
    assert slice_and_dice(text) == expected


def test_slice_and_dice_other_text():
    expected = ['word', 'list', 'list']
    assert slice_and_dice(another_text) == expected

def slice_and_dice(text: str = text) -> list:
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""
    result = []
    text = text.strip()
    text = text.split('\n')

    cleanded_sentence = []
    for sentence in text:
        sentence = sentence.strip()
        cleanded_sentence.append(sentence)


    for sentence in cleanded_sentence:
        if sentence[0].islower():
            sentence_split = sentence.split(" ")
            last_word = sentence_split[len(sentence_split) - 1: len(sentence_split)]
            last_word = last_word[0].replace('.','')
            last_word = last_word.replace('!', '')
            result.append(last_word)

            test = result



    results = []


def main():
    slice_and_dice(text)

if __name__ == '__main__':
    main()