"""
Paper AI Agent - 메인 애플리케이션
FastAPI 앱 초기화 및 실행
"""
from fastapi import FastAPI
from api.routes import router
import uvicorn


# FastAPI 앱 생성
app = FastAPI(
    title="Paper AI Agent",
    description="논문 PDF를 업로드하면 AI 에이전트가 자율적으로 분석하는 API",
    version="1.0.0"
)
# API 라우터 등록
app.include_router(router)


if __name__ == "__main__":
    # 서버 실행
    uvicorn.run(app, host="0.0.0.0", port=8000)