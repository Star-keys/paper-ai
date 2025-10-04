"""
FastAPI 라우트 정의
API 엔드포인트만 관리
"""
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List
from agent.agent import PaperAnalysisAgent, ScientistAgent
from database.mock_db import db


# 라우터 생성 (나중에 main.py에서 등록)
router = APIRouter()

# 에이전트 인스턴스 (앱 시작 시 한 번만 생성)
summary_agent = PaperAnalysisAgent()
scientist_agent = ScientistAgent()


class PaperSummary(BaseModel):
    """논문 요약 정보"""
    id: int
    title: str
    authors: str
    year: int


class PaperDetail(BaseModel):
    """논문 상세 정보"""
    id: int
    title: str
    authors: str
    year: int
    abstract: str
    introduction: str
    method: str
    results: str


@router.get("/")
async def root():
    """헬스체크 엔드포인트"""
    return {
        "message": "Paper AI Agent API",
        "status": "running",
        "version": "1.0.0"
    }


@router.get("/papers", response_model=List[PaperDetail])
async def get_papers():
    """
    모든 논문 목록 조회 (섹션별 필드 포함)

    Returns:
        List[PaperDetail]: 논문 상세 정보 목록
    """
    papers = db.get_all_papers()
    return [
        PaperDetail(
            id=p["id"],
            title=p["title"],
            authors=p["authors"],
            year=p["year"],
            abstract=p["abstract"],
            introduction=p["introduction"],
            method=p["method"],
            results=p["results"]
        )
        for p in papers
    ]


@router.post("/papers/{paper_id}/analyze")
async def analyze_paper(paper_id: int):
    """
    DB에 저장된 논문을 스트리밍으로 분석

    Args:
        paper_id: 분석할 논문 ID

    Returns:
        StreamingResponse: 실시간 분석 결과

    Raises:
        HTTPException: 논문을 찾을 수 없는 경우
    """
    # 1. DB에서 논문 조회
    paper = db.get_paper_by_id(paper_id)

    if not paper:
        raise HTTPException(
            status_code=404,
            detail=f"논문 ID {paper_id}를 찾을 수 없습니다."
        )

    # 2. 논문 content 합치기
    paper_content = f"""
Abstract
{paper["abstract"]}

Introduction
{paper["introduction"]}

Method
{paper["method"]}

Results
{paper["results"]}
"""

    # 3. 스트리밍 응답 반환
    return StreamingResponse(
        summary_agent.analyze(paper_content),
        media_type="text/plain; charset=utf-8"
    )


@router.post("/papers/{paper_id}/scientist")
async def scientist_analyze(paper_id: int):
    """
    과학자 관점에서 논문 분석 (새로운 가설 제안)

    Args:
        paper_id: 분석할 논문 ID

    Returns:
        StreamingResponse: 실시간 분석 결과

    Raises:
        HTTPException: 논문을 찾을 수 없는 경우
    """
    # 1. DB에서 논문 조회
    paper = db.get_paper_by_id(paper_id)

    if not paper:
        raise HTTPException(
            status_code=404,
            detail=f"논문 ID {paper_id}를 찾을 수 없습니다."
        )

    # 2. 논문 content 합치기
    paper_content = f"""
Abstract
{paper["abstract"]}

Introduction
{paper["introduction"]}

Method
{paper["method"]}

Results
{paper["results"]}
"""

    # 3. 과학자 에이전트로 분석
    return StreamingResponse(
        scientist_agent.analyze(paper_content),
        media_type="text/plain; charset=utf-8"
    )
