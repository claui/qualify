"""Finds a submodule if it is erroneously referred to under its base
name, i.e. as a top level module without qualifying it with its
(relative or absolute) package name.
"""

import importlib
from importlib.machinery import ModuleSpec
import sys
from types import ModuleType
from typing import Optional, Sequence, Union

from .loader import CloneLoader


class SubmoduleFinder(importlib.abc.MetaPathFinder):
    """Finds a submodule if it is erroneously referred to under its
    base name, i.e. as a top level module without qualifying it with
    its (relative or absolute) package name.

    Serves as a compatibility aid for wheel building and packaging
    upstream projects which use top-level `import` statements to load
    their own modules from the same package.
    """

    def __init__(self, parent: Union[str, ModuleType]) -> None:
        super().__init__()
        parent_obj = sys.modules[parent] if isinstance(parent, str) \
            else parent
        if not (parent_spec := parent_obj.__spec__):
            raise ValueError('Missing `__spec__` in parent module')
        self.parent_spec = parent_spec


    def find_spec(self, fullname: str, path: Optional[Sequence[str]],
        _: Optional[ModuleType]=None,
    ) -> Optional[ModuleSpec]:
        """Finds a submodule if it is erroneously referred to under
        its base name.
        """
        if path:
            return None
        qualified_name = importlib.util.resolve_name(
            f'.{fullname}', self.parent_spec.name)
        try:
            module = importlib.import_module(qualified_name)
        except ImportError:
            # Unrelated module from outside this package
            return None

        return CloneLoader(module, fullname).spec
