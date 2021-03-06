# -*- coding: utf-8 -*-
import warnings
from contextlib import redirect_stderr, redirect_stdout, suppress
from copy import deepcopy
from logging import Logger, LogRecord
from os import devnull
from typing import Optional, Sequence, Sized, Tuple, TypeVar

import numpy as np
import pandas as pd
import sklearn.datasets
from funcy import complement, decorator, lfilter
from funcy.decorators import Call

from pada.check.exception import PadaError
from pada.utils.log import logger


def asarray2d(a: np.ndarray) -> np.ndarray:
    """Cast to 2d array"""
    arr = np.asarray(a)
    if arr.ndim == 1:
        arr = arr.reshape(-1, 1)
    return arr


def get_arr_desc(arr: np.ndarray) -> str:
    """Get array description, in the form '<array type> <array shape>'"""
    type_ = type(arr).__name__  # see also __qualname__
    shape = getattr(arr, 'shape', '<no shape>')
    return f'{type_} {shape}'


def indent(text: str, n=4) -> str:
    """Indent each line of text by n spaces"""
    _indent = ' ' * n
    return '\n'.join(_indent + line for line in text.split('\n'))


def make_plural_suffix(obj: Sized, suffix='s') -> str:
    if len(obj) != 1:
        return suffix
    else:
        return ''


def has_nans(obj) -> bool:
    """Check if obj has any NaNs

    Compatible with different behavior of np.isnan, which sometimes applies
    over all axes (py35+) and sometimes does not (py34).
    """
    nans = np.isnan(obj)
    while np.ndim(nans):
        nans = np.any(nans)
    return bool(nans)


@decorator
def dfilter(call: Call, pred):
    """Decorate a callable with a filter that accepts a predicate

    Example::

        >>> @dfilter(lambda x: x >= 0)
        ... def numbers():
        ...     return [-1, 2, 0, -2]
        [2, 0]
    """
    return lfilter(pred, call())


def load_sklearn_df(name: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    method_name = f'load_{name}'
    method = getattr(sklearn.datasets, method_name)
    data = method()
    X_df = pd.DataFrame(data=data.data, columns=data.feature_names)
    y_df = pd.Series(data.target, name='target')
    return X_df, y_df


@decorator
def quiet(call: Call):
    with open(devnull, 'w') as fnull:
        with redirect_stderr(fnull), redirect_stdout(fnull):
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                return call()


class DeepcopyMixin:

    def __deepcopy__(self, memo: dict):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result


_T = TypeVar('_T')


def one_or_raise(seq: Sequence[_T]) -> _T:
    n = len(seq)
    if n == 1:
        return seq[0]
    else:
        raise ValueError(f'Expected exactly 1 element, but got {n}')


def warn(msg: str):
    """Issue a warning message of category BalletWarning"""
    warnings.warn(msg, category=PadaError)


@decorator
def raiseifnone(call: Call):
    """Decorate a function to raise a ValueError if result is None"""
    result = call()
    if result is None:
        raise ValueError
    else:
        return result


def falsy(o) -> bool:
    """Check whether o is falsy

    In this case, a falsy value is one of the following:
    1. the singleton value `False`
    2. the string 'false' (ignoring case)
    3. the empty string
    """
    if isinstance(o, bool):
        return not o
    return isinstance(o, str) and (o.lower() == 'false' or o == '')


truthy = complement(falsy)
"""Check whether o is truthy

In this case, a truthy value is any value that is not falsy.
"""


@decorator
def nonnegative(call: Call, name: Optional[str] = None):
    """Warn if the function's return value is negative and set it to 0"""
    result = call()
    with suppress(TypeError):
        if result < 0:
            result = 0.0
            # Format a nice log message
            if name is None:
                try:
                    pieces = call._func.__name__.split('_')[1:]
                    name = ''.join(map(str.capitalize, pieces))
                except RuntimeError:
                    name = 'Result'
            logger.warning(f'{name} should be non-negative.')
    return result


@decorator
def dont_log_nonnegative(call: Call, logger: Logger = logger):
    def filter(record: LogRecord) -> int:
        return 0 if 'should be non-negative' in record.msg else 1
    logger.addFilter(filter)
    try:
        return call()
    finally:
        logger.removeFilter(filter)


# re-export cookiecutter work_in
# work_in = cookiecutter.utils.work_in


def skipna(a: np.ndarray, b: np.ndarray, *c: np.ndarray, how: str = 'left'):
    """Drop rows of both a and b corresponding to missing values

    The length of a and b along the first dimension must be equal.

    Args:
        a:
            first array
        b:
            second array
        *c:
            any additional arrays
        how:
            how to determine the rows to drop, one of 'left', 'any', or 'all'.
            If left, then any row in which a has a missing value is dropped. If
            any, then any row in which at least one of a, b, or additional
            arrays has a missing value is dropped. If all , then any row in
            which all of a, b, and additional arrays has a missing value is
            dropped. Defaults to left.

    Returns:
        tuple of a, b, and any additional arrays where a, b, and any
        additional arrays are guaranteed to be the same length with missing
        values removed according to ``how``.
    """
    if how not in ('left', 'any', 'all'):
        raise ValueError(f'Invalid value for how: {how}')

    def find_nan_inds(arr):
        nan_inds = np.isnan(arr)
        if arr.ndim > 1:
            nan_inds = nan_inds.any(axis=1)
        nan_inds = nan_inds.squeeze()
        assert nan_inds.shape == (arr.shape[0],)
        return nan_inds

    if how == 'left':
        nan_inds = find_nan_inds(a)
    elif how == 'any':
        arr = np.concatenate(
            (asarray2d(a), asarray2d(b), *(asarray2d(c0) for c0 in c)),
            axis=1
        )
        nan_inds = find_nan_inds(arr)
    elif how == 'all':
        nan_inds = find_nan_inds(a)
        for arr in [b, *c]:
            nan_inds &= find_nan_inds(arr)

    a_out = a[~nan_inds]
    b_out = b[~nan_inds]
    c_out = [
        arr[~nan_inds]
        for arr in c
    ]
    out = (a_out, b_out, *c_out)
    return out
