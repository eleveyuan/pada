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

    sig_fit = signature(transformer.fit)
    if '(X, y=None' not in str(sig_fit):
        raise CheckTransformerDefError(f'Invalid signature for transformer.fit: {sig_fit}')

    sig_transform = signature(transformer.transform)
    if '(X' not in str(sig_transform):
        raise CheckTransformerDefError(
            f'Invalid signature for transformer.transform: {sig_transform}')