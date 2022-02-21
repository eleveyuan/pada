# -*- coding: utf-8 -*-
from pada.utils.state import OneOrMore

def assemble():
    pass


class Named1:
    def __init__(self, input: OneOrMore[str], output: OneOrMore[str]):
        self._input = input
        self._output = output


origin = ['a', 'b', 'c', 'd']  # 用于存储原始特征
collected = []  # 用于收集是否特征是否出现过
is_circle = False  # 是否存在特征的循环依赖

f1 = Named1('a', 'A')
f2 = Named1(['A', 'b'], 'B')
f3 = Named1('c', 'C')
# f4 = Named1('c', 'D')
f5 = Named1(['C', 'D'], 'E')
f6 = Named1('d', 'F')


def _stack_check(named):
    _input = getattr(named, '_input')
    _output = getattr(named, '_output')
    if _input not in origin and _input not in collected:
        raise Exception('input name not exist')
    if _output in collected:
        raise Exception('output name already exist')

    collected.append(_output)