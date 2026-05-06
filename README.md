# PaperPilot

PaperPilot은 논문 PDF 분석 및 발표 자료 구성 보조를 목표로 하는 AI 기반 연구 보조 프로그램입니다.

## 현재 구현 상태

- Phase 0: 프로젝트 기본 구조 및 Streamlit 화면 구성
- Phase 1: PDF 업로드 및 `data/uploads/` 저장 기능 구현
- Phase 2: PDF 텍스트 추출 및 `data/extracted/` 저장 기능 구현

## 포함된 항목

- `app.py` Streamlit 기본 화면 및 PDF 업로드 UI
- `src/storage/file_storage.py` PDF 업로드 저장 로직
- `src/document/text_extractor.py` PDF 텍스트 추출 로직
- `requirements.txt`, `.env.example`, `.gitignore`
- `data/uploads/`, `data/extracted/`, `data/summaries/`, `data/slide_plans/`
- `docs/` 문서 폴더

## 사용 라이브러리

- `streamlit`
- `python-dotenv`
- `PyMuPDF`

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

## 현재 개발 단계

- Phase 2: PDF 텍스트 추출 기능 구현 완료
- 다음 단계: Phase 3 논문 구조 분석 기능 구현

## 향후 구현 예정 기능

- PDF 텍스트 섹션 분리
- AI 기반 요약 생성
- PPT 슬라이드 구성안 생성
- PPTX 자동 생성
