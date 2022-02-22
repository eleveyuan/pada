import pandas as pd

from pada.assemble.hooks import Hooker
from pada.utils.state import OneOrMore


def run(data: pd.DataFrame, urls: OneOrMore):
    _hooker = Hooker(data)

