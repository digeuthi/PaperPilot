# PaperPilot

PaperPilot은 논문 PDF 분석 및 발표 자료 구성 보조를 목표로 하는 AI 기반 연구 보조 프로그램입니다.

## Phase 0: 프로젝트 세팅

이 단계에서는 Python + Streamlit 기반 기본 구조를 준비합니다.

### 포함된 항목

- `app.py` 기본 Streamlit 화면
- `README.md`
- `requirements.txt`
- `.env.example`
- `.gitignore`
- `data/` 하위 폴더 및 `.gitkeep`
- `src/`, `tests/` 추적용 `.gitkeep`
- `docs/` 문서 폴더

## 실행 방법

1. Python 가상환경을 생성합니다.

```bash
python -m venv .venv
```

2. 가상환경을 활성화합니다.

```bash
.venv\Scripts\activate
```

3. 의존성을 설치합니다.

```bash
pip install -r requirements.txt
```

4. Streamlit 앱을 실행합니다.

```bash
streamlit run app.py
```

## 다음 단계

- Phase 1: PDF 업로드 및 파일 저장 기능 구현
- Phase 2: PDF 텍스트 추출 기능 추가
