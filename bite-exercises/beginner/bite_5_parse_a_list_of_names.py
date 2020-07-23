"""
    In this bite you will work with a list of names.
    First you will write a function to take out duplicates and title case them.
    Then you will sort the list in alphabetical descending order by surname and
    lastly determine what the shortest first name is. For this exercise you can assume
    there is always one name and one surname.
    With some handy Python builtins you can write this in a pretty concise way. Get it sorted :)
"""

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

PY_CONTENT_CREATORS = ['brian okken', 'michael kennedy', 'trey hunner',
                       'matt harrison', 'julian sequeira', 'dan bader',
                       'michael kennedy', 'brian okken', 'dan bader']


def test_dedup_and_title_case_names():
    names = dedup_and_title_case_names(NAMES)
    assert names.count('Bob Belderbos') == 1
    assert names.count('julian sequeira') == 0
    assert names.count('Brad Pitt') == 1
    assert len(names) == 10
    assert all(n.title() in names for n in NAMES)

def test_dedup_and_title_case_names_different_names_list():
    actual = sorted(dedup_and_title_case_names(PY_CONTENT_CREATORS))
    expected = ['Brian Okken', 'Dan Bader', 'Julian Sequeira',
                'Matt Harrison', 'Michael Kennedy', 'Trey Hunner']
    assert actual == expected




def main():
    test_dedup_and_title_case_names()
    test_dedup_and_title_case_names_different_names_list()



def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    result = []
    for name in names:
        title_name = name.title()
        if title_name not in result:
            result.append(title_name)
    return result


if __name__ == '__main__':
    main()