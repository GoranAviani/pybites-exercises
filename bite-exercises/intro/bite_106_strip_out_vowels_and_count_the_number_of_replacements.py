"""
    In this Bite we'd like you to loop over the characters in the large block of text (the most important text for any Python programmer: The Zen of Python!)
    Within this loop you'll perform the following actions:
        Replace all vowels (aeiou) with stars (*), do this case insensitively.
        Count the number of replacements you do (= vowels in the text).
        Return the new block of text post replacements and the count of vowels you replaced.
    Hint: Try converting the block of text to a list first to make working with the characters simpler.
    Tip: If you're struggling, work on one step at a time and expand on your code slowly. Don't try and tackle every requirement right away.
    Bonus: if you already have some Python under your belt, try to use re and try to solve it without a for loop :)
"""

def test_strip_vowels_on_zen():
    output, number_replacements = strip_vowels(text)

    assert number_replacements == 262

    assert 'Th* Z*n *f Pyth*n, by T*m P*t*rs' in output
    assert 'B***t*f*l *s b*tt*r th*n *gly' in output
    assert 'N*m*sp*c*s *r* *n* h*nk*ng gr**t *d**' in output
    assert '*lth**gh pr*ct*c*l*ty b**ts p*r*ty.' in output


def main():
    pass


def strip_vowels(text: str) -> Tuple[str, int]:
    """Replace all vowels in the input text string by a star
       character (*).
       Return a tuple of (replaced_text, number_of_vowels_found)

       So if this function is called like:
       strip_vowels('hello world')

       ... it would return:
       ('h*ll* w*rld', 3)

       The str/int types in the function defintion above are part
       of Python's new type hinting:
       https://docs.python.org/3/library/typing.html"""
    pass

if __name__ == '__main__':
    main()