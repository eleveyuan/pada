# -*- coding: utf-8 -*-
import os
from funcy import cached_property

import pandas as pd

from pada.assemble.watch import FeatureEngineerPart, FeatureEngineerVisitor


class Data(FeatureEngineerPart):
    """a base data loader class"""
    def __init__(self, data: pd.DataFrame):
        self._data = data
        self._cols = data.columns.values
        self._org_data = data


def train_test_split(*arrays,
                     test_size=None,
                     train_size=None,
                     random_state=None,
                     shuffle=True):
    pass