# -*- coding: utf-8 -*-
class FeatureEngineerVisitor:
    """base visitor class"""
    def visit(self, obj):
        pass


class FeatureEngineerPart:
    """base entity class"""
    def accept(self, obj: FeatureEngineerVisitor):
        obj.visit(self)
