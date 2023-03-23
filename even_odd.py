#!/usr/bin/env python3
def is_even(x: int) -> bool:
    """Return True if a number is even."""
    return x % 2 == 0


def is_odd(x: int) -> bool:
    """Return True if a number is odd."""
    return not is_even(x)
