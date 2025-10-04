"""
FastAPI 라우트 정의
API 엔드포인트만 관리
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from agent.agent import PaperAnalysisAgent
from database.mock_db import db


# 라우터 생성 (나중에 main.py에서 등록)
router = APIRouter()

# 에이전트 인스턴스 (앱 시작 시 한 번만 생성)
agent = PaperAnalysisAgent()


class PaperSummary(BaseModel):
    """논문 요약 정보"""
    id: int
    title: str
    authors: str
    year: int


class AnalysisResponse(BaseModel):
    """분석 결과 응답 모델"""
    paper_id: int
    title: str
    analysis: str


@router.get("/")
async def root():
    """헬스체크 엔드포인트"""
    return {
        "message": "Paper AI Agent API",
        "status": "running",
        "version": "1.0.0"
    }


@router.get("/papers", response_model=List[PaperSummary])
async def get_papers():
    """
    모든 논문 목록 조회

    Returns:
        List[PaperSummary]: 논문 목록
    """
    papers = db.get_all_papers()
    return [
        PaperSummary(
            id=p["id"],
            title=p["title"],
            authors=p["authors"],
            year=p["year"]
        )
        for p in papers
    ]


@router.post("/papers/{paper_id}/analyze", response_model=AnalysisResponse)
async def analyze_paper(paper_id: int):
    """
    DB에 저장된 논문을 에이전트가 분석

    Args:
        paper_id: 분석할 논문 ID

    Returns:
        AnalysisResponse: 에이전트의 분석 결과

    Raises:
        HTTPException: 논문을 찾을 수 없거나 분석 실패 시
    """
    try:
        # 1. DB에서 논문 조회
        paper = db.get_paper_by_id(paper_id)

        if not paper:
            raise HTTPException(
                status_code=404,
                detail=f"논문 ID {paper_id}를 찾을 수 없습니다."
            )

        # 2. 에이전트 실행
        analysis_result = agent.analyze(paper["content"])

        # 3. 결과 반환
        return AnalysisResponse(
            paper_id=paper["id"],
            title=paper["title"],
            analysis=analysis_result
        )

    except HTTPException:
        # HTTPException은 그대로 재발생
        raise

    except Exception as e:
        # 그 외 예외는 500 에러로 변환
        raise HTTPException(
            status_code=500,
            detail=f"논문 분석 중 오류가 발생했습니다: {str(e)}"
        )
