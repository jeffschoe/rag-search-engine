import string

from .search_utils import DEFAULT_SEARCH_LIMIT, load_movies, load_stopwords


def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    stopwords = preprocess_stopwords(load_stopwords())
    
    results = []

    query_tokens = remove_stopwords_from_list(preprocess_text(query), stopwords)
        #print(f'*** DEBUG QUERY:')
        #print(*preprocessed_query, sep='\n')

    for movie in movies:
        
        title_tokens = remove_stopwords_from_list(preprocess_text(movie["title"]), stopwords)
        
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
    lowered = text.lower()
    translation_table = str.maketrans("", "", string.punctuation)
    translated = lowered.translate(translation_table)
    tokenized_list = tokenize_text(translated)
    return tokenized_list

def tokenize_text(text: str) -> list[str]:
    split_text = text.split(' ') # split on whitespace
    empty_str_removed = [token for token in split_text if token != ""]
    return empty_str_removed

def preprocess_stopwords(stopwords: list[str]) -> list[str]:
    translation_table = str.maketrans("", "", string.punctuation)
    preprocessed_stopwords = [sw.lower().translate(translation_table) for sw in stopwords]
    return preprocessed_stopwords

def remove_stopwords_from_list(tokenized_list: list[str], stopwords_list: list[str]) -> list[str]:
    stopwords_removed_list = [token for token in tokenized_list if token not in stopwords_list]
    return stopwords_removed_list