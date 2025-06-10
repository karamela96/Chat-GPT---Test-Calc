#!/usr/bin/env python3
"""Simple command-line calculator."""

import argparse
import operator
import sys


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument(
        "operation",
        choices=["add", "sub", "mul", "div"],
        help="Operation to perform",
    )
    parser.add_argument("x", type=float, help="First operand")
    parser.add_argument("y", type=float, help="Second operand")
    args = parser.parse_args()

    operations = {
        "add": operator.add,
        "sub": operator.sub,
        "mul": operator.mul,
        "div": operator.truediv,
    }

    try:
        result = operations[args.operation](args.x, args.y)
    except ZeroDivisionError:
        print("Error: Division by zero", file=sys.stderr)
        sys.exit(1)

    if result.is_integer():
        result = int(result)
    print(result)


if __name__ == "__main__":
    main()
