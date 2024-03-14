"""The primary module in python_qualify.

Contains convenience functions to enable `import` for top-level
modules which reside in a directory that is not on `sys.path`."""

import sys
from types import ModuleType
from typing import Union

from .finder import SubmoduleFinder


def enable_submodules(package: Union[str, ModuleType]) -> None:
    """Enables modules contained in a given package to be imported
    as qualified submodules.

    Example: Directory `d` contains modules `main` and `utils`.
    `main` imports `utils` as a top-level module, so if you just
    run `import d.main`, you’d get an error:

    > `ModuleNotFoundError: No module named 'utils'`

    Run `enable_submodules('d')` to allow `import d.main` to succeed.

    :param package:
        A package whose directory is not in `sys.path` but contains
        top-level modules that you want to import.

        After this function returns, you will be able to `import`
        those modules as submodules, even if they refer to each
        other by their top-level names.

        May be a package as a `ModuleType` or a package name.
    """
    sys.meta_path.insert(0, SubmoduleFinder(package))
