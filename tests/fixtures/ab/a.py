# pylint: disable=missing-function-docstring, missing-module-docstring

from b import world  # type: ignore  # pylint: disable=import-error

def hello() -> str:
    return f'Hello, {world()}!'
