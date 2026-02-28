## Importing libraries and files
import os
# ...existing code...
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent

from tools import search_tool, read_data_tool

# Import ChatOpenAI with fallbacks for different langchain versions
ChatOpenAI = None
_candidates = [
    "langchain.chat_models",
    "langchain.chat_models.openai",
    "langchain_core.chat_models.openai",
    "langchain.chat_models.base",
    "langchain_community.chat_models",
    "langchain_community.chat_models.openai",
]
for _mod in _candidates:
    try:
        _m = __import__(_mod, fromlist=["ChatOpenAI"])
        ChatOpenAI = getattr(_m, "ChatOpenAI", None)
        if ChatOpenAI is not None:
            break
    except Exception:
        ChatOpenAI = None

if ChatOpenAI is None:
    raise ImportError("ChatOpenAI class not found in installed langchain. Install a compatible langchain or update imports.")

### Loading LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Creating an Experienced Financial Analyst agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Provide comprehensive investment advice based on financial documents: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You're an experienced financial analyst with deep knowledge of markets and investment strategies. "
        "You carefully read financial reports and identify key opportunities and risks. "
        "You provide evidence-based investment recommendations grounded in financial analysis. "
        "You follow regulatory compliance guidelines and provide responsible financial guidance. "
        "You make conservative estimates and highlight uncertainty in predictions. "
        "You provide thorough analysis of financial metrics and market fundamentals."
    ),
    tools=[read_data_tool],
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=True
)

# Creating a document verifier agent
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify that uploaded documents are valid financial documents and extract key information",
    verbose=True,
    memory=True,
    backstory=(
        "You're a document verification specialist with experience in compliance and financial document validation. "
        "You carefully examine documents to ensure they contain financial information. "
        "You accurately identify financial metrics, dates, and key sections. "
        "You maintain high standards for regulatory accuracy and documentation completeness."
    ),
    tools=[read_data_tool],
    llm=llm,
    max_iter=2,
    max_rpm=10,
    allow_delegation=False
)

investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide tailored investment recommendations based on financial analysis: {query}",
    verbose=True,
    backstory=(
        "You're a certified investment advisor with expertise in portfolio management and asset allocation. "
        "You understand different investment vehicles and market conditions. "
        "You provide recommendations suitable to risk profiles and investment objectives. "
        "You base recommendations on thorough financial analysis and market research. "
        "You maintain professional standards in all investment advice. "
        "You clearly disclose risks and uncertainties in your recommendations."
    ),
    tools=[read_data_tool],
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=False
)

risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal="Conduct thorough risk analysis of financial documents and provide mitigation strategies: {query}",
    verbose=True,
    backstory=(
        "You're an expert in financial risk analysis and portfolio risk management. "
        "You have quantitative knowledge of risk metrics and hedging strategies. "
        "You evaluate market, credit, and operational risks comprehensively. "
        "You provide realistic and evidence-based risk assessments. "
        "You align risk recommendations with regulatory standards and best practices. "
        "You help clients understand and manage risk within appropriate parameters."
    ),
    tools=[read_data_tool],
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=False
)
