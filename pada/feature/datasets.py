# -*- coding: utf-8 -*-
import os
from funcy import cached_property

import pandas as pd

from pada.assemble.visit import FeatureEngineerPart, FeatureEngineerVisitor


class Data(FeatureEngineerPart):
    """a base data loader class"""
    def __init__(self, data: pd.DataFrame):
        self._data = data
        self._cols = data.columns.values
        self._org_data = data

    def __str__(self):
        return f'{self._data}'

    def __repr__(self):
        return f'{type(self._data)}({self._data})'


def train_test_split(*arrays,
                     test_size=None,
                     train_size=None,
                     random_state=None,
                     shuffle=True):
    pass