import argparse
from calc.core import add, floor_division, subtract, multiply, divide, modulo, exponent

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "**": exponent,
    "/": divide,
    "//": floor_division,
    "%": modulo,
}


def build_arg_parser():
    parser = argparse.ArgumentParser(description="A simple CLI calculator")

    parser.add_argument("x", type=float, help="First number")
    parser.add_argument(
        "operator",
        choices=["+", "-", "*", "**", "/", "//", "%"],
        help="Operation to perform",
    )
    parser.add_argument("y", type=float, help="Second number")

    return parser


def process_command(args: argparse.Namespace):
    if args.operator not in operations:
        print("Unsupported opeartion '%s'!\n" % args.operator)
        return

    result: float
    operation = operations[args.operator]

    try:
        result = operation(args.x, args.y)
    except ZeroDivisionError:
        print("Cannot divide by zero!\n")
    else:
        print(result)


def main():
    parser = build_arg_parser()
    args = parser.parse_args()
    process_command(args)
