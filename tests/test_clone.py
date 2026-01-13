# pylint: disable=magic-value-comparison, missing-class-docstring, missing-function-docstring, missing-module-docstring, no-self-use, too-few-public-methods, too-many-public-methods

import calendar
import sys

import pytest

from python_qualify.clone import clone


@pytest.fixture(autouse=True)
def reset_sys_modules(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delitem(sys.modules, 'cloned_calendar', raising=False)


def test_source_empty() -> None:
    with pytest.raises(ValueError, match='Missing argument'):
        clone('', 'bar')


def test_dest_empty() -> None:
    with pytest.raises(ValueError, match='Missing argument'):
        clone('foo', '')


class TestWithObject:
    def test_target_exists(self) -> None:
        with pytest.raises(
            ValueError, match='Module already exists: math'
        ):
            clone(calendar, 'math')

    def test_cloned_module(self) -> None:
        clone(calendar, 'cloned_calendar')
        assert 'cloned_calendar' in sys.modules
        import cloned_calendar  # type: ignore  # noqa: F401  # pylint: disable=import-error, import-outside-toplevel

        assert issubclass(
            cloned_calendar.LocaleTextCalendar, calendar.TextCalendar
        )
        locale_text_calendar = cloned_calendar.LocaleTextCalendar(
            locale='C'
        )
        assert locale_text_calendar.formatweekday(0, 3) == 'Mon'
        assert calendar.c is cloned_calendar.c
        expected = calendar.firstweekday()
        assert cloned_calendar.firstweekday() == expected
        calendar.setfirstweekday(6 - calendar.firstweekday())
        assert cloned_calendar.firstweekday() == 6 - expected
        cloned_calendar.setfirstweekday(
            6 - cloned_calendar.firstweekday()
        )
        assert calendar.firstweekday() == expected


class TestWithString:
    def test_target_exists(self) -> None:
        with pytest.raises(
            ValueError, match='Module already exists: math'
        ):
            clone('calendar', 'math')

    def test_cloned_module(self) -> None:
        clone('calendar', 'cloned_calendar')
        assert 'cloned_calendar' in sys.modules
        import cloned_calendar  # noqa: F401  # pylint: disable=import-error, import-outside-toplevel

        assert issubclass(
            cloned_calendar.LocaleTextCalendar, calendar.TextCalendar
        )
        locale_text_calendar = cloned_calendar.LocaleTextCalendar(
            locale='C'
        )
        assert locale_text_calendar.formatweekday(0, 3) == 'Mon'
        assert calendar.c is cloned_calendar.c
        expected = calendar.firstweekday()
        assert cloned_calendar.firstweekday() == expected
        calendar.setfirstweekday(6 - calendar.firstweekday())
        assert cloned_calendar.firstweekday() == 6 - expected
        cloned_calendar.setfirstweekday(
            6 - cloned_calendar.firstweekday()
        )
        assert calendar.firstweekday() == expected
