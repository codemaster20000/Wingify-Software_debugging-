## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from crewai.tools import tool

## Creating search tool (optional)
search_tool = None  # Placeholder for search functionality

## Creating custom pdf reader tool
@tool
def read_data_tool(filename: str = 'data/sample.pdf') -> str:
    """Tool to read data from a PDF file path
    
    Args:
        filename: Path of the pdf file. Defaults to 'data/sample.pdf'.
    
    Returns:
        str: Full Financial Document file content
    """
    
    try:
        docs = PyPDFLoader(file_path=filename).load()
        full_report = ""
        for data in docs:
            # Clean and format the financial document data
            content = data.page_content
            
            # Remove extra whitespaces and format properly
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
                
            full_report += content + "\n"
            
        return full_report
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

## Creating Investment Analysis Tool
class InvestmentTool:
    async def analyze_investment_tool(financial_document_data):
        # Process and analyze the financial document data
        processed_data = financial_document_data
        
        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
                
        # TODO: Implement investment analysis logic here
        return "Investment analysis functionality to be implemented"

## Creating Risk Assessment Tool
class RiskTool:
    async def create_risk_assessment_tool(financial_document_data):        
        # TODO: Implement risk assessment logic here
        return "Risk assessment functionality to be implemented"