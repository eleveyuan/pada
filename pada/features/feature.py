# -*- coding: utf-8 -*-
class BaseFeature:
    def __init__(self):
        self.a = 1


class SiblingBaseFeature(BaseFeature):
    def __init__(self):
        super().__init__()
        self.b = 1
