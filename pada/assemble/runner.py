import pandas as pd

from pada.assemble.visitor import (Pipe, Assemble)

data = pd.DataFrame({'pet':      ['cat', 'dog', 'dog', 'fish', 'cat', 'dog', 'cat', 'fish'],
                     'children': [4., 6, 3, 3, 2, 3, 5, 4],
                     'salary':   [90., 24, 44, 27, 32, 59, 36, 27]})


def run(data: pd.DataFrame):
    pipe = Pipe(data)
    pipe.accept(Assemble())


def test(featuere: str):
    """test function: test feature or features in module"""
    pass


run(data)
