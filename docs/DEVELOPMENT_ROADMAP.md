# DEVELOPMENT_ROADMAP.md

# PaperPilot 개발 로드맵

## 1. 프로젝트 목표

PaperPilot은 논문 PDF 또는 이미지 파일을 입력받아 대학원 박사과정 1년차 연구자가 발표 준비에 사용할 수 있는 결과물을 생성하는 AI 기반 연구 발표 보조 프로그램이다.

최종 목표는 다음과 같다.

```text
논문 입력
→ 논문 구조 분석
→ 핵심 내용 요약
→ Figure / Table 해석
→ 1장 공부 요약 생성
→ PPT 슬라이드 구성안 생성
→ PPTX 초안 생성
```

---

## 2. MVP 범위

초기 MVP는 다음 기능까지만 구현한다.

```text
PDF 업로드
→ 텍스트 추출
→ 논문 구조 분석
→ 1장 공부 요약 생성
→ PPT 슬라이드 구성안 생성
```

초기 MVP에서 제외하는 기능:

```text
- 사용자 로그인
- 다중 사용자 관리
- 완성형 PPT 디자인
- 고급 OCR
- 논문 추천
- 자동 발표 음성 생성
- 복잡한 에이전트 구조
```

---

## 3. Phase 0. 프로젝트 세팅

### 목표

VS Code에서 실행 가능한 Python 프로젝트 기본 구조를 만든다.

### 작업 항목

- [ ] 프로젝트 폴더 생성 또는 GitHub Repository Clone
- [ ] Python 가상환경 생성
- [ ] requirements.txt 생성
- [ ] .env.example 생성
- [ ] .gitignore 생성
- [ ] docs 폴더 생성
- [ ] data 폴더 생성
- [ ] src 폴더 생성
- [ ] tests 폴더 생성
- [ ] Streamlit 기본 화면 실행
- [ ] Git 초기 커밋 생성

### 완료 기준

- [ ] `streamlit run app.py` 실행 가능
- [ ] 기본 화면이 표시됨
- [ ] Git 초기 커밋이 존재함

### 예상 결과물

```text
app.py
requirements.txt
README.md
docs/CODING_GUIDELINES.md
docs/DEVELOPMENT_ROADMAP.md
docs/WORK_LOG.md
docs/PROMPT_GUIDE.md
```

---

## 4. Phase 1. PDF 업로드 및 파일 저장

### 목표

사용자가 PDF 파일을 업로드하고, 업로드된 파일을 로컬 폴더에 저장한다.

### 작업 항목

- [ ] Streamlit 파일 업로드 UI 작성
- [ ] PDF 파일 확장자 검증
- [ ] 업로드 파일을 `data/uploads/`에 저장
- [ ] 중복 파일명 처리
- [ ] 저장 성공 메시지 표시
- [ ] 파일 저장 로직을 `src/storage/file_storage.py`로 분리

### 완료 기준

- [ ] PDF 파일 업로드 가능
- [ ] 업로드된 파일이 `data/uploads/`에 저장됨
- [ ] 잘못된 파일 형식일 경우 안내 메시지 표시

### Copilot 요청 예시

```text
docs/CODING_GUIDELINES.md와 docs/DEVELOPMENT_ROADMAP.md를 기준으로,
Phase 1의 PDF 업로드 및 파일 저장 기능을 구현해줘.
Streamlit을 사용하고,
파일 저장 로직은 src/storage/file_storage.py로 분리해줘.
```

---

## 5. Phase 2. PDF 텍스트 추출

### 목표

업로드된 PDF에서 텍스트를 추출한다.

### 작업 항목

- [ ] PyMuPDF 설치
- [ ] PDF 텍스트 추출 함수 작성
- [ ] 추출된 텍스트를 화면에 일부 표시
- [ ] 추출된 텍스트를 `data/extracted/`에 `.txt`로 저장
- [ ] 텍스트가 없는 PDF 처리
- [ ] 텍스트 추출 로직을 `src/document/text_extractor.py`로 분리

### 완료 기준

- [ ] PDF 본문 텍스트가 추출됨
- [ ] 추출 결과 파일이 저장됨
- [ ] 텍스트가 없는 경우 안내 메시지 표시

### 주의 사항

- Phase 2에서는 OCR을 필수로 구현하지 않는다.
- 스캔 PDF는 추후 Phase에서 처리한다.

---

## 6. Phase 3. 논문 구조 분석

### 목표

추출된 텍스트를 논문 섹션 단위로 분리한다.

### 주요 섹션

```text
Title
Abstract
Introduction
Methods
Results
Discussion
Conclusion
References
```

### 작업 항목

- [ ] 섹션명 패턴 정의
- [ ] Abstract 추출
- [ ] Introduction 추출
- [ ] Methods 또는 Materials and Methods 추출
- [ ] Results 추출
- [ ] Discussion 추출
- [ ] Conclusion 추출
- [ ] References 제외
- [ ] 섹션별 결과를 JSON으로 저장
- [ ] 섹션 분석 로직을 `src/analysis/paper_parser.py`로 분리

### 완료 기준

- [ ] 주요 섹션이 JSON으로 분리됨
- [ ] 섹션 분리 실패 시 전체 텍스트 기반 fallback 가능

### 주의 사항

논문마다 섹션명이 다를 수 있으므로 다음 패턴을 고려한다.

```text
Methods
Materials and Methods
Experimental Procedures
Results and Discussion
Discussion and Conclusion
Conclusion
Conclusions
```

---

## 7. Phase 4. AI 기반 섹션 요약

### 목표

논문 각 섹션을 AI를 이용해 요약한다.

### 작업 항목

- [ ] LLM API 클라이언트 구성
- [ ] API Key를 `.env`에서 로드
- [ ] 섹션별 요약 프롬프트 작성
- [ ] Abstract 요약
- [ ] Introduction 요약
- [ ] Methods 요약
- [ ] Results 요약
- [ ] Discussion 요약
- [ ] 요약 결과를 JSON으로 저장
- [ ] AI 호출 로직을 `src/ai/llm_client.py`로 분리
- [ ] 프롬프트를 `src/ai/prompts.py`로 분리

### 완료 기준

- [ ] 각 섹션별 요약 생성 가능
- [ ] 요약 결과가 JSON으로 저장됨
- [ ] AI가 논문에 없는 내용을 생성하지 않도록 프롬프트에 제한 문구 포함

### 주의 사항

- AI 응답은 항상 검증 대상이다.
- 원문에 없는 내용은 생성하지 않도록 한다.
- 추측은 반드시 "추측"으로 표시한다.

---

## 8. Phase 5. 1장 공부 요약 생성

### 목표

박사과정 1년차가 발표 전에 볼 수 있는 1장 요약을 생성한다.

### 출력 구성

```text
1. 논문 제목
2. 연구 배경
3. 핵심 질문
4. 이 논문이 해결하려는 문제
5. 사용한 방법
6. 주요 결과
7. Figure / Table 핵심 의미
8. 저자의 주장
9. 한계점
10. 발표 시 강조할 포인트
```

### 작업 항목

- [x] 섹션 요약 결과를 기반으로 통합 요약 생성
- [x] Markdown 형식으로 출력
- [x] `data/summaries/`에 Markdown 저장
- [x] Streamlit UI에 1장 요약 표시 및 다운로드 기능 추가
- [x] 1장 요약 저장 로직을 `src/output/one_page_summary_generator.py`로 분리

### 완료 기준

- [x] 1장 공부 요약 Markdown 생성
- [x] 1장 공부 요약이 `data/summaries/`에 저장됨
- [x] Streamlit에서 Markdown 출력 및 다운로드 버튼 표시됨
- [ ] 실제 OpenAI API 연결 없이 Mock 기반 동작
- [ ] 화면에 요약 표시
- [ ] `data/summaries/`에 `.md` 파일 저장
- [ ] 요약 생성 로직을 `src/output/study_summary_generator.py`로 분리

### 완료 기준

- [ ] 1장 요약 Markdown 생성 가능
- [ ] 사용자가 복사해서 공부 자료로 사용할 수 있음
- [ ] 논문의 핵심 질문과 주장이 명확히 드러남

---

## 9. Phase 6. PPT 슬라이드 구성안 생성

### 목표

논문 발표용 PPT 슬라이드 구성안을 생성한다.

### 기본 슬라이드 구조

```text
Slide 1. Title
Slide 2. Background
Slide 3. Research Question
Slide 4. Method Overview
Slide 5. Key Figure 1
Slide 6. Key Figure 2
Slide 7. Main Findings
Slide 8. Discussion
Slide 9. Limitation
Slide 10. Conclusion
Slide 11. Q&A
```

### 작업 항목

- [ ] 발표 시간 선택 기능 추가
- [ ] 5분 발표용 슬라이드 구조 생성
- [ ] 10분 발표용 슬라이드 구조 생성
- [ ] 15분 발표용 슬라이드 구조 생성
- [ ] 슬라이드별 제목 생성
- [ ] 슬라이드별 핵심 메시지 생성
- [ ] 슬라이드별 bullet point 생성
- [ ] 발표자 노트 초안 생성
- [ ] 결과를 JSON과 Markdown으로 저장
- [ ] 슬라이드 구성 로직을 `src/output/slide_plan_generator.py`로 분리

### 완료 기준

- [ ] 슬라이드별 구성안 생성 가능
- [ ] 사용자가 PPT에 그대로 옮길 수 있음
- [ ] 발표 흐름이 자연스러움

---

## 10. Phase 7. Figure / Table 분석

### 목표

논문 내 Figure와 Table을 추출하고 발표용으로 해석한다.

### 작업 항목

- [ ] PDF 내 이미지 추출
- [ ] Figure caption 추출
- [ ] Figure 번호와 caption 매칭
- [ ] Figure별 핵심 메시지 생성
- [ ] 발표 우선순위 지정
- [ ] 슬라이드 구성안에 Figure 추천 반영
- [ ] Figure 분석 로직을 `src/analysis/figure_analyzer.py`로 분리

### 완료 기준

- [ ] Figure별 설명 생성 가능
- [ ] 어떤 Figure를 PPT에 넣을지 추천 가능
- [ ] Figure 해석이 caption과 연결됨

### 주의 사항

- 이미지 자체 해석보다 caption 기반 분석을 우선한다.
- AI가 Figure에 없는 내용을 단정하지 않도록 한다.
- 복잡한 Figure는 사용자가 직접 확인할 수 있도록 원본 이미지를 함께 표시한다.

---

## 11. Phase 8. PPTX 초안 생성

### 목표

슬라이드 구성안을 기반으로 실제 PPTX 초안을 생성한다.

### 작업 항목

- [ ] python-pptx 설치
- [ ] 제목 슬라이드 생성
- [ ] 배경 슬라이드 생성
- [ ] 결과 슬라이드 생성
- [ ] Figure 이미지 삽입
- [ ] PPTX 파일 저장
- [ ] PPTX 다운로드 기능 추가
- [ ] PPT 생성 로직을 `src/output/ppt_generator.py`로 분리

### 완료 기준

- [ ] `.pptx` 파일 생성 가능
- [ ] 제목, 본문, Figure가 포함됨
- [ ] 발표자가 초안을 수정해서 사용할 수 있음

### 주의 사항

- 초기에는 디자인보다 구조를 우선한다.
- PPT는 완성본이 아니라 초안이다.
- 텍스트가 너무 많은 슬라이드를 만들지 않는다.

---

## 12. Phase 9. 검증 기능

### 목표

AI가 논문에 없는 내용을 생성하지 않았는지 검토한다.

### 작업 항목

- [ ] 요약 문장별 근거 섹션 연결
- [ ] 논문에 없는 주장 탐지
- [ ] 과장 표현 탐지
- [ ] Results와 Discussion 구분 검토
- [ ] 발표 전 확인 체크리스트 생성

### 완료 기준

- [ ] 요약 결과의 신뢰도를 높일 수 있음
- [ ] 사용자가 발표 전에 확인해야 할 위험 포인트를 알 수 있음

### 주의 사항

- 완전 자동 검증은 불가능하다.
- 불확실한 내용은 "확인 필요"로 표시한다.
- 논문 원문 근거가 없는 내용은 제거하거나 별도 표시한다.

---

## 13. 개발 진행 방식

각 Phase는 다음 순서로 진행한다.

```text
1. 기능 목표 확인
2. 관련 파일 생성
3. 최소 기능 구현
4. 실행 테스트
5. 예외 처리 추가
6. 작업 기록 작성
7. Git 커밋
```

---

## 14. 작업 기록 규칙

각 Phase 또는 기능 완료 후 `docs/WORK_LOG.md`에 기록한다.

기록 예시:

```markdown
## YYYY-MM-DD

### 작업 내용
- PDF 업로드 UI 추가
- 업로드 파일 저장 경로 구성
- PyMuPDF 기반 텍스트 추출 테스트

### 완료된 항목
- [x] PDF 업로드
- [x] 파일 저장
- [x] 텍스트 추출

### 미완료 항목
- [ ] 스캔 PDF OCR 처리
- [ ] 섹션 자동 분리

### 이슈
- 일부 논문에서 Abstract 제목이 감지되지 않음

### 다음 작업
- 섹션명 패턴 목록 추가
- Introduction / Methods / Results 분리 로직 구현
```

---

## 15. 현재 우선순위

현재 가장 먼저 할 일은 다음과 같다.

```text
1. GitHub에서 PaperPilot Repository 생성
2. VS Code에서 Repository Clone
3. docs 폴더 생성
4. CODING_GUIDELINES.md 추가
5. DEVELOPMENT_ROADMAP.md 추가
6. WORK_LOG.md 추가
7. PROMPT_GUIDE.md 추가
8. app.py 기본 화면 생성
9. Phase 1 PDF 업로드 기능 구현
```

초기 목표는 다음 문장이 성립하는 것이다.

```text
사용자가 PDF를 업로드하면 파일이 저장되고, 그 PDF에서 텍스트 일부를 추출해 화면에 보여준다.
```
