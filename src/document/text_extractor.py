from pathlib import Path
from typing import Optional

import fitz


def ensure_folder(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def extract_text_from_pdf(pdf_path: Path) -> str:
    document = fitz.open(str(pdf_path))
    text_parts = []

    for page in document:
        text_parts.append(page.get_text())

    return "\n".join(text_parts).strip()


def save_extracted_text(text: str, destination: Path) -> Path:
    ensure_folder(destination.parent)
    with destination.open("w", encoding="utf-8") as f:
        f.write(text)
    return destination


def extract_text_from_pdf_file(pdf_path: str, extracted_dir: str = "data/extracted") -> Optional[Path]:
    source_path = Path(pdf_path)
    if not source_path.exists():
        return None

    extracted_folder = Path(extracted_dir)
    ensure_folder(extracted_folder)

    extracted_file_path = extracted_folder / f"{source_path.stem}.txt"

    try:
        text = extract_text_from_pdf(source_path)
        save_extracted_text(text, extracted_file_path)
        return extracted_file_path
    except Exception:
        return None
