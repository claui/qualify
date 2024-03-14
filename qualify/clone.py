"""Clones a loaded Python module under a different name."""

from importlib.machinery import ModuleSpec
import sys
from types import ModuleType
from typing import Union, cast

import wrapt  # type: ignore


def clone(source: Union[str, ModuleType], dest: str,
    add_to_sys_modules: bool=True) -> ModuleType:
    """Clones a loaded Python module under a different name.

    :param source:
        The existing Python module to be cloned.
        May be a module object or a string.

    :param dest:
        The name of the newly-cloned module.

    :param add_to_sys_modules:
        Whether this method should add the resulting module to
        `sys.modules`.
        Defaults to `True`.
    """
    if not source or not dest:
        raise ValueError('Missing argument')

    source_obj = sys.modules[source] if isinstance(source, str) \
        else source
    if not (source_spec := source_obj.__spec__):
        raise ValueError('Missing `__spec__` in module')

    if dest in sys.modules:
        if source_spec.name == dest:
            return sys.modules[dest]
        raise ValueError(f'Module already exists: {dest}')

    dest_obj = cast(ModuleType, wrapt.ObjectProxy(source_obj))
    dest_obj.__spec__ = ModuleSpec(
        dest, source_spec.loader, origin=source_spec.origin)

    if add_to_sys_modules:
        sys.modules[dest] = dest_obj
    return dest_obj
