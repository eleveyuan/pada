# __package__ = 'test_templates'
from pada.assemble.locates import url

from definition import feats_def


urls_pattern = [
    url(feats_def, '*')
]