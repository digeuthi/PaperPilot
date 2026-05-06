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

### 미완료 항목
- [ ] Python 가상환경 생성
- [ ] Phase 1 PDF 업로드 기능 구현

### 이슈
- 아직 실제 코드 구현 전 단계이다.
- GitHub Repository 생성 후 프로젝트 폴더 구조를 먼저 정리해야 한다.
- 빈 폴더는 Git에서 추적되지 않으므로 `.gitkeep`로 보완함.

### 다음 작업
- Phase 1 PDF 업로드 및 파일 저장 기능 구현
- `src/storage/file_storage.py` 구조 설계
- Python 가상환경 생성 및 의존성 설치
