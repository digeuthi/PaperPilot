import streamlit as st
from src.storage.file_storage import save_uploaded_file

st.set_page_config(page_title="PaperPilot", page_icon="📄", layout="centered")

st.title("PaperPilot")
st.markdown(
    """
    PaperPilot은 논문 분석 및 발표자료 구성 보조를 목표로 하는 MVP입니다.

    이 Phase 0 버전에서는 프로젝트 기본 구조와 Streamlit 기본 화면을 준비합니다.
    """
)

st.info("PDF 분석, AI 요약, PPT 생성 기능은 아직 구현되지 않았습니다.")

st.header("Phase 0: 기본 설정 완료")
st.write(
    """
    - `app.py` 기본 화면
    - `README.md`, `requirements.txt`, `.env.example`, `.gitignore` 생성
    - `data/` 하위 폴더 및 `.gitkeep` 생성
    - `src/`, `tests/` 빈 폴더 추적용 `.gitkeep` 추가
    """
)

st.caption("다음 단계: Phase 1 PDF 업로드 및 파일 저장 기능 구현")

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
    else:
        st.error("파일 저장에 실패했습니다. PDF 파일인지 확인해주세요.")
