from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}
def get_total_points(belts=ninja_belts):
    """Calculate the amount of points rewarded on PyBites given the
       ninja_belts dictionary, formula: belt score x belt owners (aka ninjas)
       (of course there are more points but let's keep it simple)

       Make your code generic so if we update ninja_belts to include
       more belts (which we do in the tests) it will still work.

       Ah and you can get score and ninjas from the namedtuple with nice
       attribute access: belt.score / belt.ninjas (reason why we get
       you familiar with namedtuple here, because we love them and use
       them all over the place!)

       Return the total number of points int from the function."""
    result = 0
    for color, numbers in belts.items():
        total_numbers = numbers[0] * numbers[1]
        result += total_numbers

    return result


def test_get_total_points_given_belts():
    assert get_total_points(ninja_belts) == 2675

def test_get_total_points_more_belts():
    more_belts = dict(brown=BeltStats(400, 2),
                      black=BeltStats(600, 5))

    # this way to dict merge is >= 3.5 (PEP 448)
    ninja_belts_updated = {**ninja_belts, **more_belts}

    assert get_total_points(ninja_belts_updated) == 6475

def main():
    test_get_total_points_given_belts()
    test_get_total_points_more_belts()

if __name__ == '__main__':
    main()

