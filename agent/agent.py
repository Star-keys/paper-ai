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
다음 논문을 분석하여 한글로 간결하게 요약해주세요.

논문 내용:
{paper_content}

**중요: 10줄 이내로 핵심만 요약하세요.**

다음을 포함하세요:
- 연구 주제 및 목적 (2-3줄)
- 핵심 방법론 (2-3줄)
- 주요 결과 및 기여 (2-3줄)

요약:
""")

        # Gemini 모델
        model = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-exp",
            google_api_key=os.getenv("GEMINI_API_KEY"),
            temperature=0  # 다향성 0 조절 =>  항상 같은 값
        )

        # 출력 파서
        output_parser = StrOutputParser()

        # 체인 생성 (파이프라인)
        self.chain = prompt | model | output_parser

    def analyze(self, paper_text: str):
        """
        논문 분석 실행 (스트리밍)

        Args:
            paper_text: 논문 전체 텍스트

        Yields:
            분석 결과 청크 (실시간 스트리밍)
        """
        # 체인 스트리밍 실행
        for chunk in self.chain.stream({'paper_content': paper_text[:5000]}):
            yield chunk


class ScientistAgent:
    """과학자 역할 에이전트 - 새로운 가설 제안"""

    def __init__(self):
        """체인 초기화"""
        # 프롬프트 템플릿
        prompt = ChatPromptTemplate.from_template("""
당신은 새로운 가설을 세우려는 과학자입니다.
다음 논문을 분석하여 연구 기회를 발견하고 새로운 가설을 제시하세요.

논문 내용:
{paper_content}

다음 형식으로 분석하세요:

## 1. 연구 핵심 요약 (3-4줄)
- 이 논문의 주제, 방법론, 주요 발견을 간단히 정리

## 2. 연구 갭(Gap) 분석
- 이 논문에서 다루지 못한 부분이나 한계점
- 추가 연구가 필요한 영역

## 3. 새로운 가설 제안
- 이 논문을 기반으로 제시할 수 있는 새로운 연구 가설 2-3개
- 각 가설이 왜 중요한지 설명

## 4. 후속 연구 아이디어
- 제안한 가설을 검증하기 위한 실험 설계 또는 연구 방법
- 필요한 데이터나 기술

분석:
""")

        # Gemini 모델
        model = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-exp",
            google_api_key=os.getenv("GEMINI_API_KEY"),
            temperature=0.3  # 창의성 약간 추가
        )

        # 출력 파서
        output_parser = StrOutputParser()

        # 체인 생성
        self.chain = prompt | model | output_parser

    def analyze(self, paper_text: str):
        """
        과학자 관점 분석 실행 (스트리밍)

        Args:
            paper_text: 논문 전체 텍스트

        Yields:
            분석 결과 청크 (실시간 스트리밍)
        """
        # 체인 스트리밍 실행
        for chunk in self.chain.stream({'paper_content': paper_text[:5000]}):
            yield chunk
