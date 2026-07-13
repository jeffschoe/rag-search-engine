import string

from .search_utils import DEFAULT_SEARCH_LIMIT, load_movies


def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []

    query_tokens = preprocess_text(query)
        #print(f'*** DEBUG QUERY:')
        #print(*preprocessed_query, sep='\n')

    for movie in movies:
        
        title_tokens = preprocess_text(movie["title"])
        #print(f'*** DEBUG TITLE:')
        #print(*preprocessed_title, sep='\n')

        if has_matching_tokens(query_tokens, title_tokens):
            results.append(movie)
            if len(results) >= limit:
                break

    return results

def has_matching_tokens(query_tokens: list[str], title_tokens: list[str]) -> bool:
    for query_token in query_tokens:
        for title_token in title_tokens:
            if query_token in title_token:
                return True
    return False

def preprocess_text(text: str) -> list[str]:
    #print(f'*** original = {text}')
    lowered = text.lower()
    #print(f'*** lowered = {lowered}')
    translation_table = str.maketrans("", "", string.punctuation)
    translated = lowered.translate(translation_table)
    #print(f'*** translated = {translated}') # punctuation is removed at this point
    tokenized_list = tokenize_text(translated)
    return tokenized_list


def tokenize_text(text: str) -> list[str]:
    split_text = text.split(' ') # split on whitespace
    empty_str_removed = [token for token in split_text if token != ""]
    return empty_str_removed

    