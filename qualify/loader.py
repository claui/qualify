"""Clones a loaded module under a different name."""

import importlib
from importlib.machinery import ModuleSpec
from types import ModuleType

from .clone import clone


class CloneLoader(importlib.abc.Loader):
    """Clones a loaded module under a different name."""

    def __init__(self, source: ModuleType, dest_name: str) -> None:
        super().__init__()
        self.dest_name = dest_name
        self.source = source
        if not source.__spec__:
            raise ValueError('Missing `__spec__` in module')
        self.spec = ModuleSpec(
            source.__spec__.name, self, origin=source.__spec__.origin)


    def create_module(self, spec: ModuleSpec) -> ModuleType:
        assert self.spec == spec
        return clone(self.source, self.dest_name, add_to_sys_modules=False)


    def exec_module(self, _: ModuleType) -> None:  # pylint: disable=no-self-use
        """Called by `importlib`. Implemented as a no-op because the
        original module has already been executed."""


    def module_repr(self, _: ModuleType) -> str:
        raise NotImplementedError
