import streamlit as st

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
