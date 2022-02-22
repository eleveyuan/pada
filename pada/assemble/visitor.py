class FeatureEngineerVisitor:
    """base visitor class"""
    def visit(self, obj):
        pass


class FeatureEngineerPart:
    """base entity class"""
    def accept(self, obj: FeatureEngineerVisitor):
        pass


class DataGet(FeatureEngineerPart):
    def accept(self, obj: FeatureEngineerVisitor):
        print('DataGet')


class FeatureGet(FeatureEngineerPart):
    def accept(self, obj: FeatureEngineerVisitor):
        print('FeatureGet')


class FeatureStack(FeatureEngineerPart):
    def accept(self, obj: FeatureEngineerVisitor):
        print('FeatureStack')


class ValidFeature(FeatureEngineerPart):
    # TODO
    def accept(self, obj: FeatureEngineerVisitor):
        pass


class Pipe(FeatureEngineerPart):
    def __init__(self):
        self._parts = [
            DataGet(),
            FeatureGet(),
            FeatureStack()
        ]

    def accept(self, obj: FeatureEngineerVisitor):
        for _part in self._parts:
            _part.accept(obj)
        obj.visit(self)


class Assemble(FeatureEngineerVisitor):
    def visit(self, obj):
        if isinstance(obj, FeatureEngineerPart):
            print('Assemble DataGet')
        if isinstance(obj, FeatureEngineerPart):
            print('Assemble FeatureGet')
        if isinstance(obj, FeatureEngineerPart):
            print('Assemble FeatureStack')
