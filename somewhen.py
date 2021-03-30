import datetime


class Somewhen(datetime.datetime):
    _singleton = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = datetime.datetime.__new__(cls, year=2000, month=1, day=1, hour=1, minute=1, second=1, microsecond=0, tzinfo=None)
        return cls._singleton

    def __eq__(self, other):
        return other is self

    def __ne__(self, other):
        return other is not self

    def __le__(self, other):
        return self is other

    def __lt__(self, other):
        return False

    def __gt__(self, other):
        return False

    def __ge__(self, other):
        return self is other

    def __add__(self, other):
        if not isinstance(other, datetime.timedelta):
            return NotImplemented
        return self

    def __sub__(self, other):
        if not isinstance(other, datetime.timedelta):
            return NotImplemented
        return self

    def __str__(self):
        return "somewhen :shrug:"

    def __repr__(self):
        return "Somewhen()"

    def __deepcopy__(self, memodict={}):
        return self

    def __copy__(self):
        return self
