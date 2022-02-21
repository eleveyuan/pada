# -*- coding: utf-8 -*-
from typing import Callable, List, TypeVar, Union

from pada.utils.compat import PathLike

T = TypeVar('T')
OneOrMore = Union[T, List[T]]
Pathy = Union[str, PathLike]
TransformerLike = Union[Callable, 'padas.features.BaseTransformer', None]
FeatureInputType = Union[OneOrMore[str], Callable[..., OneOrMore[str]]]
FeatureTransformerType = OneOrMore[TransformerLike]
