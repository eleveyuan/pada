from pada.feature.features import BaseFeature
import sklearn.preprocessing

input = ['pet_cat']
transformer = sklearn.preprocessing.StandardScaler()
_feats0 = BaseFeature(input, transformer)

# input = 'kid_'
# transformer = sklearn.preprocessing.StandardScaler()
# _feats3 = BaseFeature(input, transformer)

input = 'pet'
transformer = sklearn.preprocessing.LabelBinarizer()
_feats = BaseFeature(input, transformer)


input = ['children']
transformer = sklearn.preprocessing.StandardScaler()
_feats1 = BaseFeature(input, transformer)


# input = ['kids']
# transformer = sklearn.preprocessing.StandardScaler()
# _feats2 = BaseFeature(input, transformer)
