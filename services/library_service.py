from collections import defaultdict
from typing import Dict, List
from models.book import Book
from services.api_client import OpenLibraryClient

class LibraryService:
    def __init__(self):
        self.client = OpenLibraryClient()

    def build_book(self, raw_book: dict) -> Book:
        cover_id = raw_book.get('cover_i') or raw_book.get('cover_id')
        cover_url = (
            f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
            if cover_id else None
        )

        key = raw_book.get('key', '')
        info_url = f"https://openlibrary.org{key}" if key else None

        return Book(
            title=raw_book.get('title', 'Sin título'),
            authors=raw_book.get('author_name', ['Autor desconocido']),
            year=raw_book.get('first_publish_year'),
            categories=raw_book.get('subject', [])[:5],
            isbn=raw_book.get('isbn', [])[:3],
            cover_url=cover_url,
            info_url=info_url
        )

    def get_books_by_categories(self, categories: List[str], limit: int = 10) -> Dict[str, List[Book]]:
        library = defaultdict(list)

        for category in categories:
            try:
                data = self.client.get_books_by_subject(category, limit)
                works = data.get('works', [])

                for work in works:
                    library[category].append(self.build_book(work))
            except Exception as error:
                print(f"Error al obtener categoría '{category}': {error}")

        return dict(library)
