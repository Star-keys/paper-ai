"""
논문 분석 체인
LangChain을 사용한 간단한 논문 요약
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()


class PaperAnalysisAgent:
    """논문 분석 체인 클래스"""

    def __init__(self):
        """체인 초기화"""
        # 프롬프트 템플릿
        prompt = ChatPromptTemplate.from_template("""
다음 논문을 분석하여 한글로 요약해주세요.

논문 내용:
{paper_content}

다음을 포함한 분석 리포트를 작성하세요:
- 연구 주제 및 목적
- 핵심 방법론
- 주요 결과 및 기여

요약:
""")

        # Gemini 모델
        model = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-exp",
            google_api_key=os.getenv("GEMINI_API_KEY"),
            temperature=0.7
        )

        # 출력 파서
        output_parser = StrOutputParser()

        # 체인 생성 (파이프라인)
        self.chain = prompt | model | output_parser

    def analyze(self, paper_text: str) -> str:
        """
        논문 분석 실행

        Args:
            paper_text: 논문 전체 텍스트

        Returns:
            분석 결과 (한글 리포트)
        """
        # 체인 실행
        result = self.chain.invoke({'paper_content': paper_text[:5000]})  # 처음 5000자만
        return result
