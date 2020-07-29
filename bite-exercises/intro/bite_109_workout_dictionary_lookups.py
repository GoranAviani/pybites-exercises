import pytest

WORKOUT_SCHEDULE = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
REST, CHILL_OUT, TRAIN = 'Rest', 'Chill out!', 'Go train {}'
INVALID_DAY = 'Not a valid day'


def get_workout_motd(day):
    """First title case the passed in day argument
       (so monday or MONDAY both result in Monday).

       If day is not in WORKOUT_SCHEDULE, return INVALID_DAY

       If day is in WORKOUT_SCHEDULE retrieve the value (workout)
       and return the following:
       - weekday, return TRAIN with the workout value interpolated
       - weekend day (value 'Rest'), return CHILL_OUT

       Examples:
       - if day is Monday -> function returns 'Go train Chest+biceps'
       - if day is Thursday -> function returns 'Go train Legs'
       - if day is Saturday -> function returns 'Chill out!'
       - if day is nonsense -> function returns 'Not a valid day'

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'
    """
    day = day.title()
    if day not in WORKOUT_SCHEDULE:
        return INVALID_DAY
    else:
        if WORKOUT_SCHEDULE[day] == 'Rest':
            return CHILL_OUT
        else:
            return (TRAIN . format(WORKOUT_SCHEDULE[day]))

def main():
    pass


if __name__ == '__main__':
    main()


# About parametrize: https://pybit.es/pytest-coding-100-tests.html
@pytest.mark.parametrize("day, expected", [
    ('Monday', 'Go train Chest+biceps'),
    ('monday', 'Go train Chest+biceps'),
    ('Tuesday', 'Go train Back+triceps'),
    ('TuEsdAy', 'Go train Back+triceps'),
    ('Wednesday', 'Go train Core'),
    ('wednesdaY', 'Go train Core'),
    ('Thursday', 'Go train Legs'),
    ('Friday', 'Go train Shoulders'),
    ('Saturday', CHILL_OUT),
    ('Sunday', CHILL_OUT),
    ('sundAy', CHILL_OUT),
    ('nonsense', INVALID_DAY),
    ('monday2', INVALID_DAY),
])
def test_get_workout_valid_case_insensitive_dict_lookups(day, expected):
    assert get_workout_motd(day) == expected