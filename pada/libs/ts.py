# -*- coding: utf-8 -*-
from typing import Iterable

from sklearn.pipeline import FeatureUnion

from pada.libs.base import GroupedFunctionTransformer

__all__ = (
    'SingleLagger',
    'make_multi_lagger'
)

"""
base class copy from ballat directly
"""


class SingleLagger(GroupedFunctionTransformer):
    """Transformer that applies a lag operator to each group

    Args:
        lag: lag to apply
        groupby_kwargs: keyword arguments to pd.DataFrame.groupby
    """

    def __init__(self, lag: int, groupby_kwargs: dict = None):
        super().__init__(lambda x: x.shift(lag), groupby_kwargs=groupby_kwargs)


def make_multi_lagger(
    lags: Iterable[int], groupby_kwargs: dict = None
) -> FeatureUnion:
    """Return a union of transformers that apply different lags

    Args:
        lags: collection of lags to apply
        groupby_kwargs: keyword arguments to pd.DataFrame.groupby
    """
    laggers = [
        SingleLagger(lag, groupby_kwargs=groupby_kwargs)
        for lag in lags
    ]
    feature_union = FeatureUnion([
        (repr(lagger), lagger) for lagger in laggers
    ])
    return feature_union
