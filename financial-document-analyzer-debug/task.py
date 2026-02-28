## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier
from tools import search_tool, read_data_tool

## Creating a task to help solve user's query
analyze_financial_document = Task(
    description="Analyze the financial document provided by the user to answer: {query}.\n\
Read the document carefully and extract relevant financial information.\n\
Identify key financial metrics, trends, and ratios.\n\
Provide well-reasoned analysis based on the actual document content.\n\
Reference specific sections and figures from the document.\n\
Give clear and comprehensive answers to the user's query.",

    expected_output="""Provide a detailed analysis in the following format:
- Executive Summary of key findings
- Relevant Financial Metrics (with actual numbers from the document)
- Analysis of trends and performance
- Identification of key risks and opportunities
- Clear references to specific document sections
- Evidence-based insights and conclusions""",

    agent=financial_analyst,
    tools=[read_data_tool],
    async_execution=False,
)

## Creating an investment analysis task
investment_analysis = Task(
    description="Analyze the financial document and provide investment recommendations for: {query}.\n\
Review financial metrics and performance indicators thoroughly.\n\
Identify investment opportunities backed by financial data.\n\
Consider market conditions and sector trends.\n\
Provide recommendations aligned with the financial analysis.\n\
Clearly explain the rationale for each recommendation.",

    expected_output="""Structured investment recommendations:
- Investment Thesis (based on financial analysis)
- Recommended Actions with rationale
- Target allocation if applicable
- Expected returns and timeframe
- Relevant risks to monitor
- Comparison with market benchmarks""",

    agent=financial_analyst,
    tools=[read_data_tool],
    async_execution=False,
)

## Creating a risk assessment task
risk_assessment = Task(
    description="Conduct a comprehensive risk assessment for: {query}.\n\
Analyze financial metrics to identify potential risks.\n\
Evaluate market volatility and sector-specific risks.\n\
Consider macroeconomic factors and their impact.\n\
Provide realistic risk scenarios based on financial data.\n\
Recommend risk mitigation strategies where appropriate.",

    expected_output="""Complete risk assessment including:
- Risk Identification (types and sources)
- Risk Quantification (where possible)
- Potential Impact Assessment
- Realistic Risk Scenarios
- Risk Mitigation Strategies
- Monitoring and Review Recommendations
- Risk Rating (Low/Medium/High with justification)""",

    agent=financial_analyst,
    tools=[read_data_tool],
    async_execution=False,
)

verification = Task(
    description="Verify that the uploaded document is a valid financial document for: {query}.\n\
Carefully read and validate the document structure and content.\n\
Confirm it contains legitimate financial information.\n\
Identify the document type and key financial sections.\n\
Check for completeness and data quality.",

    expected_output="""Document verification report:
- Document Type Classification
- Financial Information Confirmed (Yes/No)
- Key Sections Identified
- Data Quality Assessment
- Validation Status
- Any Data Quality Issues Found
- Recommendation for Analysis Proceeding""",

    agent=financial_analyst,
    tools=[read_data_tool],
    async_execution=False
)
