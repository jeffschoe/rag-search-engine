import string

from .search_utils import DEFAULT_SEARCH_LIMIT, STOPWORDS_PATH, load_movies
from nltk.stem import PorterStemmer

def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []

    query_tokens = tokenize_text(query)
        #print(f'*** DEBUG QUERY:')
        #print(*preprocessed_query, sep='\n')

    for movie in movies:
        
        title_tokens = tokenize_text(movie["title"])
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

def preprocess_text(text: str) -> str:
    lowered = text.lower()
    translation_table = str.maketrans("", "", string.punctuation)
    translated = lowered.translate(translation_table) # removes punctuation
    return translated

def load_stopwords() -> list[str]:
    with open(STOPWORDS_PATH, "r") as f:
        return [preprocess_text(word) for word in f.read().splitlines()]


STOPWORDS = load_stopwords()
stemmer = PorterStemmer()

def tokenize_text(text: str) -> list[str]:
    text = preprocess_text(text)
    tokens = text.split() # splits on any whitespace (spaces, tabs, newlines)
    valid_tokens = [token for token in tokens if token] # removes empty tokens
    filtered_words = [word for word in valid_tokens if word not in STOPWORDS] # removes stopwords
    stemmed_words = [stemmer.stem(word) for word in filtered_words]
    return stemmed_words
