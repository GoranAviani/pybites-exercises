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

def test_sort_by_surname_desc_different_names_list():
    names = sort_by_surname_desc(PY_CONTENT_CREATORS)
    assert names[0] == 'Julian Sequeira'
    assert names[-1] == 'Dan Bader'





def main():
    test_dedup_and_title_case_names()
    test_dedup_and_title_case_names_different_names_list()
    test_sort_by_surname_desc_different_names_list()

def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    result = []
    for name in names:
        title_name = name.title()
        if title_name not in result:
            result.append(title_name)
    return result

def sort_by_surname_desc(names):
    """

    :param names:
    :return:
    """
    result_list = []
    master_list = []
    for full_name in names:
        title_name = full_name.title()
        full_name_list = title_name.split(" ")
        full_info_dict = {"last_name": full_name_list[1], "full_name": title_name}
        master_list.append(full_info_dict)

    print(master_list)

    sorted_list_od_dicts = sort_by_last_name(master_list)


    result_list = dict_to_list(sorted_list_od_dicts)

    return result_list

def dict_to_list(sorted_list_od_dicts):
    result = []
    for full_info in sorted_list_od_dicts:
        result.append(full_info["full_name"])
    return result


def sort_by_last_name(full_info_dict):
    from operator import itemgetter
    result = sorted(full_info_dict, key=itemgetter('last_name'), reverse=True)
    return result

if __name__ == '__main__':
    main()