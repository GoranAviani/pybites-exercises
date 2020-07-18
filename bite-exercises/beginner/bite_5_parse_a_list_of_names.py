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
def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    result = []
    for name in names:
        title_name = name.title()
        if title_name not in result:
            result.append(title_name)
    return result



def main():
    NAMES1 = dedup_and_title_case_names(NAMES)
    test = NAMES1


if __name__ == '__main__':
    main()