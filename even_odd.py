#!/usr/bin/env python3
import argparse


def is_even(x: int) -> bool:
    """Return True if a number is even."""
    return x % 2 == 0


def is_odd(x: int) -> bool:
    """Return True if a number is odd."""
    return not is_even(x)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('x', type=float)
    args = parser.parse_args()

    evenodd = 'odd'
    if is_even(args.x):
        evenodd = 'even'

    print(f'The number {args.x} is {evenodd}')


if __name__ == '__main__':
    main()
