import pytest
import inspect

import feats_def
from pada.feature.features import BaseFeature
from pada.assemble.locates import url

# pytest.main(["-m", "add", "-s"])


def test_url():
    feats_list = url(feats, '', name='feats')
    assert len(feats_list) > 0
    for feat in feats_list:
        assert isinstance(feat, BaseFeature)

    feats_list = url(feats, '.*', name='feats')
    assert len(feats_list) > 0
    for feat in feats_list:
        assert isinstance(feat, BaseFeature)

    feats_list = url(feats, 'feats_.*', name='feats')
    assert len(feats_list) > 0
    for feat in feats_list:
        assert isinstance(feat, BaseFeature)
