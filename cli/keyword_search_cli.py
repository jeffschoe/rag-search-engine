import argparse
import json
import os

from lib.keyword_search import search_command


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI") # creates CLI
    subparsers = parser.add_subparsers(dest="command", help="Available commands") # allows commands

    search_parser = subparsers.add_parser("search", help="Search movies using keywords") # defines 'search' command
    search_parser.add_argument("query", type=str, help="Search query") # define arguments 'search' needs

    args = parser.parse_args() # capture user input

    abs_file_path = os.path.abspath("./data/movies.json")
    match args.command:
        case "search":
            print(f'Searching for: {args.query}')
            results = search_command(args.query)
            for i, res in enumerate(results, 1):
                print(f'{i}. {res['title']}')         

        case _:
            parser.print_help()

if __name__ == "__main__":
    main()