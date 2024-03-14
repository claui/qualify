"""Test package containing modules which refer to each other by
their unqualified top-level names."""

import qualify
qualify.enable_submodules(__name__)
