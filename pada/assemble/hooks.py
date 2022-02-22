from typing import Callable

import pandas as pd


class Hooker:

    def __init__(self, data: pd.DataFrame):
        self._header = data.columns
        self._data_caller = None

