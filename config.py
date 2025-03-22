# Application configuration settings

# Default page title
APP_TITLE = "FLex - Financial Literacy Assistant"

# Custom CSS for styling
CUSTOM_CSS = """
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 1rem;
    }
    .tile-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 0.5rem;
    }
    .info-box {
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .highlight {
        background-color: #DBEAFE;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .subheader {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1E3A8A;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    .footer {
        font-size: 0.8rem;
        color: #6B7280;
        text-align: center;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #E5E7EB;
    }
</style>
"""

# Popular financial terms for quick access
POPULAR_TERMS = [
    "Budgeting", 
    "Student Loans", 
    "Credit Scores", 
    "Investing Basics", 
    "Emergency Fund", 
    "Compound Interest", 
    "Taxes for Students", 
    "Checking vs. Savings"
]

# Financial profile form options
PROFILE_OPTIONS = {
    "status": ["High School Student", "Undergraduate", "Graduate", "Recent Graduate"],
    "income": ["$0-500", "$501-1000", "$1001-2000", "$2001-3000", "$3000+"],
    "savings": ["$0-100", "$101-500", "$501-1000", "$1001-5000", "$5000+"],
    "debt": ["None", "Less than $1000", "$1000-5000", "$5001-25000", "$25000+"],
    "goals": ["Emergency Fund", "Pay Off Debt", "Save for Education", "Start Investing", "Major Purchase"]
}

# API configuration (for future implementation)
API_CONFIG = {
    "polygon_api_key": "", # To be filled when implemented
    "yahoo_finance_enabled": True,
    "duckduckgo_enabled": True
}

# LLM configuration (for future implementation)
LLM_CONFIG = {
    "model": "Palmyra-Fin-70B-32K",
    "temperature": 0.7,
    "max_tokens": 1024
}