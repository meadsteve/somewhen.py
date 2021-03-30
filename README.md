# somewhen.py
Dates and times are hard. Just don't bother.

Somewhen is vague.
```python
date_one = Somewhen()
date_two = date_one + datetime.timedelta(days=1)

assert date_one == date_two
```

Somewhen is compatible:

```python
assert isinstance(date_one, datetime.datetime)
```

Somwhen is neither future nor past

```python
assert not Somewhen() > datetime.datetime.now()
assert not Somewhen() < datetime.datetime.now()
```

But somewhen is also not now

```python
assert not Somewhen() == datetime.datetime.now()
```
