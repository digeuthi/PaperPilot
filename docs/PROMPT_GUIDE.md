# PROMPT_GUIDE.md

# PaperPilot Copilot / AI 작업 요청 가이드

이 문서는 VS Code Copilot 또는 AI 도구에게 PaperPilot 프로젝트 작업을 요청할 때 사용하는 프롬프트 예시와 규칙을 정리한 문서이다.

Copilot에게 작업을 요청할 때는 반드시 다음 문서를 기준으로 하도록 지시한다.

```text
docs/CODING_GUIDELINES.md
docs/DEVELOPMENT_ROADMAP.md
docs/WORK_LOG.md
```

---

## 1. 기본 요청 원칙

Copilot에게 한 번에 너무 큰 작업을 요청하지 않는다.

나쁜 예:

```text
논문 분석 프로그램 전체를 만들어줘.
```

좋은 예:

```text
docs/CODING_GUIDELINES.md와 docs/DEVELOPMENT_ROADMAP.md를 기준으로,
Phase 1의 PDF 업로드 및 파일 저장 기능만 구현해줘.
Streamlit 기반으로 app.py를 작성하고,
파일 저장 로직은 src/storage/file_storage.py로 분리해줘.
```

---

## 2. Copilot에게 항상 포함할 기준 문구

작업 요청을 시작할 때 아래 문구를 포함한다.

```text
이 프로젝트는 PaperPilot이라는 논문 분석 및 발표자료 구성 보조 프로그램입니다.

docs/CODING_GUIDELINES.md, docs/DEVELOPMENT_ROADMAP.md, docs/WORK_LOG.md를 먼저 읽고,
그 지침을 기준으로 작업해주세요.

한 번에 모든 기능을 만들지 말고,
현재 요청한 Phase 또는 기능만 구현해주세요.

- 작업 후 `docs/WORK_LOG.md`와 `README.md`를 현재 구현 상태에 맞게 함께 업데이트해주세요.
```

---

## 3. Phase 0 요청 프롬프트

```text
이 프로젝트는 PaperPilot이라는 논문 분석 및 발표자료 구성 보조 프로그램입니다.

docs/CODING_GUIDELINES.md와 docs/DEVELOPMENT_ROADMAP.md를 기준으로,
Phase 0 프로젝트 세팅을 진행해주세요.

현재는 GitHub에서 생성한 빈 Repository를 VS Code로 Clone한 상태입니다.

Python + Streamlit 기반으로 시작하고,
다음 항목을 생성해주세요.

- app.py
- README.md
- requirements.txt
- .env.example
- .gitignore
- docs/WORK_LOG.md
- docs/PROMPT_GUIDE.md
- data/uploads/
- data/extracted/
- data/summaries/
- data/slide_plans/
- src/
- tests/

Streamlit 기본 화면이 실행되도록 app.py도 작성해주세요.

단, API Key가 들어가는 .env 파일은 생성하지 말고,
.env.example만 생성해주세요.
```

---

## 4. Phase 1 요청 프롬프트

```text
docs/CODING_GUIDELINES.md와 docs/DEVELOPMENT_ROADMAP.md를 기준으로,
Phase 1의 PDF 업로드 및 파일 저장 기능을 구현해주세요.

요구사항:
- Streamlit에서 PDF 파일 업로드 UI를 만든다.
- PDF 파일만 업로드 가능하게 한다.
- 업로드된 파일은 data/uploads/ 폴더에 저장한다.
- 파일 저장 로직은 src/storage/file_storage.py로 분리한다.
- 저장 성공/실패 메시지를 화면에 표시한다.
- 작업 후 docs/WORK_LOG.md에 작업 내용을 기록한다.
```

---

## 5. Phase 2 요청 프롬프트

```text
docs/CODING_GUIDELINES.md와 docs/DEVELOPMENT_ROADMAP.md를 기준으로,
Phase 2의 PDF 텍스트 추출 기능을 구현해주세요.

요구사항:
- PyMuPDF를 사용한다.
- PDF 텍스트 추출 로직은 src/document/text_extractor.py로 분리한다.
- 추출된 텍스트는 data/extracted/ 폴더에 .txt 파일로 저장한다.
- Streamlit 화면에는 추출된 텍스트의 앞부분만 미리보기로 표시한다.
- 텍스트가 없는 PDF일 경우 스캔 PDF일 가능성이 있다는 안내 메시지를 표시한다.
- 작업 후 docs/WORK_LOG.md에 작업 내용을 기록한다.
```

---

## 6. Phase 3 요청 프롬프트

```text
docs/CODING_GUIDELINES.md와 docs/DEVELOPMENT_ROADMAP.md를 기준으로,
Phase 3의 논문 구조 분석 기능을 구현해주세요.

요구사항:
- 추출된 텍스트를 섹션별로 분리한다.
- Abstract, Introduction, Methods, Results, Discussion, Conclusion, References를 우선 고려한다.
- Methods는 Materials and Methods도 인식하도록 한다.
- 섹션 분리 로직은 src/analysis/paper_parser.py로 분리한다.
- 결과는 JSON으로 저장한다.
- 섹션 분리에 실패하면 전체 텍스트 기반 fallback 결과를 생성한다.
- 작업 후 docs/WORK_LOG.md에 작업 내용을 기록한다.
```

---

## 7. Phase 4 요청 프롬프트

```text
docs/CODING_GUIDELINES.md와 docs/DEVELOPMENT_ROADMAP.md를 기준으로,
Phase 4의 AI 기반 섹션 요약 기능을 구현해주세요.

요구사항:
- LLM API 호출 로직은 src/ai/llm_client.py로 분리한다.
- 프롬프트는 src/ai/prompts.py에 작성한다.
- API Key는 .env에서 읽어온다.
- AI가 논문에 없는 내용을 추가하지 않도록 프롬프트에 명시한다.
- 추측이 필요한 경우 "추측"이라고 표시하도록 한다.
- Results와 Discussion을 구분하도록 한다.
- 결과는 JSON으로 저장한다.
- 작업 후 docs/WORK_LOG.md에 작업 내용을 기록한다.
```

---

## 8. Phase 5 요청 프롬프트

```text
docs/CODING_GUIDELINES.md와 docs/DEVELOPMENT_ROADMAP.md를 기준으로,
Phase 5의 1장 공부 요약 생성 기능을 구현해주세요.

요구사항:
- 섹션 요약 결과를 기반으로 1장 공부 요약을 생성한다.
- 출력 형식은 Markdown으로 한다.
- 요약 생성 로직은 src/output/one_page_summary_generator.py로 분리한다.
- 결과는 data/summaries/ 폴더에 .md 파일로 저장한다.
- 필요하다면 JSON 메타데이터도 함께 저장할 수 있도록 구조를 준비한다.
- 요약에는 논문 제목, 핵심 연구 질문, 연구 배경, 사용한 방법, 주요 결과, 핵심 주장, 한계점 및 발표 시 강조 포인트를 포함해야 한다.
- Streamlit 화면에 1장 공부 요약을 보기 좋게 표시하고, Markdown 파일 다운로드 버튼을 추가한다.
- 작업 후 docs/WORK_LOG.md에 작업 내용을 기록한다.
```

---

## 9. Phase 6 요청 프롬프트

```text
docs/CODING_GUIDELINES.md와 docs/DEVELOPMENT_ROADMAP.md를 기준으로,
Phase 6의 PPT 슬라이드 구성안 생성 기능을 구현해주세요.

요구사항:
- 5분, 10분, 15분 발표 시간을 선택할 수 있게 한다.
- 발표 시간에 따라 슬라이드 개수를 조정한다.
- 슬라이드별 제목, 핵심 메시지, bullet point, 발표자 노트 초안을 생성한다.
- 슬라이드 구성 로직은 src/output/slide_plan_generator.py로 분리한다.
- 결과는 JSON과 Markdown으로 저장한다.
- 작업 후 docs/WORK_LOG.md에 작업 내용을 기록한다.
```

---

## 10. 코드 수정 요청 프롬프트

```text
현재 구현된 코드에서 다음 부분을 수정해주세요.

수정 대상:
- 파일명:
- 함수명:
- 문제 상황:

수정 요구사항:
- 기존 구조는 최대한 유지해주세요.
- docs/CODING_GUIDELINES.md의 코딩 수칙을 지켜주세요.
- 수정 후 어떤 파일이 변경되었는지 설명해주세요.
- 작업 후 docs/WORK_LOG.md에 기록해주세요.
```

---

## 11. 디버깅 요청 프롬프트

```text
다음 오류가 발생했습니다.

오류 메시지:
[여기에 오류 메시지 붙여넣기]

상황:
- 실행 명령:
- 수행한 작업:
- 기대한 결과:
- 실제 결과:

docs/CODING_GUIDELINES.md를 기준으로,
원인을 분석하고 수정 방법을 제안해주세요.
필요한 경우 코드 수정도 진행해주세요.
```

---

## 12. 작업 후 확인 요청 프롬프트

```text
방금 구현한 기능이 docs/CODING_GUIDELINES.md와 docs/DEVELOPMENT_ROADMAP.md 기준에 맞는지 검토해주세요.

확인할 항목:
- 기능별 파일 분리가 되어 있는가
- 예외 처리가 되어 있는가
- .env가 Git에 포함되지 않는가
- 불필요한 코드가 없는가
- WORK_LOG.md가 업데이트되었는가
- README.md가 현재 구현 상태를 반영하고 있는가
- 다음 작업이 명확히 기록되었는가
```

---

## 13. 커밋 메시지 요청 프롬프트

```text
현재 변경사항에 적절한 Git 커밋 메시지를 추천해주세요.

커밋 메시지는 아래 형식을 따르며, 본문은 한국어로 작성합니다.

- init: 초기 세팅 및 구조 생성
- docs: 문서 추가/수정
- feat: 기능 추가
- fix: 버그 수정
- refactor: 리팩터링
- test: 테스트 추가/수정

예시:
- feat: PDF 업로드 및 파일 저장 기능 구현
- docs: WORK_LOG에 Phase 1 작업 기록
- refactor: 파일 저장 로직을 src/storage/file_storage.py로 분리
- fix: PDF 업로드 파일 형식 검증 오류 수정
```

---

## 14. 커밋 작성 가이드

- 각 Phase별 변경 사항은 작은 단위로 커밋합니다.
- 커밋 메시지는 `prefix: 설명` 형태로 한글로 작성합니다.
- `docs/WORK_LOG.md` 업데이트도 커밋에 포함합니다.
- 변경 사항이 많지 않다면 한 Phase를 하나의 커밋으로 유지합니다.
- 예시 커밋 명령:

```bash
git add .
git commit -m "feat: Phase 1 PDF 업로드 및 저장 기능 구현"
```

- 커밋 후에는 `git log --oneline --decorate`로 커밋 기록을 확인합니다.

이번 변경사항을 기준으로 가장 적절한 커밋 메시지를 3개 정도 추천해주세요.
```

---

## 14. 주의사항

Copilot이 한 번에 너무 많은 코드를 생성하려고 하면 작업 범위를 줄인다.

예:

```text
지금은 Phase 1만 구현해주세요.
AI 요약, PPT 생성, OCR 기능은 아직 만들지 마세요.
```

항상 작은 단위로 진행한다.

```text
1. 폴더 구조 생성
2. 기본 화면 생성
3. PDF 업로드
4. 파일 저장
5. 텍스트 추출
6. 섹션 분리
7. 요약 생성
8. 슬라이드 구성안 생성
```
