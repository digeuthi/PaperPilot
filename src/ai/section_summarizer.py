import json
import os
from pathlib import Path
from typing import Dict, List

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TARGET_SECTIONS = ["abstract", "introduction", "methods", "results", "discussion", "conclusion"]


def _mock_summary(section_name: str, section_text: str) -> str:
    preview = " ".join(section_text.strip().split())[:180]
    return (
        f"임시 요약 (Mock Summary) [{section_name.title()}]: "
        f"이 섹션은 실제 AI 요약으로 교체될 수 있습니다. 주요 내용 미리보기: {preview}"
    )


def build_section_summaries(parsed_sections: Dict[str, object]) -> Dict[str, object]:
    summaries: Dict[str, str] = {}
    missing_sections: List[str] = []

    for section_key in TARGET_SECTIONS:
        raw_text = parsed_sections.get("sections", {}).get(section_key, "")
        section_text = raw_text.strip() if isinstance(raw_text, str) else ""

        if not section_text:
            summaries[section_key] = ""
            missing_sections.append(section_key)
            continue

        # 현재는 실제 OpenAI API 호출을 연결하지 않은 상태입니다.
        # 추후 OPENAI_API_KEY가 있는 경우 이 함수 내부에 실제 호출 로직을 추가할 수 있습니다.
        summaries[section_key] = _mock_summary(section_key, section_text)

    return {
        "paper_title": parsed_sections.get("title", ""),
        "summaries": summaries,
        "missing_sections": missing_sections,
        "is_mock": True,
    }


def save_section_summaries(summary_data: Dict[str, object], extracted_txt_path: Path, summary_dir: str = "data/summaries") -> Path:
    output_folder = Path(summary_dir)
    output_folder.mkdir(parents=True, exist_ok=True)
    output_path = output_folder / f"{extracted_txt_path.stem}_section_summaries.json"

    with output_path.open("w", encoding="utf-8") as output_file:
        json.dump(summary_data, output_file, ensure_ascii=False, indent=2)

    return output_path
