import pandas as pd


class FeatureEngineerVisitor:
    """base visitor class"""
    def visit(self, obj):
        pass


class FeatureEngineerPart:
    """base entity class"""
    def accept(self, obj: FeatureEngineerVisitor):
        obj.visit(self)


class Data(FeatureEngineerPart):
    """a base data loader class"""
    def __init__(self, data):
        self._data = data

    def accept(self, obj: FeatureEngineerVisitor):
        obj.visit(self)



class DataGet(FeatureEngineerPart):
    def accept(self, obj: FeatureEngineerVisitor):
        print('DataGet')
        obj.visit(self)


class FeatureGet(FeatureEngineerPart):
    def accept(self, obj: FeatureEngineerVisitor):
        print('FeatureGet')
        obj.visit(self)


class FeatureStack(FeatureEngineerPart):
    def accept(self, obj: FeatureEngineerVisitor):
        print('FeatureStack')
        obj.visit(self)


class ValidFeature(FeatureEngineerPart):
    # TODO
    def accept(self, obj: FeatureEngineerVisitor):
        pass


class Pipe(FeatureEngineerPart):
    def __init__(self, data: pd.DataFrame):
        self._parts = [
            Data(data),
            DataGet(),
            FeatureGet(),
            FeatureStack()
        ]

    def accept(self, obj: FeatureEngineerVisitor):
        for _part in self._parts:
            _part.accept(obj)


class Assemble(FeatureEngineerVisitor):
    _data = None

    def visit(self, obj):
        if isinstance(obj, Data):
            print('Assemble Data')
            self._data = getattr(obj, '_data')
        if isinstance(obj, DataGet):
            print('Assemble DataGet')
        if isinstance(obj, FeatureGet):
            print('Assemble FeatureGet')
        if isinstance(obj, FeatureStack):
            print('Assemble FeatureStack')


# pipe = Pipe()
# pipe.accept(Assemble())