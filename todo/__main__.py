import argparse

from .todo import (
    add_todo,
    delete_todo,
    delete_all_todos,
    mark_todo_complete,
    mark_todo_uncomplete,
    show_todos,
)


def main():
    parser = argparse.ArgumentParser(description="Todo app")
    parser.add_argument("-a", "--add", type=str, help="add a new todo")
    parser.add_argument("-d", "--delete", type=int, help="delete a todo")
    parser.add_argument(
        "-da", "--delete_all", action="store_true", help="delete all todos"
    )
    parser.add_argument(
        "-c", "--complete", type=int, help="mark a todo as complete"
    )
    parser.add_argument(
        "-uc", "--uncomplete", type=int, help="mark a todo as incomplete"
    )
    parser.add_argument(
        "-s", "--show", action="store_true", help="show all todos"
    )

    args = parser.parse_args()

    if args.add:
        add_todo(args.add)
    elif args.delete:
        delete_todo(args.delete)
    elif args.delete_all:
        delete_all_todos()
    elif args.complete:
        mark_todo_complete(args.complete)
    elif args.uncomplete:
        mark_todo_uncomplete(args.uncomplete)
    elif args.show:
        show_todos()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
