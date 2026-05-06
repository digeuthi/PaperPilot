import streamlit as st
from src.ai.section_summarizer import build_section_summaries, save_section_summaries
from src.document.section_parser import extract_paper_sections, save_sections_json
from src.document.text_extractor import extract_text_from_pdf_file
from src.storage.file_storage import save_uploaded_file

st.set_page_config(page_title="PaperPilot", page_icon="📄", layout="centered")

st.title("PaperPilot")
st.markdown(
    """
    PaperPilot은 논문 분석 및 발표자료 구성 보조를 목표로 하는 MVP입니다.

    이 Phase 4 버전에서는 PDF 업로드, 파일 저장, PDF 텍스트 추출, 논문 섹션 분석, AI 기반 섹션 요약 기능을 준비합니다.
    """
)

st.info("현재 구현된 기능: PDF 업로드, 파일 저장, PDF 텍스트 추출, 논문 섹션 분리, 섹션 요약. PPT 생성은 아직 구현되지 않았습니다.")

st.header("Phase 0~4: 현재 상태")
st.write(
    """
    - Phase 0: 프로젝트 기본 구조 및 Streamlit 화면 구성
    - Phase 1: PDF 업로드 및 `data/uploads/` 저장
    - Phase 2: PDF 텍스트 추출 및 `data/extracted/` 저장
    - Phase 3: 추출된 텍스트 기반 논문 섹션 분석
    """
)

st.divider()

st.header("Phase 1: PDF 업로드")

uploaded_file = st.file_uploader(
    "PDF 파일을 업로드하세요.",
    type=["pdf"],
    accept_multiple_files=False,
    help="PDF 파일만 업로드할 수 있습니다."
)

if uploaded_file is not None:
    with st.spinner("파일을 저장하는 중입니다..."):
        saved_path = save_uploaded_file(uploaded_file, "data/uploads")

    if saved_path:
        st.success(f"파일이 성공적으로 저장되었습니다: `{saved_path.name}`")
        st.info(f"저장 위치: `{saved_path}`")

        with st.spinner("PDF 텍스트를 추출하는 중입니다..."):
            extracted_path = extract_text_from_pdf_file(str(saved_path), "data/extracted")

        if extracted_path:
            st.success(f"텍스트가 추출되어 저장되었습니다: `{extracted_path.name}`")

            try:
                extracted_text = extracted_path.read_text(encoding="utf-8")
            except OSError:
                extracted_text = ""

            if extracted_text:
                st.subheader("추출된 텍스트 미리보기")
                st.text_area("PDF 텍스트 앞부분", extracted_text[:2000], height=250)

                parsed_sections = extract_paper_sections(extracted_text)
                section_json_path = save_sections_json(parsed_sections, extracted_path)

                st.success(f"논문 섹션 분석 결과가 저장되었습니다: `{section_json_path.name}`")

                if parsed_sections["title"]:
                    st.markdown(f"**Title:** {parsed_sections['title']}")

                missing_sections = parsed_sections.get("missing_sections", [])
                if missing_sections:
                    st.warning(f"탐지되지 않은 섹션: {', '.join(missing_sections)}")

                summary_data = build_section_summaries(parsed_sections)
                summary_json_path = save_section_summaries(summary_data, extracted_path)
                st.success(f"섹션 요약 결과가 저장되었습니다: `{summary_json_path.name}`")

                if summary_data.get("is_mock"):
                    st.info("현재 요약은 Mock Summary 형태로 생성되었습니다. 추후 OpenAI API 연결 시 실제 요약으로 교체됩니다.")

                st.subheader("섹션 요약 결과")
                for section_key in [
                    "abstract",
                    "introduction",
                    "methods",
                    "results",
                    "discussion",
                    "conclusion",
                ]:
                    summary_text = summary_data.get("summaries", {}).get(section_key, "").strip()
                    if summary_text:
                        with st.expander(f"{section_key.title()} 요약"):
                            st.write(summary_text)
                    else:
                        st.warning(f"{section_key.title()} 섹션 요약을 생성할 수 없습니다.")

                if summary_data.get("missing_sections"):
                    st.warning(f"요약할 수 없는 섹션: {', '.join(summary_data['missing_sections'])}")

                st.subheader("탐지된 섹션 목록 및 미리보기")
                for section_key in [
                    "abstract",
                    "introduction",
                    "methods",
                    "results",
                    "discussion",
                    "conclusion",
                    "references",
                ]:
                    section_text = parsed_sections["sections"].get(section_key, "").strip()
                    if section_text:
                        preview = section_text.replace("\n", " ")[:500]
                        with st.expander(f"{section_key.title()} 섹션 미리보기"):
                            st.write(preview)
                    else:
                        st.write(f"- **{section_key.title()}**: 섹션을 찾지 못했습니다.")
            else:
                st.warning("PDF에서 텍스트를 찾지 못했습니다. 스캔 PDF일 가능성이 있습니다.")
        else:
            st.error("PDF 텍스트 추출에 실패했습니다.")
    else:
        st.error("파일 저장에 실패했습니다. PDF 파일인지 확인해주세요.")
