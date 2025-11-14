import argparse

from contacts.core import add_contact, delete_contact, print_contacts, search_contacts
from contacts.storage import load_contacts


def build_arg_parser():
    parser = argparse.ArgumentParser(
        description="Manage your contacts - add, search & delete."
    )
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add new contact")
    add_parser.add_argument("name", type=str, help="Contact Name")
    add_parser.add_argument("--phone", type=str, help="Contact Phone number")
    add_parser.add_argument("--email", type=str, help="Contact Email")

    search_parser = subparsers.add_parser("search", help="Search contacts")
    search_parser.add_argument("name", type=str, help="Contact Name")

    _list_parser = subparsers.add_parser("list", help="List all contacts")

    delete_parser = subparsers.add_parser("delete", help="Delete a contact by id")
    delete_parser.add_argument("id", type=int, help="Contact's Id")

    return parser


def handle_contact_add(args: argparse.Namespace):
    add_contact(name=args.name, phone=args.phone, email=args.email)


def handle_contact_search(args: argparse.Namespace):
    contacts = search_contacts(query=args.name)
    print_contacts(contacts)
    print()


def handle_contact_list(_: argparse.Namespace):
    contacts = load_contacts()

    if len(contacts) > 0:
        print_contacts(contacts)
        print()


def handle_contact_delete(args: argparse.Namespace):
    deleted = delete_contact(args.id)

    if not deleted:
        print("Please enter valid Id!")
    else:
        print("Contact Deleted!")


def main():
    arg_parser = build_arg_parser()
    args = arg_parser.parse_args()

    handlers = {
        "add": handle_contact_add,
        "search": handle_contact_search,
        "list": handle_contact_list,
        "delete": handle_contact_delete,
    }

    if args.command in handlers.keys():
        handler = handlers[args.command]
        handler(args)
    else:
        print(arg_parser.format_help())
