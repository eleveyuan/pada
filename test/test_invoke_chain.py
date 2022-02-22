import pytest

from pada.assemble.runner import run


def mock_data():
    import pandas as pd
    data = pd.DataFrame({'pet': ['cat', 'dog', 'dog', 'fish', 'cat', 'dog', 'cat', 'fish'],
                    'children': [4., 6, 3, 3, 2, 3, 5, 4],
                    'salary': [90., 24, 44, 27, 32, 59, 36, 27],
                    'target': [1, 0, 0, 0, 0, 1, 0, 0]})
    return data


def test_run():
    dataset = mock_data()
    run(dataset)


