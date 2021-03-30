import datetime
from copy import copy, deepcopy

from somewhen import Somewhen


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

