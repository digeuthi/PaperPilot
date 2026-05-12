import json
from pathlib import Path
from typing import Dict, Optional, Tuple


def _normalize_text(text: Optional[str]) -> str:
    return text.strip() if isinstance(text, str) else ""


def _build_block(title: str, content: str, fallback: str) -> str:
    if content:
        return f"## {title}\n{content.strip()}\n\n"
    return f"## {title}\n{fallback}\n\n"


def _build_emphasis_points(summary_data: Dict[str, object]) -> str:
    results_summary = _normalize_text(summary_data.get("summaries", {}).get("results", ""))
    methods_summary = _normalize_text(summary_data.get("summaries", {}).get("methods", ""))
    discussion_summary = _normalize_text(summary_data.get("summaries", {}).get("discussion", ""))

    points = []
    if results_summary:
        points.append("- 주요 결과와 임팩트를 간결하게 전달하세요.")
    if methods_summary:
        points.append("- 사용된 방법의 핵심 차별점을 분명히 설명하세요.")
    if discussion_summary:
        points.append("- 저자의 주장과 한계점을 함께 제시하세요.")

    if not points:
        points.append("- 세부 정보를 확인하기 위해 원문 섹션을 다시 참조하세요.")

    return "\n".join(points)


def build_one_page_summary(summary_data: Dict[str, object], parsed_sections: Dict[str, object]) -> str:
    """Build a mock one-page study summary in Markdown format."""
    title = _normalize_text(parsed_sections.get("title", "제목 정보 없음"))
    abstract_summary = _normalize_text(summary_data.get("summaries", {}).get("abstract", ""))
    introduction_summary = _normalize_text(summary_data.get("summaries", {}).get("introduction", ""))
    methods_summary = _normalize_text(summary_data.get("summaries", {}).get("methods", ""))
    results_summary = _normalize_text(summary_data.get("summaries", {}).get("results", ""))
    discussion_summary = _normalize_text(summary_data.get("summaries", {}).get("discussion", ""))
    conclusion_summary = _normalize_text(summary_data.get("summaries", {}).get("conclusion", ""))

    research_background = introduction_summary or abstract_summary
    core_question = introduction_summary or abstract_summary
    claim = conclusion_summary or discussion_summary or "핵심 주장을 요약할 수 없습니다."
    limitations = discussion_summary or conclusion_summary or "한계점을 명확히 파악할 수 없습니다."

    markdown = [
        "# 임시 1장 요약(Mock One-Page Summary)",
        "*이 요약은 현재 Phase 5 Mock 생성입니다. 실제 OpenAI API 연결 시 내용이 업데이트됩니다.*",
        "",
        _build_block("논문 제목", title, "논문 제목을 추출할 수 없습니다."),
        _build_block(
            "핵심 연구 질문",
            f"{core_question}\n\n(이 내용은 섹션 요약을 기반으로 작성된 Mock 질문입니다.)" if core_question else "",
            "핵심 연구 질문을 추출할 수 없습니다."
        ),
        _build_block(
            "연구 배경",
            research_background,
            "연구 배경을 생성할 수 없습니다."
        ),
        _build_block(
            "사용한 방법",
            methods_summary,
            "사용한 방법을 생성할 수 없습니다."
        ),
        _build_block(
            "주요 결과",
            results_summary,
            "주요 결과를 생성할 수 없습니다."
        ),
        _build_block(
            "논문의 핵심 주장",
            claim,
            "논문의 핵심 주장을 생성할 수 없습니다."
        ),
        _build_block(
            "한계점 또는 추가 확인 필요 사항",
            limitations,
            "한계점 또는 추가 확인 필요 사항을 생성할 수 없습니다."
        ),
        "## 발표 시 강조할 포인트",
        _build_emphasis_points(summary_data),
    ]

    return "\n".join(markdown)


def save_one_page_summary(
    markdown_text: str,
    extracted_txt_path: Path,
    summary_data: Optional[Dict[str, object]] = None,
    summary_dir: str = "data/summaries",
) -> Tuple[Path, Path]:
    """Save one-page summary Markdown and optional JSON metadata to the summaries folder."""
    summary_dir_path = Path(summary_dir)
    summary_dir_path.mkdir(parents=True, exist_ok=True)

    base_name = extracted_txt_path.stem
    md_path = summary_dir_path / f"{base_name}_one_page_summary.md"
    json_path = summary_dir_path / f"{base_name}_one_page_summary.json"

    with md_path.open("w", encoding="utf-8") as md_file:
        md_file.write(markdown_text)

    json_payload = {
        "paper_title": _normalize_text(summary_data.get("paper_title", "")) if summary_data else "",
        "markdown_path": str(md_path),
        "summary_data": summary_data or {},
    }
    with json_path.open("w", encoding="utf-8") as json_file:
        json.dump(json_payload, json_file, ensure_ascii=False, indent=2)

    return md_path, json_path
