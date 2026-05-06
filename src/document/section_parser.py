import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

SECTION_ORDER = [
    "abstract",
    "introduction",
    "methods",
    "results",
    "discussion",
    "conclusion",
    "references",
]

SECTION_PATTERNS: List[Tuple[List[str], re.Pattern]] = [
    (
        ["abstract"],
        re.compile(
            r'^\s*(?:\d+\.?\s*|[ivxlcdm]+\.?\s*)?(?:abstract|summary)(?:\b.*)?\s*[:\-]?\s*(.*)$',
            re.I,
        ),
    ),
    (
        ["introduction"],
        re.compile(
            r'^\s*(?:\d+\.?\s*|[ivxlcdm]+\.?\s*)?(?:introduction|background)(?:\b.*)?\s*[:\-]?\s*(.*)$',
            re.I,
        ),
    ),
    (
        ["methods"],
        re.compile(
            r'^\s*(?:\d+\.?\s*|[ivxlcdm]+\.?\s*)?(?:materials and methods|materials & methods|materials\/methods|experimental procedures|methodology|methods)(?:\b.*)?\s*[:\-]?\s*(.*)$',
            re.I,
        ),
    ),
    (
        ["results"],
        re.compile(
            r'^\s*(?:\d+\.?\s*|[ivxlcdm]+\.?\s*)?(?:results|findings)(?:\b.*)?\s*[:\-]?\s*(.*)$',
            re.I,
        ),
    ),
    (
        ["discussion"],
        re.compile(
            r'^\s*(?:\d+\.?\s*|[ivxlcdm]+\.?\s*)?(?:discussion)(?:\b.*)?\s*[:\-]?\s*(.*)$',
            re.I,
        ),
    ),
    (
        ["results", "discussion"],
        re.compile(
            r'^\s*(?:\d+\.?\s*|[ivxlcdm]+\.?\s*)?(?:results and discussion|results & discussion)(?:\b.*)?\s*[:\-]?\s*(.*)$',
            re.I,
        ),
    ),
    (
        ["discussion", "conclusion"],
        re.compile(
            r'^\s*(?:\d+\.?\s*|[ivxlcdm]+\.?\s*)?(?:discussion and conclusion|discussion & conclusion|discussion and conclusions|discussion & conclusions)(?:\b.*)?\s*[:\-]?\s*(.*)$',
            re.I,
        ),
    ),
    (
        ["conclusion"],
        re.compile(
            r'^\s*(?:\d+\.?\s*|[ivxlcdm]+\.?\s*)?(?:conclusion|conclusions)(?:\b.*)?\s*[:\-]?\s*(.*)$',
            re.I,
        ),
    ),
    (
        ["references"],
        re.compile(
            r'^\s*(?:\d+\.?\s*|[ivxlcdm]+\.?\s*)?(?:references|bibliography|reference)(?:\b.*)?\s*[:\-]?\s*(.*)$',
            re.I,
        ),
    ),
]


def _find_section_headings(lines: List[str]) -> List[Dict[str, object]]:
    headings = []

    for index, line in enumerate(lines):
        normalized_line = line.strip()
        if not normalized_line:
            continue

        for section_keys, pattern in SECTION_PATTERNS:
            match = pattern.match(normalized_line)
            if not match:
                continue

            body_after_heading = match.group(1).strip() if match.groups() else ""
            headings.append(
                {
                    "section_keys": section_keys,
                    "index": index,
                    "body_after": body_after_heading,
                }
            )
            break

    return headings


def _extract_title(lines: List[str], headings: List[Dict[str, object]]) -> str:
    if not lines:
        return ""

    first_heading_index = min((heading["index"] for heading in headings), default=len(lines))

    for index, line in enumerate(lines[:first_heading_index]):
        cleaned = line.strip()
        if cleaned:
            return cleaned

    return ""


def _build_section_texts(lines: List[str], headings: List[Dict[str, object]]) -> Dict[str, str]:
    section_texts = {section: "" for section in SECTION_ORDER}
    if not headings:
        return section_texts

    expanded_headings = []
    for heading in headings:
        for key in heading["section_keys"]:
            expanded_headings.append(
                {
                    "section": key,
                    "index": heading["index"],
                    "body_after": heading["body_after"],
                }
            )

    expanded_headings.sort(key=lambda item: item["index"])

    for idx, heading in enumerate(expanded_headings):
        section_key = heading["section"]
        start_index = heading["index"] + 1
        end_index = expanded_headings[idx + 1]["index"] if idx + 1 < len(expanded_headings) else len(lines)
        content_lines = []

        if heading["body_after"]:
            content_lines.append(heading["body_after"])

        content_lines.extend(line for line in lines[start_index:end_index])
        section_texts[section_key] = "\n".join(content_lines).strip()

    return section_texts


def extract_paper_sections(text: str) -> Dict[str, object]:
    lines = text.splitlines()
    headings = _find_section_headings(lines)
    title = _extract_title(lines, headings)
    section_texts = _build_section_texts(lines, headings)

    if not any(section_texts.values()):
        fallback_title = title or lines[0].strip() if lines else ""
        fallback_body = "\n".join(lines[1:]).strip() if len(lines) > 1 else ""
        section_texts["introduction"] = fallback_body or text.strip()
        title = fallback_title

    missing_sections = [
        section for section, content in section_texts.items() if not content.strip()
    ]

    result = {
        "title": title,
        "sections": section_texts,
        "missing_sections": missing_sections,
    }
    return result


def save_sections_json(parsed_sections: Dict[str, object], extracted_txt_path: Path) -> Path:
    output_folder = extracted_txt_path.parent
    output_folder.mkdir(parents=True, exist_ok=True)

    output_path = output_folder / f"{extracted_txt_path.stem}_sections.json"
    with output_path.open("w", encoding="utf-8") as output_file:
        json.dump(parsed_sections, output_file, ensure_ascii=False, indent=2)

    return output_path
