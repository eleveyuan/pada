# -*- coding: utf-8 -*-
import pathlib
from typing import Optional

from cookiecutter.main import cookiecutter as _cookiecutter
import funcy as fy

from pada.utils.compat import PathLike
from pada.utils.state import Pathy


TEMPLATES_PATH = pathlib.Path(__file__).resolve().parent.joinpath('templates')
PROJECT_TEMPLATE_PATH = TEMPLATES_PATH.joinpath('project_template')


def _stringify_path(obj) -> str:
    return str(obj) if isinstance(obj, PathLike) else obj


@fy.wraps(_cookiecutter)
def cookiecutter(*args, **kwargs) -> str:
    """Call cookiecutter.main.cookiecutter after stringifying paths

    Return:
        project directory path
    """
    # funcy.walk/walk_values类似map函数，第一个参数为函数，第二个参数是集合，然后函数对集合一一作用
    args = fy.walk(_stringify_path, args)
    kwargs = fy.walk_values(_stringify_path, kwargs)
    return _cookiecutter(*args, **kwargs)


def render_project_template(project_template_path: Optional[Pathy] = None, **cc_kwargs):
    if project_template_path is None:
        project_template_path = PROJECT_TEMPLATE_PATH

    project_path = cookiecutter(project_template_path, **cc_kwargs)

    return project_path
