# -*- coding: utf-8 -*-
from collections import defaultdict
from inspect import signature
from typing import Optional, Tuple

from funcy import cached_property
from slugify import slugify

import pada.feature.pipeline
import pada.assemble.visit
from pada.check.exception import CheckStackFeatureorderError
from pada.feature.transformer import RobustTransformer, make_robust_transformer
from pada.utils.state import (FeatureInputType, FeatureTransformerType, OneOrMore,)


class BaseFeature:
    """A feature definition

    Conceptually, a feature definition is a learned function that maps raw
    variables in one data instance to a vector of feature values. A feature
    definition can produce either a scalar feature value for each instance
    or a vector of feature values, as in the case of an embedding technique
    like PCA or the one-hot encoding of a categorical variable.

    Args:
        input: required columns from the input dataframe needed for the
            transformation. There is also preliminary support for using other
            pandas indexing, such as selection by callable -- if you pass a
            callable, the entities data frame will be indexed using the
            callable. This is not officially supported by the underlying
            sklearn-pandas library, so please report any issues you experience.
        transformer: transformer, sequence of transformers, or ``None``. A
            "transformer" is an instance of a class that provides a
            fit/transform-style learned transformation. Alternately, a
            callable can be provided, either by itself or in a list, in
            which case it will be converted into a
            :py:class:``FunctionTransformer`` for convenience. If ``None``
            is provided, it will be replaced with the
            :py:class:``IdentityTransformer``.
        name: name of the feature
        description: description of the feature
        output: base name or ordered sequence of names of feature values
            produced by this transformer
        source: the module in which this feature was defined
        options: options
    """

    def __init__(
        self,
        input: FeatureInputType,
        transformer: FeatureTransformerType,
        name: Optional[str] = None,
        description: Optional[str] = None,
        output: Optional[OneOrMore[str]] = None,
        source: Optional[str] = None,
        options: Optional[dict] = None
    ):
        self.input = input
        self.transformer = make_robust_transformer(transformer)
        self.name = name
        self.description = description
        self.output = (
            output
            or (slugify(self.name, separator='_') if self.name else None)
        )
        self.source = source
        self.options = options or {}

    @cached_property
    def _init_attr_list(self):
        return list(signature(self.__init__).parameters)

    def __repr__(self):
        indent = 4
        attr_list = self._init_attr_list
        attrs_str = ',\n'.join(
            '{indent}{attr_name}={attr_val!s}'.format(
                indent=' ' * indent,
                attr_name=attr,
                attr_val=getattr(self, attr)
            ) for attr in attr_list
        )
        return '{clsname}(\n{attrs_str}\n)'.format(
            clsname=type(self).__name__, attrs_str=attrs_str)

    def as_input_transformer_tuple(
        self
    ) -> Tuple[FeatureInputType, RobustTransformer, dict]:
        """Return an tuple for passing to DataFrameMapper constructor"""
        return self.input, self.transformer, {'alias': self.output}

    def as_feature_engineering_pipeline(
        self
    ) -> pada.feature.pipeline.FeatureEngineeringPipeline:
        """Return standalone FeatureEngineeringPipeline with this feature"""
        return pada.feature.pipeline.FeatureEngineeringPipeline(self)

    @property
    def author(self) -> Optional[str]:
        """The author of this feature if it can be inferred from its source

        The author can be inferred if the module the feature was defined in
        follows the pattern
        ``package.subpackage.user_username.feature_featurename``. Otherwise,
        returns ``None``.
        """
        if self.source:
            pieces = self.source.rsplit('.', maxsplit=2)
            if len(pieces) >= 2:
                user_str = pieces[-2]
                if user_str.startswith('user_'):
                    return user_str[len('user_'):]

        return None

    _pipeline = None

    @property
    def pipeline(self) -> pada.feature.pipeline.FeatureEngineeringPipeline:
        """A feature engineering pipeline containing just this feature"""
        if self._pipeline is None:
            self._pipeline = self.as_feature_engineering_pipeline()

        return self._pipeline

    def fit(self, X, y=None):
        """Fit feature.pipeline"""
        return self.pipeline.fit(X, y=y)

    def transform(self, X):
        """Transform data using feature.pipeline"""
        return self.pipeline.transform(X)

    def fit_transform(self, X, y=None):
        """Fit feature.pipeline and then transform data"""
        return self.fit(X, y=y).transform(X)


class FeaturesStack(pada.assemble.visit.FeatureEngineerVisitor):
    def __init__(self):
        self._features = []
        self._g = defaultdict(list)
        self._inv_g = defaultdict(list)
        self._stack = []

    def stack(self, feature: BaseFeature, input: OneOrMore[str], output: Optional[OneOrMore[str]]):
        self._features.append({
            'feature': feature,
            'input': input,  # must be true feature name
            'output': output  # not truely output feature name, maybe a alias
        })

    def _build(self, obj):
        collected = obj._data.columns.values
        builded_idx = 0
        for i in range(len(self._features)):
            cur = self._features[i]
            temp_pipe = cur['feature'].pipeline
            try:
                transformed = temp_pipe.fit_transform(obj._data)
                output = temp_pipe.transformed_names_

                if all(el in cur['input'] for el in output):
                    output = [_name + '_ed' for _name in output]

                # TODO naive implement, should be more compatible
                if cur['output'] is None:
                    cur['output'] = output
                else:
                    cur['output'] = output

                obj._data[output] = transformed

                temp = self._features[i]
                self._features[i] = self._features[builded_idx]
                self._features[builded_idx] = temp
                builded_idx += 1

            except Exception:
                pass

        if builded_idx >= len(self._features):
            self._graph()
        else:
            raise CheckStackFeatureorderError(
                f'dependencies column(s) {self._features[builded_idx]["input"]} not exist')

    def _graph(self):
        feats_num = len(self._features)

        for i in range(feats_num):
            self._g[i] = []
            for j in range(feats_num):
                if j != i and all(el in self._features[i]['output'] for el in self._features[j]['input']):
                    self._g[i].append(j)
        # inverse graph
        for k in self._g.keys():
            self._inv_g[k] = []
        for k, v in self._g.items():
            for el in v:
                self._inv_g[el].append(k)

    def visit(self, obj):
        self._build(obj)



