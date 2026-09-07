from typing import Iterable
from numbers import Real
import statistics
from statistics import StatisticsError


def average(numbers: Iterable[Real]) -> Real:
    """Return the arithmetic mean of an iterable of real numbers.

    This function accepts any iterable of numeric types that register with
    the Real ABC (ints, floats, Decimal, Fraction, etc.). It consumes the
    iterable (so generators are supported) and preserves numeric type where
    possible — e.g., averaging Decimal values returns a Decimal, averaging
    Fraction values returns a Fraction. For plain ints/floats the result
    follows normal Python numeric promotion (typically a float).

    Parameters
    ----------
    numbers:
        An iterable of real numbers.

    Returns
    -------
    Real
        The arithmetic mean. The precise returned numeric type depends on the
        input types (Decimal/Fraction inputs typically produce Decimal/Fraction
        results, respectively).

    Raises
    ------
    ValueError
        If `numbers` is empty.
    TypeError
        If elements of `numbers` are not numeric or are of incompatible
        types such that arithmetic operations fail.
    """
    try:
        # statistics.mean accepts any iterable and will raise StatisticsError
        # for empty inputs; it also preserves numeric types where possible.
        return statistics.mean(numbers)
    except StatisticsError:
        raise ValueError("numbers must not be empty")
