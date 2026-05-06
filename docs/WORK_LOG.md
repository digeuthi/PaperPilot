# WORK_LOG.md

# PaperPilot 작업 기록

이 문서는 PaperPilot 프로젝트의 개발 진행 상황, 완료 항목, 이슈, 다음 작업을 기록하기 위한 문서이다.

작업이 끝날 때마다 날짜별로 기록한다.

---

## 기록 규칙

각 작업 단위 또는 Phase가 끝날 때마다 아래 형식으로 기록한다.

```markdown
## YYYY-MM-DD

### 작업 내용
- 수행한 작업을 간단히 정리한다.

### 완료된 항목
- [x] 완료한 항목

### 미완료 항목
- [ ] 아직 완료하지 못한 항목

### 이슈
- 개발 중 발생한 문제
- 원인
- 임시 해결 방법
- 추후 확인이 필요한 부분

### 다음 작업
- 다음에 이어서 진행할 작업
```

---

## 2026-05-06

### 작업 내용
- Phase 0 프로젝트 세팅 진행
- Streamlit 기본 화면 `app.py` 작성
- 프로젝트 초기 문서 및 파일 구조 생성
- `data/` 하위 폴더 및 `.gitkeep` 추가
- `README.md`, `requirements.txt`, `.env.example`, `.gitignore` 생성
- Phase 1 PDF 업로드 및 파일 저장 기능 구현
- Phase 2 PDF 텍스트 추출 기능 구현
- Phase 3 논문 섹션 분석 기능 구현 및 추출된 텍스트 기반 JSON 저장 기능 추가

### 완료된 항목
- [x] 프로젝트명 PaperPilot 확정
- [x] 프로젝트 목적 정의
- [x] `CODING_GUIDELINES.md` 작성
- [x] `DEVELOPMENT_ROADMAP.md` 작성
- [x] `WORK_LOG.md` 작성
- [x] `PROMPT_GUIDE.md` 작성
- [x] 프로젝트 기본 폴더 구조 생성
- [x] Streamlit 기본 화면 구성
- [x] `app.py`, `README.md`, `requirements.txt`, `.env.example`, `.gitignore` 생성
- [x] `data/` 하위 폴더와 `.gitkeep` 생성
- [x] `src/`, `tests/` 빈 폴더 추적용 `.gitkeep` 추가
- [x] Phase 1 PDF 업로드 및 파일 저장 기능 구현
- [x] Phase 2 PDF 텍스트 추출 기능 구현
- [x] Phase 3 논문 섹션 분석 기능 구현 및 JSON 저장 기능 추가
- [x] Python 가상환경 생성 및 의존성 설치

### 미완료 항목
- [ ] AI 요약 기능 구현
- [ ] PPT 생성 기능 구현

### 이슈
- 아직 실제 AI 요약과 PPT 생성을 구현하지 않았다.
- PDF 텍스트 추출 후 추가 분석 단계는 Phase 3 이후에 진행할 예정.

### 다음 작업
- Phase 4 AI 요약 기능 구현
- PPT 슬라이드 구성안 생성 기능 설계
- 추후 OCR 및 Figure/Table 분석 단계 준비
