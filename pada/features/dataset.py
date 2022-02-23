# -*- coding: utf-8 -*-
import os
from funcy import cached_property

from pada.assemble.visitor import FeatureEngineerPart, FeatureEngineerVisitor


class Data(FeatureEngineerPart):
    """a base data loader class"""
    def __init__(self, data):
        self._data = data

    def accept(self, obj: FeatureEngineerVisitor):
        pass


def train_test_split(*arrays,
                     test_size=None,
                     train_size=None,
                     random_state=None,
                     shuffle=True):
    pass