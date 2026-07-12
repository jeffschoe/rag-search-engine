import argparse
import json
import os

DEFAULT_SEARCH_LIMIT = 5

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

            processed_query = args.query.lower()
            
            results = []

            with open (abs_file_path,"r") as read_content:
                movies_json: dict = json.load(read_content)

            movies_dict = movies_json["movies"]
            for movie in movies_dict:
                movie_title = movie["title"]
                if processed_query in movie_title.lower():
                    results.append(movie_title)
            
         
            for i, res in enumerate(results, 1):
                if i > DEFAULT_SEARCH_LIMIT: break
                print(f'{i}. Movie Title: {res}')
            


        case _:
            parser.print_help()

if __name__ == "__main__":
    main()