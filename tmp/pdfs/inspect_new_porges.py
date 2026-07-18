from __future__ import annotations

import json
from pathlib import Path

from pypdf import PdfReader


path = Path(
    r"C:\Users\MARIO\Libro Emozioni\fonti\biblioteca\divulgazione"
    r"\The Polyvagal Theory_ Neurophys - Stephen W. Porges.pdf"
)
reader = PdfReader(path)
metadata = reader.metadata or {}
counts = []
selected = {}

for index, page in enumerate(reader.pages):
    text = " ".join((page.extract_text() or "").split())
    counts.append(len(text))
    if index < 25 or index >= len(reader.pages) - 5:
        selected[index + 1] = text[:3000]

record = {
    "file": path.name,
    "size_bytes": path.stat().st_size,
    "pages": len(reader.pages),
    "encrypted": reader.is_encrypted,
    "metadata": {str(key): str(value) for key, value in metadata.items()},
    "searchable_pages": sum(value >= 20 for value in counts),
    "near_empty_pages": sum(value < 20 for value in counts),
    "coverage_pct": round(100 * sum(value >= 20 for value in counts) / len(counts), 1),
    "total_extracted_characters": sum(counts),
    "selected_pages": selected,
}

print(json.dumps(record, ensure_ascii=False, indent=2))
