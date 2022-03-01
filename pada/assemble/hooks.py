from typing import Callable

import pandas as pd

from pada.assemble import settings


class Hooker:

    def __init__(self):
        self._data_caller = None
        self._features_caller = None
        self._validation_caller = None
        self._filter_caller = None

    def register_data(self, call: Callable):
        self._data_caller = call
        return self

    def register_features(self, call: Callable):
        self._features_caller = call
        return self

    def register_validation(self, call: Callable):
        self._validation_caller = call
        return self

    def register_feature_selection(self, call: Callable):
        self._filter_caller = call
        return self

    def handle(self):
        _data_obj = self._data_caller(settings.DATA_CONF)
        _features_obj = self._features_caller(settings.URLS_CONF)

        _data_obj.accept(_features_obj)

        return _data_obj
