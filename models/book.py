from dataclasses import dataclass, asdict
from typing import List, Optional

@dataclass
class Book:
    title: str
    authors: List[str]
    year: Optional[int]
    categories: List[str]
    isbn: List[str]
    cover_url: Optional[str]
    info_url: Optional[str]

    def to_dict(self):
        return asdict(self)
