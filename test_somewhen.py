import datetime
from copy import copy, deepcopy

import pytest

from somewhen import Somewhen, Somedate, Sometime


def test_somewhen_is_a_datetime():
    assert isinstance(Somewhen(), datetime.datetime)


def test_somewhen_is_a_somewhen():
    assert isinstance(Somewhen(), Somewhen)


def test_somewhen_is_exactly_the_same_as_any_other_somewhen():
    assert Somewhen() is Somewhen()


def test_somewhen_is_equally_to_somewhen():
    assert Somewhen() == Somewhen()


def test_copying_somewhen_is_still_somewhen():
    assert copy(Somewhen()) is Somewhen()


def test_deep_copying_somewhen_is_still_somewhen():
    assert deepcopy(Somewhen()) is Somewhen()


def test_somewhen_is_never_the_same_as_a_specific_date():
    some_date = datetime.datetime(year=2000, month=1, day=1, hour=1, minute=1, second=1, microsecond=0, tzinfo=None)
    assert Somewhen() != some_date


def test_somewhen_is_not_after_a_date():
    the_past = datetime.datetime.now() - datetime.timedelta(days=1)
    assert not the_past < Somewhen()


def test_somewhen_is_not_before_a_date():
    the_past = datetime.datetime.now() - datetime.timedelta(days=1)
    assert not the_past > Somewhen()


def test_somewhen_is_less_than_or_equal_to_itself_though():
    assert Somewhen() >= Somewhen()


def test_somewhen_is_also_greater_than_or_equal_to_itself_though():
    assert Somewhen() <= Somewhen()


def test_a_day_after_somewhen_is_somewhen():
    assert (Somewhen() + datetime.timedelta(days=1)) == Somewhen()


def test_a_day_before_somewhen_is_somewhen():
    assert (Somewhen() - datetime.timedelta(days=1)) == Somewhen()


def test_it_looks_appropriate_as_a_string():
    assert str(Somewhen()) == "somewhen :shrug:"


def test_it_looks_appropriate_as_a_repr():
    assert repr(Somewhen()) == "Somewhen()"


@pytest.mark.parametrize("attribute", ["year", "month", "day", "hour", "minute", "second", "microsecond"])
def test_that_you_cant_find_out_when_somewhen_is_from_attributes(attribute):
    with pytest.raises(RuntimeError):
        getattr(Somewhen(), attribute)


def test_somewhen_is_on_some_date():
    assert (Somewhen()).date() is Somedate()


def test_somewhen_is_at_some_time():
    assert (Somewhen()).time() is Sometime()
