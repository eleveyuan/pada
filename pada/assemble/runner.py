from typing import Optional

import pandas as pd

from pada.feature.features import BaseFeature
from pada.assemble.hooks import Hooker
from pada.assemble.locates import _urls, _data


def run():
    hook = Hooker()
    hook.register_data(_data) \
        .register_features(_urls)

    return hook.handle()


def test(feature: Optional[BaseFeature]):
    """test function: test feature or features in module"""
    if feature is None:
        return run()

    # TODO get build.json infomation

    # TODO if build.json exists, then read it. partially get feature dependency and run

    # TODO if build.json doesn't exist, then invoke run() function
    hook = Hooker()
    hook.register_data(_data) \
        .register_features(_urls)



