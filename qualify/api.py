"""The primary module in qualify.

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


def prune_submodules(package: Union[str, ModuleType]) -> None:
    """Removes transitive imports from `sys.modules`.
    Calling this function is optional, but recommended to keep the
    global namespace clean from unwanted top-level modules.

    Example: Directory `d` contains modules `a` and `b`.
    `a` imports `b`.

    Running `enable_submodules('d'); import d.a` will add four
    new entries to `sys.modules`: `d`, `d.a`, `d.b`, and `b`.
    The first three are legitimate, but `b` has been added as a
    side effect of importing `d.a`, and is now polluting the global
    namespace of top-level modules.

    To undo this side effect, call `prune_submodules('d')`.

    :param package:
        Controls which top-level modules are to be removed from
        `sys.modules`.
        All top-level modules which have been added to `sys.modules`
        as a side effect of `enable('package')` will be removed.

        May be a module object or a string.
    """
    raise NotImplementedError
