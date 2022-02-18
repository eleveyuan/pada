import pytest
import inspect

import feats
from kada.features.feature import BaseFeature
from kada.assemble.urls import url

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

    feats_list = url(feats, 'feat_.*', name='feats')
    assert len(feats_list) > 0
    for feat in feats_list:
        assert isinstance(feat, BaseFeature)
