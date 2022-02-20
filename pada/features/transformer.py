from sklearn.preprocessing import FunctionTransformer

from pada.libs import BaseTransformer, IdentityTransformer, SubsetTransformer
from pada.utils.state import OneOrMore, TransformerLike

def desugar_transformer(
    transformer: TransformerLike,
) -> BaseTransformer:
    """Replace transformer syntactic sugar with actual transformer

    The following syntactic sugar is supported:
    - `None` is replaced with an IdentityTransformer
    - a callable (function or lambda) is replaced with a FunctionTransformer
        that wraps that callable
    - a tuple (input, transformer) is replaced with a SubsetTransformer
    """
    if transformer is None:
        return IdentityTransformer()
    elif callable(transformer) and not isinstance(transformer, type):
        return FunctionTransformer(transformer)
    elif isinstance(transformer, tuple):
        return SubsetTransformer(*transformer)
    else:
        transformer = cast(BaseTransformer, transformer)
        return transformer