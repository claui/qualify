"""Test package containing modules which refer to each other by
their unqualified top-level names."""

import python_qualify

python_qualify.enable_submodules(__name__)
