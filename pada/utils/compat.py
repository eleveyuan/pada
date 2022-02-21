# -*- coding: utf-8 -*-
import sys
from typing import List, Optional, Tuple, Union

try:
    from os import PathLike
except ImportError:
    from pathlib import Path
    PathLike = (Path, )

# nullcontext new in 3.7?
try:
    from contextlib import nullcontext
except ImportError:
    from funcy import nullcontext


