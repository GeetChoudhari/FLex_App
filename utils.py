import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from config import CUSTOM_CSS

def load_css():
    """Load custom CSS styles"""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

def display_sidebar():
    """Display sidebar navigation and user profile"""
    with st.sidebar:
        st.markdown("# FLex 💰")
        st.markdown("### Your Financial Literacy Assistant")
        
        # Navigation header
        st.markdown("## Navigation")
        
        # Native Streamlit navigation links - avoids query param issues
        st.page_link("app.py", label="🏠 Home", icon=None)
        st.page_link("pages/01_Financial_Information.py", label="📚 Financial Information", icon=None)
        st.page_link("pages/02_Know_Your_Finances.py", label="💼 Know Your Finances", icon=None)
        st.page_link("pages/03_Current_Market.py", label="📈 Current Market", icon=None)
        
        # User profile section
        st.markdown("---")
        with st.expander("Your Profile"):
            if 'user_name' in st.session_state:
                st.write(f"Hi, {st.session_state.user_name}!")
                st.write(f"Status: {st.session_state.get('user_status', 'Student')}")
                if st.button("Edit Profile"):
                    st.session_state.edit_profile = True
                    # Use native page navigation
                    st.switch_page("pages/02_Know_Your_Finances.py")
            else:
                st.write("Please complete your profile in 'Know Your Finances'")
                if st.button("Create Profile"):
                    # Use native page navigation
                    st.switch_page("pages/02_Know_Your_Finances.py")
        
        # Footer in sidebar
        st.markdown("---")
        st.markdown("Powered by Palmyra-Fin-70B")

def calculate_financial_score():
    """Calculate a financial health score based on user profile"""
    # This is a simplified mock calculation
    score = 50  # Base score
    
    # Add points for savings
    savings_map = {"$0-100": 0, "$101-500": 5, "$501-1000": 10, "$1001-5000": 15, "$5000+": 20}
    score += savings_map.get(st.session_state.user_savings, 0)
    
    # Deduct for debt
    debt_map = {"None": 0, "Less than $1000": -5, "$1000-5000": -10, "$5001-25000": -15, "$25000+": -20}
    score += debt_map.get(st.session_state.user_debt, 0)
    
    # Add for income
    income_map = {"$0-500": 5, "$501-1000": 10, "$1001-2000": 15, "$2001-3000": 20, "$3000+": 25}
    score += income_map.get(st.session_state.user_income, 0)
    
    # Ensure score is between 0-100
    return max(0, min(100, score))

def get_financial_term_content(term):
    """Get content for a financial term"""
    term = term.lower()
    
    # Dictionary of financial terms and their explanations
    terms = {
        "budgeting": {
            "content": """
            Budgeting is simply a plan for how you'll spend your money each month. Think of it like a food plan for your wallet!
            
            It helps you make sure you have enough money for the things you need (like rent and food) before spending on things you want (like entertainment).
            """,
            "examples": """
            **Student Example**: Maria receives $1,200 monthly from her part-time job and financial aid. Her simple budget is:
            - Rent & Utilities: $600 (50%)
            - Groceries: $240 (20%)
            - Transportation: $120 (10%)
            - School Supplies: $120 (10%)
            - Fun Money: $120 (10%)
            
            By tracking these categories using a simple app, Maria knows exactly when she can afford to go out with friends.
            """,
            "related": ["Emergency Fund", "50/30/20 Rule", "Expense Tracking"]
        },
        "student loans": {
            "content": """
            Student loans are money borrowed to pay for college or university. Unlike scholarships or grants, loans must be paid back, usually with interest.
            
            Federal student loans come from the government and typically have more flexible repayment options than private loans from banks or other lenders.
            """,
            "examples": """
            **Student Example**: Alex borrowed $20,000 in federal student loans at 4.5% interest. 
            
            After graduation, Alex's monthly payment is about $207 on a standard 10-year repayment plan. The total paid over 10 years will be approximately $24,840 - meaning $4,840 goes to interest.
            
            By making an extra $50 payment each month, Alex could pay off the loan 2 years earlier and save about $1,200 in interest.
            """,
            "related": ["Loan Subsidization", "Repayment Plans", "Loan Forgiveness"]
        },
        "credit scores": {
            "content": """
            A credit score is like a financial report card that shows how reliable you are with borrowing and repaying money. 
            
            Scores typically range from 300-850, with higher scores showing better credit management. Your score affects whether you can get loans, credit cards, apartments, and even some jobs.
            """,
            "examples": """
            **Student Example**: Jordan got their first credit card in college with a $500 limit. By making small purchases and paying the balance in full each month, Jordan built a credit score of 720 within two years.
            
            When Jordan graduated and wanted to rent an apartment, the landlord checked their credit score. Having a good score meant Jordan didn't need a co-signer and got approved easily.
            """,
            "related": ["Credit Reports", "Credit Utilization", "Payment History"]
        },
        "investing basics": {
            "content": """
            Investing means putting money into something with the hope it will grow over time. It's different from saving because it involves some risk, but generally offers higher potential returns.
            
            Common beginner investments include stocks (ownership in companies), bonds (loans to companies or governments), and funds (collections of stocks/bonds).
            """,
            "examples": """
            **Student Example**: Chris started investing with just $25 a month in a low-cost index fund through a free investing app while in sophomore year.
            
            By graduation 2.5 years later, Chris had invested about $750 total, but the account had grown to $840 (a 12% return). Chris learned that starting early, even with small amounts, takes advantage of compound growth.
            """,
            "related": ["Index Funds", "Compound Growth", "Risk Tolerance"]
        }
    }
    
    # Return term content if it exists, otherwise return generic content
    if term in terms:
        return terms[term]
    else:
        return {
            "content": f"This would contain a simple, student-friendly explanation of {term}.",
            "examples": "This section would show real-world examples of how this concept applies to student life.",
            "related": ["Term 1", "Term 2", "Term 3"]
        }

def generate_market_data():
    """Generate sample market data for demonstration"""
    import datetime
    
    today = datetime.date.today()
    dates = [today - datetime.timedelta(days=x) for x in range(30, 0, -1)]
    
    # Create sample performance data
    np.random.seed(42)  # For reproducible results
    
    spy_start = 460
    qqq_start = 440
    vti_start = 230
    
    spy_data = [spy_start]
    qqq_data = [qqq_start]
    vti_data = [vti_start]
    
    for i in range(1, 30):
        spy_data.append(spy_data[-1] * (1 + np.random.normal(0.0003, 0.008)))
        qqq_data.append(qqq_data[-1] * (1 + np.random.normal(0.0004, 0.01)))
        vti_data.append(vti_data[-1] * (1 + np.random.normal(0.0003, 0.007)))
    
    # Create DataFrame
    market_data = pd.DataFrame({
        'Date': dates,
        'S&P 500 (SPY)': spy_data,
        'NASDAQ (QQQ)': qqq_data,
        'Total Market (VTI)': vti_data
    })
    
    return market_data

def get_bank_data():
    """Get sample bank interest rate data"""
    bank_data = {
        'Bank': ['Student Credit Union', 'Bank A', 'Bank B', 'Online Bank', 'Credit Union'],
        'Savings Rate': [2.0, 1.5, 1.8, 2.5, 2.2],
        'CD Rate (1-year)': [3.5, 3.0, 3.2, 3.8, 3.6],
        'Student Account Perks': ['Yes', 'No', 'Yes', 'No', 'Yes']
    }
    
    return pd.DataFrame(bank_data)

def get_loan_data():
    """Get sample student loan interest rate data"""
    loan_data = {
        'Loan Type': ['Federal Undergraduate', 'Federal Graduate', 'Private (Good Credit)', 'Private (Average Credit)'],
        'Interest Rate': [5.5, 6.6, 7.2, 10.8]
    }
    
    return pd.DataFrame(loan_data)

def get_savings_allocation(user_debt, user_income):
    """Get recommended savings allocation based on user profile"""
    if user_debt in ["$5001-25000", "$25000+"]:
        return {
            'Category': ['Essentials', 'Debt Repayment', 'Emergency Fund', 'Flexible'],
            'Percentage': [50, 20, 20, 10]
        }
    elif user_income in ["$0-500", "$501-1000"]:
        return {
            'Category': ['Essentials', 'Emergency Fund', 'Education & Flexible'],
            'Percentage': [60, 20, 20]
        }
    else:
        return {
            'Category': ['Essentials', 'Financial Goals', 'Flexible'],
            'Percentage': [50, 30, 20]
        }