"""
.. include:: ../README.md

## API Documentation
"""

# Re-export these symbols
# (This promotes them from qualify.qualify to qualify)
from qualify.api import enable_submodules as enable_submodules

from qualify.version import version

__all__ = [
    # Tell pdoc to pick up all re-exported symbols
    'enable_submodules',

    # Modules that every subpackage should see
    # (This also exposes them to pdoc)
    'api',
    'settings',
]

__version__ = version()
