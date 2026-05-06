# CODING_GUIDELINES.md

# PaperPilot 코딩 지침

## 1. 프로젝트 개요

PaperPilot은 논문 PDF 또는 이미지 파일을 입력받아 대학원 박사과정 1년차 연구자가 논문을 분석하고 발표 준비를 할 수 있도록 돕는 AI 기반 연구 발표 보조 프로그램이다.

PaperPilot의 주요 결과물은 다음과 같다.

- 논문 1장 공부 요약
- 논문 구조 분석
- Figure / Table 핵심 해석
- PPT 발표용 슬라이드 구성안
- 추후 PPTX 초안 자동 생성

초기 목표는 완성형 프로그램이 아니라 MVP를 만드는 것이다.

---

## 2. MVP 정의

이 프로젝트에서 MVP는 `Minimum Viable Product`, 즉 최소 기능 제품을 의미한다.

초기 MVP의 목표는 다음과 같다.

```text
논문 PDF 업로드
→ 텍스트 추출
→ 논문 구조 분석
→ 1장 공부 요약 생성
→ PPT 슬라이드 구성안 생성
```

초기 MVP에서는 다음 기능은 제외한다.

- 사용자 로그인
- 복잡한 DB 관리
- 완성형 PPT 디자인
- 다중 사용자 지원
- 논문 추천 기능
- 자동 발표 음성 생성
- 고급 에이전트 구조

---

## 3. 기본 개발 원칙

- 한 번에 전체 프로그램을 만들지 않는다.
- Phase 단위로 작게 구현하고 테스트한다.
- 한 파일에 모든 기능을 작성하지 않는다.
- 기능별로 모듈을 분리한다.
- 함수 하나는 하나의 책임만 가진다.
- AI 호출 로직과 UI 로직을 분리한다.
- 파일 저장 로직과 분석 로직을 분리한다.
- 테스트 가능한 구조로 작성한다.
- 임시 코드는 반드시 TODO 주석을 남긴다.
- 사용하지 않는 코드는 삭제한다.
- 각 Phase 완료 시 작업 기록을 남긴다.

## 3.1 README 업데이트 규칙

각 Phase가 완료될 때마다 `README.md`도 함께 확인하고 필요한 경우 업데이트한다.

README.md에는 다음 내용을 현재 구현 상태에 맞게 반영한다.

- 프로젝트 소개
- 현재 구현된 기능
- 아직 구현되지 않은 기능
- 실행 방법
- 폴더 구조
- 사용 라이브러리
- 다음 개발 예정 기능

Phase 완료 후 Copilot은 다음 문서를 함께 업데이트해야 한다.

- `docs/WORK_LOG.md`
- `README.md`

단, `README.md`에는 너무 상세한 개발 이력을 모두 적지 않는다.
상세 개발 이력은 `docs/WORK_LOG.md`에 기록하고,
`README.md`에는 사용자가 프로젝트를 이해하고 실행하는 데 필요한 정보만 정리한다.

---

## 4. 추천 기술 스택

초기 MVP 기준 기술 스택은 다음과 같다.

```text
Language: Python
UI: Streamlit
PDF Processing: PyMuPDF
AI API: OpenAI API 또는 호환 LLM API
Storage: Local File / JSON / Markdown
PPT Generation: python-pptx
```

초기에는 복잡한 백엔드 서버나 DB를 도입하지 않는다.

---

## 5. 추천 프로젝트 구조

```text
PaperPilot/
│
├─ app.py
│
├─ README.md
├─ requirements.txt
├─ .env.example
├─ .gitignore
│
├─ docs/
│   ├─ CODING_GUIDELINES.md
│   ├─ DEVELOPMENT_ROADMAP.md
│   ├─ WORK_LOG.md
│   └─ PROMPT_GUIDE.md
│
├─ data/
│   ├─ uploads/
│   ├─ extracted/
│   ├─ summaries/
│   └─ slide_plans/
│
├─ src/
│   ├─ config/
│   │   └─ settings.py
│   │
│   ├─ document/
│   │   ├─ pdf_loader.py
│   │   ├─ text_extractor.py
│   │   ├─ image_extractor.py
│   │   └─ ocr_processor.py
│   │
│   ├─ analysis/
│   │   ├─ paper_parser.py
│   │   ├─ section_analyzer.py
│   │   ├─ figure_analyzer.py
│   │   └─ claim_extractor.py
│   │
│   ├─ ai/
│   │   ├─ llm_client.py
│   │   ├─ prompts.py
│   │   └─ structured_outputs.py
│   │
│   ├─ output/
│   │   ├─ study_summary_generator.py
│   │   ├─ slide_plan_generator.py
│   │   └─ ppt_generator.py
│   │
│   ├─ storage/
│   │   ├─ file_storage.py
│   │   └─ json_repository.py
│   │
│   └─ utils/
│       ├─ logger.py
│       └─ file_utils.py
│
└─ tests/
    ├─ test_pdf_loader.py
    ├─ test_text_extractor.py
    └─ test_paper_parser.py
```

---

## 6. 네이밍 규칙

### 6.1 폴더명

폴더명은 소문자 또는 snake_case를 사용한다.

```text
document
analysis
output
file_storage
```

### 6.2 파일명

Python 파일명은 snake_case를 사용한다.

```text
pdf_loader.py
text_extractor.py
paper_parser.py
study_summary_generator.py
slide_plan_generator.py
```

### 6.3 클래스명

클래스명은 PascalCase를 사용한다.

```python
class PdfLoader:
    pass

class PaperParser:
    pass

class StudySummaryGenerator:
    pass
```

### 6.4 함수명

함수명은 snake_case를 사용한다.

```python
def extract_text_from_pdf(file_path: str) -> str:
    pass

def generate_study_summary(paper_data: dict) -> str:
    pass
```

### 6.5 변수명

변수명은 snake_case를 사용한다.

```python
paper_title = ""
section_text = ""
summary_result = {}
```

---

## 7. 함수 작성 규칙

함수 하나는 하나의 책임만 가진다.

좋은 예:

```python
def extract_text_from_pdf(file_path: str) -> str:
    """PDF 파일에서 텍스트만 추출한다."""
    pass
```

나쁜 예:

```python
def process_paper():
    """PDF 업로드, 저장, 텍스트 추출, AI 요약, 화면 출력을 모두 처리한다."""
    pass
```

하나의 함수가 다음을 모두 처리하면 안 된다.

- 파일 업로드
- 파일 저장
- 텍스트 추출
- AI 호출
- 결과 저장
- UI 출력

---

## 8. AI 호출 규칙

AI 호출 로직은 UI 코드와 분리한다.

나쁜 예:

```python
# app.py 안에서 직접 OpenAI API 호출
```

좋은 예:

```text
src/ai/llm_client.py
```

AI 프롬프트는 가능한 한 별도 파일 또는 `prompts.py`에 모아둔다.

프롬프트에는 반드시 다음 원칙을 포함한다.

```text
- 논문에 없는 내용을 추가하지 말 것
- 추측이 필요한 경우 "추측"이라고 표시할 것
- 원문 근거가 약한 내용은 "확인 필요"라고 표시할 것
- Results와 Discussion을 구분할 것
- Figure caption 기반 해석과 이미지 자체 해석을 구분할 것
- 발표용 문장은 간결하게 작성할 것
```

---

## 9. 출력 데이터 규칙

AI 중간 결과는 JSON으로 저장한다.

사용자에게 보여주는 최종 결과는 Markdown으로 저장한다.

PPT 생성 입력 데이터도 JSON 기반으로 한다.

```text
AI 중간 결과: JSON
사용자 출력 결과: Markdown
PPT 생성 입력: JSON
```

예시:

```json
{
  "title": "",
  "research_question": "",
  "background": [],
  "methods": [],
  "main_findings": [],
  "limitations": [],
  "presentation_points": []
}
```

---

## 10. 예외 처리 규칙

다음 상황은 반드시 예외 처리한다.

- PDF 업로드 실패
- PDF 텍스트 추출 실패
- 스캔 PDF로 인한 텍스트 없음
- AI API 호출 실패
- JSON 파싱 실패
- 파일 저장 실패
- PPT 생성 실패

사용자에게는 기술적인 에러를 그대로 보여주지 않는다.

예:

```text
PDF 텍스트 추출에 실패했습니다.
스캔본 PDF일 가능성이 있습니다. OCR 기능을 사용해 다시 시도해주세요.
```

---

## 11. 로그 작성 규칙

주요 처리 단계에는 로그를 남긴다.

예:

```text
[INFO] PDF upload started
[INFO] Text extraction completed
[INFO] Section parsing started
[ERROR] LLM API call failed
```

로그에는 다음 내용을 포함한다.

- 처리 시작
- 처리 완료
- 실패 원인
- 파일명
- 처리 시간

단, API Key나 개인정보는 로그에 남기지 않는다.

---

## 12. Git 커밋 규칙

작업은 기능 단위 또는 Phase 단위로 커밋한다.

커밋 메시지 예:

```text
init: create project structure
docs: add coding guidelines
docs: add development roadmap
feat: add pdf upload feature
feat: implement pdf text extraction
feat: add paper section parser
feat: generate one-page study summary
feat: create slide plan generator
fix: handle empty abstract section
refactor: separate llm client from summary generator
```

커밋 전 확인 사항:

```text
- 실행 가능한 상태인가?
- 불필요한 파일이 포함되지 않았는가?
- .env 파일이 커밋되지 않았는가?
- 테스트용 PDF가 너무 크지 않은가?
- 작업 기록이 업데이트되었는가?
```

---

## 13. Copilot 사용 규칙

Copilot에게 코드를 맡길 때는 반드시 다음 문서를 기준으로 하라고 지시한다.

```text
docs/CODING_GUIDELINES.md
docs/DEVELOPMENT_ROADMAP.md
docs/WORK_LOG.md
```

Copilot에게 요청할 때는 한 번에 큰 작업을 요청하지 않는다.

나쁜 요청:

```text
논문 분석 프로그램 전체를 만들어줘.
```

좋은 요청:

```text
docs/CODING_GUIDELINES.md와 docs/DEVELOPMENT_ROADMAP.md를 기준으로,
Phase 1의 PDF 업로드와 파일 저장 기능만 구현해줘.
Streamlit 기반으로 app.py를 만들고,
저장 로직은 src/storage/file_storage.py로 분리해줘.
```

---

## 14. 작업 완료 후 기록 규칙

각 기능을 구현한 뒤 `docs/WORK_LOG.md`에 기록한다.

기록 형식:

```markdown
## YYYY-MM-DD

### 작업 내용
- PDF 업로드 UI 추가
- 업로드 파일 저장 경로 구성

### 완료된 항목
- [x] PDF 업로드
- [x] 파일 저장

### 미완료 항목
- [ ] PDF 텍스트 추출

### 이슈
- 없음

### 다음 작업
- PyMuPDF 기반 텍스트 추출 구현
```
