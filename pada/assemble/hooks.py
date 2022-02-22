from typing import Callable

import pandas as pd


class Hooker:

    def __init__(self, data: pd.DataFrame):
        self._header = data.columns
        self._data_caller = None

    def register_feat_parse(self):
        return self

    def register_feat_valid(self):
        # TODO
        return self