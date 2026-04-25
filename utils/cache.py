import json
import os
from typing import Dict, Any

class CacheManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

    def save(self, data: Dict[str, Any]) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.file_path):
            return {}

        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
