import argparse

from todos import db


def build_arg_parser():
    parser = argparse.ArgumentParser(
        description="Command-line tool to track and manage todos"
    )
    subparsers = parser.add_subparsers(dest="command")

    add_todo_parser = subparsers.add_parser("add", help="Add a new todo")
    add_todo_parser.add_argument("name", type=str, help="Name of the todo")

    update_todo_parser = subparsers.add_parser("update", help="Update a todo")
    update_todo_parser.add_argument("id", type=int, help="Id of the todo")
    update_todo_parser.add_argument(
        "--name", type=str, required=True, help="New name of the todo"
    )

    mark_todo_done_parser = subparsers.add_parser("done", help="Mark a todo as done")
    mark_todo_done_parser.add_argument("id", type=int, help="Id of the todo")

    delete_todo_parser = subparsers.add_parser("delete", help="Delete a todo")
    delete_todo_parser.add_argument("id", type=int, help="Id of the todo")

    _list_todo_parser = subparsers.add_parser("list", help="List all todos")

    return parser


def handle_add(args: argparse.Namespace):
    affected_rowcount = db.add_todo(args.name)

    if affected_rowcount == 1:
        print("Todo Added!")
    else:
        print("Something went wrong!")


def handle_update(args: argparse.Namespace):
    affected_rowcount = db.update_todo_name(args.id, args.name)

    if affected_rowcount == 1:
        print("Todo Updated!")
    else:
        print("Please enter valid id.")


def handle_done(args: argparse.Namespace):
    affected_rowcount = db.update_todo_is_done(args.id, True)

    if affected_rowcount == 1:
        print("Todo marked as done!")
    else:
        print("Please enter valid id.")


def handle_delete(args: argparse.Namespace):
    affected_rowcount = db.delete_todo(args.id)

    if affected_rowcount == 0:
        print("Please Enter valid id.")
    elif affected_rowcount == 1:
        print("Todo Deleted!")
    else:
        print("Something went wrong!")


def handle_list(_: argparse.Namespace):
    todos = db.get_todos()

    for todo in todos:
        mark = "✔" if todo["is_done"] else "✗"
        print("%s %d %-30s" % (mark, todo["id"], todo["name"]))


def main():
    db.init_db()
    arg_parser = build_arg_parser()

    args = arg_parser.parse_args()
    handlers = {
        "add": handle_add,
        "update": handle_update,
        "done": handle_done,
        "delete": handle_delete,
        "list": handle_list,
    }

    if args.command in handlers:
        handler = handlers[args.command]
        handler(args)
    else:
        print(arg_parser.format_help())
