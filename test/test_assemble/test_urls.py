import pytest
import inspect

import feats
from pada.features.feature import BaseFeature
from pada.assemble.urls import url

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
