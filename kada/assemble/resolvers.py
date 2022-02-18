import re


def get_url_resolver(route):
    pass


def _route_to_regex(route):
    """
        Convert a path pattern into a regular expression. Return the regular
        expression and a dictionary mapping the capture names to the converters.
        For example, 'foo/<int:pk>' returns '^foo\\/(?P<pk>[0-9]+)'
        and {'pk': <django.urls.converters.IntConverter>}.
    """
    original_route = route


class BasePattern():
    def __init__(self, route, name):
        self._route = route
        self._name = name
        self.converters = _route_to_regex(str(route))[1]

class RePattern():
    def __init__(self, route):
        self._route = route


class URLPattern():
    pass


class URLResolver():
    pass
