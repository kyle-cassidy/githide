import argparse
from githide.add_command import add
from githide.init_command import init
from githide.list_command import list as list_files
from githide.remove_command import remove
from githide.undo_command import undo


def main():
    parser = argparse.ArgumentParser(description="GitHide CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a file to the hidden list")
    parser_add.add_argument("file", type=str, help="The file to add")

    # Init command
    subparsers.add_parser("init", help="Initialize the tool")

    # List command
    subparsers.add_parser("list", help="List all hidden files")

    # Remove command
    parser_remove = subparsers.add_parser(
        "remove", help="Remove a file from the hidden list"
    )
    parser_remove.add_argument("file", type=str, help="The file to remove")

    # Undo command
    subparsers.add_parser("undo", help="Undo the last hide operation")

    args = parser.parse_args()

    if args.command == "add":
        add(args.file)
    elif args.command == "init":
        init()
    elif args.command == "list":
        files = list_files()
        for file in files:
            print(file)
    elif args.command == "remove":
        remove(args.file)
    elif args.command == "undo":
        undo()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
