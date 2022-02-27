# -*- coding: utf-8 -*-
from pada.utils.state import OneOrMore
from pada.check.exception import ColumnsError


def assemble():
    pass


class FeatStack:
    def __init__(self, input: OneOrMore[str], output: OneOrMore[str]):
        self._input = input
        self._output = output


_origin = {'a', 'b', 'c', 'd'}  # 用于存储原始特征
_collected = {'a', 'b', 'c', 'd'}  # 用于收集是否特征是否出现过
_is_circle = False  # 是否存在特征的循环依赖
_g = []


def _stack_check(feats: OneOrMore[str]):
    _input = getattr(feats, '_input')
    _output = getattr(feats, '_output')

    if isinstance(_input, str):
        _input = [_input, ]
    if isinstance(_output, str):
        _output = [_output, ]
    print(not set(_input).issubset(set(_origin)), not set(_input).issubset(set(_collected)))
    if not set(_input).issubset(set(_origin)) and not set(_input).issubset(set(_collected)):
        raise ColumnsError('input columns not exist')
    if set(_output).issubset(set(_collected)):
        raise ColumnsError('output columns already exist')

    for item in _output:
        _collected.add(item)


# f1 = FeatStack('a', 'A')
# f2 = FeatStack(['A', 'b'], 'B')
# f3 = FeatStack('c', 'C')
# # f4 = FeatStack('c', 'D')
# f5 = FeatStack(['C', 'D'], 'E')
# f6 = FeatStack('d', 'F')
#
#
# _stack_check(f1)
# _stack_check(f2)
# _stack_check(f3)
# # _stack_check(f4)
# _stack_check(f5)
# _stack_check(f6)


class Node:
    def __init__(self, data, inject, emit):
        self._data = data
        self._in = inject
        self._out = emit


class Edge:
    def __init__(self, hnode, tnode, hlink, tlink):
        self._hnode = hnode
        self._tnode = tnode
        self._hlink = hlink
        self._tlink = tlink


class OLG:
    def __init__(self):
        self._g = []
        self._olg = []
        self._org = []
        self._org_nodes = []
        self._collect_nodes = []
        self._feature_map = {}

    def append(self, node):
        _input = getattr(node, 'input')
        _output = getattr(node, 'output')
        _node = Node(node, None, None)
        if _output is None:
            self._org_nodes.append(_node)
        else:
            self._collect_nodes.append(_node)
        self._feature_map[node] = {'intput': _input, 'output': _output}

    def _gen_edge(self):
        pass


    def relationship(self):
        pass

    def get_in_path(self, node):
        """get depend path"""
        pass

    def get_out_paht(self, node):
        pass

    def is_circle(self):
        """graph exists circle or not"""
        pass


class Mock:
    def __init__(self, input, transfromer, output):
        self.input = input
        self.transformer = transfromer
        self.output = output


if __name__ == '__main__':
    origin = ['a', 'b', 'c', 'd']
    olg = OLG()
    olg.append(Mock('a', None, None))
    olg.append(Mock('c', None, None))
    olg.append(Mock('d', None, None))
    olg.append(Mock('b', None, None))

    olg.append(Mock(['a', 'b'], None, 'e'))
    olg.append(Mock('a', None, 'f'))
    olg.append(Mock(['a', 'f'], None, 'k'))
    olg.append(Mock('c', None, 'g'))

