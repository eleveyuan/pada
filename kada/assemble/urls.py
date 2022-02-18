from functools import partial
from importlib import import_module
import inspect, gc

from kada.feature import BaseFeature


def url(route, feats, name=None):
    if inspect.ismodule(feats):
        print('helle world')
        # a = getattr(feats, 'feat')
        print(inspect.getmembers(feats, inspect.isclass))

        for attr in dir(feats):

            print(attr, isinstance(getattr(feats, attr), BaseFeature))