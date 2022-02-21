# -*- coding: utf-8 -*-
"""
base check
"""


class PadaWarning(UserWarning):
    """Base warning for pada"""
    pass


class PadaError(Exception):
    """Base error for pada"""
    pass

"""
check errors
"""


class CheckModuleError(Exception):
    """valid module error"""
    pass


class CheckRegexError(Exception):
    """regex pattern error for check"""
    pass


class ColumnsError(Exception):
    """input column error for check"""
    pass


class CheckTransformerDefError(Exception):
    """transformer behave error for check"""
    pass


class CheckStackFeatureorderError(Exception):
    """Stack Feature order error for check"""
    pass


class FeatureCollectionError(PadaError):
    """Error in collecting Feature instances from some source"""
    pass


class NoFeaturesCollectedError(FeatureCollectionError):
    """Expected to collect some features but did not find any"""
    pass


class UnsuccessfulInputConversionError(PadaError):
    """Input-type conversion for execution within pipeline was unsuccessful"""
    pass
