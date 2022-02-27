from pada.feature.features import BaseFeature
import sklearn.preprocessing


input = 'pet'
transformer = sklearn.preprocessing.LabelBinarizer()
_feats = BaseFeature(input, transformer)


print('a' == ['a'])
