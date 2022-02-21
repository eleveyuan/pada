# -*- coding: utf-8 -*-
import os
from funcy import cached_property


class DataLoader:
    """a base data loader class"""
    def __init__(self, name, path=None, desc=None):
        self._name = name
        if path is None:
            path = './data/'
        self._path = path
        self._desc = desc

    @cached_property
    def dataset(self):
        data_path = os.path.join(self._path, self._name)
        if os.path.exists(data_path):
            import pandas as pd
            temp = pd.read_csv(data_path)
            data, target = temp[:-1], temp[-1]
            return data, target
        else:
            raise FileExistsError('')


def train_test_split(*arrays,
                     test_size=None,
                     train_size=None,
                     random_state=None,
                     shuffle=True):
    pass