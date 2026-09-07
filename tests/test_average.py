import pytest
from decimal import Decimal
from fractions import Fraction

from mymath import average


def test_average_typical():
    data = [1, 2, 3, 4.5]
    expected = (1 + 2 + 3 + 4.5) / 4
    assert average(data) == pytest.approx(expected)


def test_average_single_element():
    # statistics.mean returns a float when given ints (division semantics),
    # so we assert against a float here.
    assert average([5]) == pytest.approx(5.0)


def test_average_negative_numbers():
    data = [-2, -4, 6]
    expected = (-2 + -4 + 6) / 3
    assert average(data) == pytest.approx(expected)


def test_average_empty_raises():
    with pytest.raises(ValueError):
        average([])


def test_average_non_numeric_raises():
    with pytest.raises(TypeError):
        # Incompatible types (str + int) should raise a TypeError during
        # arithmetic operations performed by statistics.mean / sum.
        average(["a", 1])


def test_average_generator():
    gen = (x for x in [1, 2, 3])
    assert average(gen) == pytest.approx(2.0)


def test_average_decimal_preserves_type():
    data = [Decimal("1.5"), Decimal("1.0")]
    expected = Decimal("1.25")
    assert average(data) == expected


def test_average_fraction_preserves_type():
    data = [Fraction(1, 2), Fraction(3, 2)]
    expected = Fraction(1, 1)
    assert average(data) == expected


def test_average_mixed_decimal_int():
    # Mixing Decimal and int is supported and should yield a Decimal result.
    data = [Decimal("1.5"), 1]
    expected = Decimal("1.25")
    assert average(data) == expected


def test_average_incompatible_types_raises():
    # Some numeric types are incompatible with one another (e.g., Decimal + Fraction)
    # and should raise a TypeError when combined.
    with pytest.raises(TypeError):
        average([Decimal("1.1"), Fraction(1, 2)])
