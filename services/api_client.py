import requests
from config import BASE_URL, SEARCH_ENDPOINT, SUBJECT_ENDPOINT, REQUEST_TIMEOUT

class OpenLibraryClient:
    def __init__(self):
        self.session = requests.Session()

    def search_books(self, query: str, limit: int = 10):
        response = self.session.get(
            f"{BASE_URL}{SEARCH_ENDPOINT}",
            params={"q": query, "limit": limit},
            timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()
        return response.json()

    def get_books_by_subject(self, subject: str, limit: int = 10):
        response = self.session.get(
            f"{BASE_URL}{SUBJECT_ENDPOINT.format(subject=subject.lower())}",
            params={"limit": limit},
            timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()
        return response.json()