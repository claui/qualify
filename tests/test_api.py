# pylint: disable=magic-value-comparison, missing-class-docstring, missing-function-docstring, missing-module-docstring, no-self-use, too-few-public-methods, too-many-public-methods

from tests.fixtures.ab import a


def test_qualified_import() -> None:
    assert a.hello() == 'Hello, world!'
