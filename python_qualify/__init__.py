"""
.. include:: ../README.md

## API Documentation
"""

# Re-export these symbols
# (This promotes them from python_qualify.python_qualify to python_qualify)
from python_qualify.api import enable_submodules as enable_submodules

from python_qualify.version import version

__all__ = [
    # Tell pdoc to pick up all re-exported symbols
    'enable_submodules',

    # Modules that every subpackage should see
    # (This also exposes them to pdoc)
    'api',
    'settings',
]

__version__ = version()
