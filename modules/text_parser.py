from pathlib import Path
from typing import List

def parse_items_from_text_file(path: str) -> List[str]:
    raw_text = Path(path).read_text(encoding="utf-8")
    return [item.strip() for item in raw_text.split("\n\n") if item.strip()]

