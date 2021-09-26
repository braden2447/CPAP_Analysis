import pytest


def test_data_split():
    from cpap_database import data_split
    input_file = open('testing_data_split.txt', 'r')
    split_data = input_file.read()
    input_file.close()
    answer = data_split(split_data)
    expected = [['patient name 1', 'patient sleep',
                 'seal data', 'events', 'O2'],
                ['patient name 2', 'sleep', 'seal',
                 'events', 'O2']
                ]
    assert answer == expected


def test_data_manipulation():
    from cpap_database import data_manipulation
    test_data = [['patient name 1', '3.0',
                 'Seal, 4, 3, 4', 'Events, 1, 0, 1', 'O2, 93, 93, 95'],
                 ['patient 2', '2.25',
                 'Seal, 5, 0', 'Events, 2, 1', 'O2, 98, 99']
                 ]
    answer = data_manipulation(test_data)
    expected = [['patient name 1', 3.0,
                 [4.0, 3.0, 4.0], [1, 0, 1], [93, 93, 95]],
                ['patient 2', 2.25,
                 [5.0, 0.0], [2, 1], [98, 99]]
                ]
    assert answer == expected


def test_data_calculations():
    from cpap_database import data_calculations
    calc_test = [['patient name 1', 3.0,
                 [4.0, 3.0, 4.0], [1, 0, 1], [93, 93, 95]],
                 ['patient 2', 2.25,
                 [5.0, 0.0], [2, 1], [98, 99]]
                 ]
    answer = data_calculations(calc_test)
    expected = [['patient name 1', 3.0,
                 [4.0, 3.0, 4.0], [1, 0, 1], [93, 93, 95],
                 3.7, 0.7],
                ['patient 2', 2.25,
                 [5.0, 0.0], [2, 1], [98, 99],
                 2.5, 1.5]
                ]
    assert answer == expected


def test_diagnoses():
    from cpap_database import diagnoses
    diagnose_me = [['patient name 1', 3.25,
                   [6.5, 3.1, 4.0], [5, 6, 5], [92, 93, 94],
                    4.5, 5.3],
                   ['patient 2', 2.25,
                   [5.0, 0.0], [2, 1], [98, 99],
                   2.5, 1.5]
                   ]
    answer = diagnoses(diagnose_me)
    expected = [['patient name 1', 3.25,
                 [6.5, 3.1, 4.0], [5, 6, 5], [92, 93, 94],
                 4.5, 5.3, 'hypoxia apnea'],
                ['patient 2', 2.25,
                 [5.0, 0.0], [2, 1], [98, 99],
                 2.5, 1.5, 'normal sleep']
                ]
    assert answer == expected


def test_dictionaries():
    from cpap_database import dictionaries
    dict_test = [['Braden Garrison', 3.25,
                 [6.5, 3.1, 4.0], [5, 6, 5], [92, 93, 94],
                 4.5, 5.3, 'hypoxia apnea'],
                 ['Doug Garrison', 2.25,
                 [5.0, 0.0], [2, 1], [98, 99],
                 2.5, 1.5, 'normal sleep']
                 ]
    answer = dictionaries(dict_test)
    expected = [{'First Name': 'Braden',
                 'Last Name': 'Garrison',
                 'Hours': 3.25,
                 'Seal': [6.5, 3.1, 4.0],
                 'Events': [5, 6, 5],
                 'O2': [92, 93, 94],
                 'Seal Average': 4.5,
                 'Diagnosis': 'hypoxia apnea'},
                {'First Name': 'Doug',
                 'Last Name': 'Garrison',
                 'Hours': 2.25,
                 'Seal': [5.0, 0.0],
                 'Events': [2, 1],
                 'O2': [98, 99],
                 'Seal Average': 2.5,
                 'Diagnosis': 'normal sleep'}
                ]
    assert answer == expected
