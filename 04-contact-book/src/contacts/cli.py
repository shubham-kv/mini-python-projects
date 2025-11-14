import argparse

from contacts.core import add_contact


def build_arg_parser():
    parser = argparse.ArgumentParser(
        description="Manage your contacts - add, search & delete."
    )
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add new contact")
    add_parser.add_argument("name", type=str, help="Contact Name")
    add_parser.add_argument("--phone", type=str, help="Contact Phone number")
    add_parser.add_argument("--email", type=str, help="Contact Email")

    return parser


def handle_contact_add(args: argparse.Namespace):
    add_contact(name=args.name, phone=args.phone, email=args.email)


def main():
    arg_parser = build_arg_parser()
    args = arg_parser.parse_args()

    handlers = {
        "add": handle_contact_add,
    }

    if args.command in handlers.keys():
        handler = handlers[args.command]
        handler(args)
    else:
        print(arg_parser.format_help())
