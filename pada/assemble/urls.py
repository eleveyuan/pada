import inspect
import re
from time import ctime

from pada.features.feature import BaseFeature
from pada.utils.log import logger


def _convert_route(route):
    if route == '':
        return re.compile('^.*$')
    return re.compile('^' + route + '$')


def _print_matched(attrs, name=None):
    if name is None:
        name = ''
    print(f"{ctime()}: matched feats `{', '.join(attrs)}`")


def url(feats, route, name=None):
    feats_list, attrs = [], []
    if inspect.ismodule(feats):
        pattern = _convert_route(route)
        for attr in dir(feats):  # simple use dir() to get local object in module
            feat_def = getattr(feats, attr)
            if isinstance(feat_def, BaseFeature) and re.match(pattern, attr):
                feats_list.append(feat_def)
                attrs.append(attr)
        # _print_matched(attrs, name)
        logger.debug(f"matched feats `{', '.join(attrs)}` in module {feats.__name__}")
        return feats_list
    else:
        raise TypeError('feats must be a module')