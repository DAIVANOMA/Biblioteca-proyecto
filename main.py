import requests
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
from collections import defaultdict
import json
import time


@dataclass
class Book:
    title: str
    authors: List[str]
    year: Optional[int]
    subjects: List[str]
    isbn: List[str]
    cover_url: Optional[str]
    openlibrary_url: Optional[str]


class DigitalLibrary:
    BASE_URL = "https://openlibrary.org/search.json"

    def __init__(self):
        self.catalog: Dict[str, List[Book]] = defaultdict(list)
        self.cache: Dict[str, List[Book]] = {}

    def search_books(self, query: str, limit: int = 20) -> List[Book]:
        if query in self.cache:
            return self.cache[query]

        params = {
            "q": query,
            "limit": limit,
            "fields": "title,author_name,first_publish_year,subject,isbn,cover_i,key"
        }

        response = requests.get(self.BASE_URL, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        books = []
        for doc in data.get("docs", []):
            book = Book(
                title=doc.get("title", "Unknown Title"),
                authors=doc.get("author_name", ["Unknown Author"]),
                year=doc.get("first_publish_year"),
                subjects=doc.get("subject", [])[:5],
                isbn=doc.get("isbn", [])[:3],
                cover_url=(
                    f"https://covers.openlibrary.org/b/id/{doc['cover_i']}-L.jpg"
                    if doc.get("cover_i") else None
                ),
                openlibrary_url=(
                    f"https://openlibrary.org{doc['key']}"
                    if doc.get("key") else None
                )
            )
            books.append(book)

        self.cache[query] = books
        return books

    def categorize_books(self, books: List[Book]) -> None:
        for book in books:
            category = book.subjects[0] if book.subjects else "General"
            self.catalog[category].append(book)

    def build_library(self, topics: List[str], books_per_topic: int = 10) -> None:
        for topic in topics:
            print(f"Fetching books for: {topic}")
            books = self.search_books(topic, books_per_topic)
            self.categorize_books(books)
            time.sleep(1)

    def export_to_json(self, filename: str = "library_catalog.json") -> None:
        export_data = {
            category: [asdict(book) for book in books]
            for category, books in self.catalog.items()
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(export_data, f, indent=4, ensure_ascii=False)

        print(f"Library exported to {filename}")

    def display_summary(self) -> None:
        print("\n=== DIGITAL LIBRARY SUMMARY ===")
        for category, books in self.catalog.items():
            print(f"\n📚 {category} ({len(books)} books)")
            for book in books[:3]:
                authors = ", ".join(book.authors[:2])
                print(f"  - {book.title} | {authors} | {book.year}")


if __name__ == "__main__":
    topics = [
        "Python Programming",
        "Artificial Intelligence",
        "Data Science",
        "Software Engineering",
        "Cybersecurity"
    ]

    library = DigitalLibrary()
    library.build_library(topics, books_per_topic=12)
    library.display_summary()
    library.export_to_json()
