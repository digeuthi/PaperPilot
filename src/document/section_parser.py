import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

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
            r'^\s*(?:\d+\.?\s*|[ivxlcdm]+\.?\s*)?(?:materials and methods|materials & methods|materials\/methods|methods and materials|methods|experimental procedures|methodology)(?:\b.*)?\s*[:\-]?\s*(.*)$',
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
        ["conclusion"],
        re.compile(
            r'^\s*(?:\d+\.?\s*|[ivxlcdm]+\.?\s*)?(?:conclusion|conclusions|summary and conclusion|final remarks|closing remarks)(?:\b.*)?\s*[:\-]?\s*(.*)$',
            re.I,
        ),
    ),
    (
        ["references"],
        re.compile(
            r'^\s*(?:\d+\.?\s*|[ivxlcdm]+\.?\s*)?(?:references|reference|bibliography|literature cited|citations|references and notes|reference list)(?:\b.*)?\s*[:\-]?\s*(.*)$',
            re.I,
        ),
    ),
]

REFERENCE_ENTRY_PATTERN = re.compile(r'^\s*(?:\[\d+\]|\d+\.)\s+[A-Z][A-Za-z\-]+,')


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


def _extract_title(lines: List[str], headings: List[Dict[str, object]]) -> Tuple[str, int]:
    if not lines:
        return "", -1

    first_heading_index = min((heading["index"] for heading in headings), default=len(lines))

    for index, line in enumerate(lines[:first_heading_index]):
        cleaned = line.strip()
        if cleaned:
            return cleaned, index

    return "", -1


def _looks_like_reference_entry(line: str) -> bool:
    return bool(REFERENCE_ENTRY_PATTERN.match(line.strip()))


def _trim_reference_tail(text: str) -> Tuple[str, str]:
    lines = text.splitlines()
    reference_start = None

    for index, line in enumerate(lines):
        if _looks_like_reference_entry(line):
            reference_start = index
            break

    if reference_start is None or reference_start == 0:
        return text, ""

    reference_lines = lines[reference_start:]
    if len(reference_lines) < 2:
        return text, ""

    return "\n".join(lines[:reference_start]).strip(), "\n".join(reference_lines).strip()


def _assign_implicit_abstract(lines: List[str], headings: List[Dict[str, object]], section_texts: Dict[str, str], title_index: int) -> None:
    if section_texts.get("abstract"):
        return

    intro_indices = [heading["index"] for heading in headings if "introduction" in heading["section_keys"]]
    if not intro_indices:
        return

    intro_index = intro_indices[0]
    start_index = title_index + 1 if title_index >= 0 else 0
    candidate_lines = [line.strip() for line in lines[start_index:intro_index] if line.strip()]
    candidate_text = " ".join(candidate_lines).strip()

    if 30 <= len(candidate_text) <= 1200 and len(candidate_text.split()) <= 250:
        section_texts["abstract"] = candidate_text


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
        end_index = len(lines)

        for next_heading in expanded_headings[idx + 1:]:
            if next_heading["index"] != heading["index"]:
                end_index = next_heading["index"]
                break

        content_lines = []
        if heading["body_after"]:
            content_lines.append(heading["body_after"])

        content_lines.extend(line for line in lines[start_index:end_index])
        section_texts[section_key] = "\n".join(content_lines).strip()

    return section_texts


def extract_paper_sections(text: str) -> Dict[str, object]:
    lines = text.splitlines()
    headings = _find_section_headings(lines)
    title, title_index = _extract_title(lines, headings)
    section_texts = _build_section_texts(lines, headings)

    _assign_implicit_abstract(lines, headings, section_texts, title_index)

    if not any(section_texts.values()):
        fallback_title = title or lines[0].strip() if lines else ""
        fallback_body = "\n".join(lines[1:]).strip() if len(lines) > 1 else ""
        section_texts["introduction"] = fallback_body or text.strip()
        title = fallback_title

    if not any(heading for heading in headings if "references" in heading["section_keys"]):
        for section_key in ["methods", "results", "discussion", "conclusion", "introduction", "abstract"]:
            section_text, reference_tail = _trim_reference_tail(section_texts.get(section_key, ""))
            if reference_tail:
                section_texts[section_key] = section_text
                existing_references = section_texts.get("references", "")
                section_texts["references"] = "\n".join(filter(None, [existing_references, reference_tail])).strip()
                break

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
