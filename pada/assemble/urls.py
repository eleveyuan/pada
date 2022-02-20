import inspect
import re
from time import ctime
from typing import Optional

from pada.features.feature import BaseFeature
from pada.utils.log import logger
from pada.check.exception import CheckModuleError


def _convert_route(route: str):
    if route == '':
        return re.compile('^.*$')
    return re.compile('^' + route + '$')


def _print_matched(attrs, name: Optional[str]):
    if name is None:
        name = ''
    print(f"{ctime()}: matched feats `{', '.join(attrs)}`")


def url(feats: BaseFeature, route: str, name: Optional[str]):
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
        raise CheckModuleError('feats must be a module')