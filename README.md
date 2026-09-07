mymath
======

A tiny utility package that provides a single function `average(numbers)` to
compute the arithmetic mean of an iterable of numbers.

Behavior
--------
- Accepts any iterable of numeric types that implement the Real ABC (ints,
  floats, Decimal, Fraction, etc.). Generators and other non-sized iterables
  are supported (the iterable will be consumed).
- Returns the arithmetic mean. The precise return numeric type depends on the
  input types: averaging Decimal objects typically returns a Decimal, likewise
  Fraction inputs produce a Fraction. For plain ints/floats the result will
  follow normal Python numeric promotion (commonly a float).
- Raises ValueError("numbers must not be empty") if the input iterable is
  empty.
- If elements are of incompatible or non-numeric types, Python arithmetic
  operations will raise a TypeError.

Example
-------

from mymath import average

print(average([1, 2, 3]))  # 2.0

Running tests
-------------

Install pytest if needed, then run:

pytest -q
