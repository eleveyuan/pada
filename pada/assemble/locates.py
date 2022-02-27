# -*- coding: utf-8 -*-
import inspect
import re
from importlib import import_module
from time import ctime
from typing import Optional

import pada.feature.features
from pada.feature.datasets import Data
# from pada.feature.features import BaseFeature, FeaturesStack
from pada.utils.log import logger
from pada.check.exception import PadaError
from pada.check.exception import CheckModuleError
from pada.assemble import settings


def _data(pattern=settings.DATA_CONF):
    try:
        _module = import_module(pattern)
        _call = getattr(_module, 'data')
        if _call is not None:
            return Data(_call())
        else:
            raise PadaError('Not found function data()')
    except ModuleNotFoundError:
        raise ModuleNotFoundError()


def _urls(pattern=settings.URLS_CONF):
    try:
        _module = import_module(pattern)
        _attr = getattr(_module, 'urls_pattern')
        if _attr is not None:
            features_stack = pada.feature.features.FeaturesStack()
            for item in _attr:
                if isinstance(item, list):
                    for _feature in item:
                        _input = getattr(_feature, 'input')
                        if not isinstance(_input, list):
                            _input = [_input, ]
                        _output = getattr(_feature, 'output', None)
                        features_stack.stack(_feature, _input, _output)
                else:
                    _input = getattr(item, 'input')
                    _output = getattr(item, 'output', None)
                    features_stack.stack(item, _input, _output)
            return features_stack
        else:
            raise PadaError('Not found attribute urls_pattern')
    except ModuleNotFoundError:
        raise ModuleNotFoundError()


def _convert_route(route: str):
    if route == '' or route == '*':
        return re.compile('^.*$')
    return re.compile('^' + route + '$')


def _print_matched(attrs, name: Optional[str]):
    if name is None:
        name = ''
    print(f"{ctime()}: matched feats `{', '.join(attrs)}`")


def url(feats, route: str):
    feats_list, attrs = [], []
    if inspect.ismodule(feats):
        pattern = _convert_route(route)
        for attr in dir(feats):  # simple use dir() to get local object in module
            feat_def = getattr(feats, attr)
            if isinstance(feat_def, pada.feature.features.BaseFeature) and re.match(pattern, attr):
                feats_list.append(feat_def)
                attrs.append(attr)
        # _print_matched(attrs, name)
        logger.debug(f"matched feats `{', '.join(attrs)}` in module {feats.__name__}")
        return feats_list
    else:
        raise CheckModuleError('feats must be a module')
