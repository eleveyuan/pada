import pandas as pd

from pada.features.feature import BaseFeature
from pada.features.pipeline import FeatureEngineeringPipeline
from pada.assemble.hooks import Hooker
from pada.utils.state import OneOrMore


def run(data: pd.DataFrame, urls: OneOrMore[OneOrMore[BaseFeature]]):
    pass

