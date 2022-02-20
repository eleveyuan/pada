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

from pada.checks.exception import PadaWarning
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
