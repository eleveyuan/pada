# -*- coding: utf-8 -*-
from inspect import signature

from pada.libs import BaseTransformer
from pada.utils.state import OneOrMore
from pada.check.exception import CheckTransformerDefError


def check_route(route: str):
    pass


def check_input_columns(cols: OneOrMore[str]):
    pass


def check_transformer(transformer: BaseTransformer):
    """check transformer behave"""
    if not all(
        hasattr(transformer, attr)
        for attr in ['fit', 'transform', 'fit_transform']
    ):
        raise CheckTransformerDefError('Transformer object missing required attribute')

    # https://github.com/ballet/ballet/issues/92#issue-1148839747
    sig_fit = signature(transformer.fit)
    if '(X, y=None' not in str(sig_fit) and '(y' not in str(sig_fit):
        raise CheckTransformerDefError(f'Invalid signature for transformer.fit: {sig_fit}')

    sig_transform = signature(transformer.transform)
    if '(X' not in str(sig_transform) and '(y' not in str(sig_fit):
        raise CheckTransformerDefError(
            f'Invalid signature for transformer.transform: {sig_transform}')


class CrossLinkChecker:
    def __init__(self):
        pass

    @property
    def is_circle(self):
        """relationship between featueres include a circle or not"""
        return False
