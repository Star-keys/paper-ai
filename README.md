# Paper AI Agent

논문 PDF를 분석하는 AI 에이전트 시스템

## 기능

### 1. 논문 요약 에이전트 (PaperAnalysisAgent)
- 논문의 핵심 내용을 간결하게 요약
- 연구 주제, 방법론, 주요 결과를 10줄 이내로 정리
- **엔드포인트**: `POST /papers/{paper_id}/analyze`

### 2. 과학자 에이전트 (ScientistAgent)
새로운 가설을 세우려는 연구자 관점에서 논문 분석
- **연구 핵심 요약**: 논문의 주제, 방법론, 발견 정리
- **연구 갭(Gap) 분석**: 논문의 한계점과 추가 연구 필요 영역 발견
- **새로운 가설 제안**: 논문 기반 2-3개의 연구 가설 제시
- **후속 연구 아이디어**: 가설 검증을 위한 실험 설계 및 연구 방법 제안
- **엔드포인트**: `POST /papers/{paper_id}/scientist`

## API 엔드포인트

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/` | 헬스체크 |
| POST | `/papers/{paper_id}/analyze` | 논문 요약 분석 |
| POST | `/papers/{paper_id}/scientist` | 과학자 관점 분석 |

## 실행 방법

```bash
python main.py
```

서버 실행 후 http://localhost:8000 접속

## Contact

Email us: zoloman316@gmail.com
