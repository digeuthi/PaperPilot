from pathlib import Path
from typing import Optional

ALLOWED_EXTENSIONS = {".pdf"}


def is_pdf_file(file_name: str) -> bool:
    return Path(file_name).suffix.lower() in ALLOWED_EXTENSIONS


def ensure_folder(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def get_unique_file_path(destination: Path) -> Path:
    if not destination.exists():
        return destination

    stem = destination.stem
    suffix = destination.suffix
    parent = destination.parent
    counter = 1

    while True:
        candidate = parent / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def save_uploaded_file(uploaded_file, upload_dir: str) -> Optional[Path]:
    upload_folder = Path(upload_dir)
    ensure_folder(upload_folder)

    file_name = Path(uploaded_file.name).name
    if not is_pdf_file(file_name):
        return None

    destination = upload_folder / file_name
    destination = get_unique_file_path(destination)

    try:
        with destination.open("wb") as f:
            f.write(uploaded_file.getbuffer())
        return destination
    except OSError:
        return None
