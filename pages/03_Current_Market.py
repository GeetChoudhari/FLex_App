import streamlit as st
import datetime
import plotly.express as px
from utils import load_css, display_sidebar, generate_market_data, get_bank_data, get_loan_data

# Configure page
st.set_page_config(
    page_title="Current Market - FLex",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_css()

# Display sidebar
display_sidebar()

# Page header
st.markdown("<div class='main-header'>Current Market</div>", unsafe_allow_html=True)

# Introduction
st.markdown("""
Stay informed about financial markets with information curated for students.
We focus on what's most relevant for beginners and young investors.
""")

# Date display
today = datetime.date.today()
st.markdown(f"### Market Data as of {today.strftime('%B %d, %Y')}")

# Tabs for different market sections
market_tab1, market_tab2, market_tab3 = st.tabs(["Bank Rates", "Market Performance", "Student Insights"])

with market_tab1:
    st.markdown("### Bank Interest Rates")
    st.markdown("Compare current interest rates for accounts popular with students:")
    
    # Get bank data
    bank_df = get_bank_data()
    
    # Bar chart for interest rates
    fig = px.bar(
        bank_df, 
        x='Bank', 
        y=['Savings Rate', 'CD Rate (1-year)'],
        barmode='group',
        title="Current Interest Rates (%)",
        color_discrete_sequence=['#3B82F6', '#10B981']
    )
    st.plotly_chart(fig)
    
    # Bank comparison table
    st.markdown("### Student Account Comparison")
    st.dataframe(bank_df, hide_index=True)
    
    st.info("💡 **Tip:** Online banks often offer higher interest rates because they have lower overhead costs than traditional banks with physical branches.")

with market_tab2:
    # Market indices
    st.markdown("### Market Indices Performance")
    
    # Generate market data
    market_data = generate_market_data()
    
    # Line chart for market performance
    fig = px.line(
        market_data, 
        x='Date', 
        y=['S&P 500 (SPY)', 'NASDAQ (QQQ)', 'Total Market (VTI)'],
        title="30-Day Market Performance",
        labels={'value': 'Price', 'variable': 'Index'},
        color_discrete_sequence=['#2563EB', '#10B981', '#6366F1']
    )
    st.plotly_chart(fig)
    
    # Current metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        last_spy = market_data['S&P 500 (SPY)'].iloc[-1]
        spy_change = (last_spy - market_data['S&P 500 (SPY)'].iloc[-2]) / market_data['S&P 500 (SPY)'].iloc[-2] * 100
        st.metric("S&P 500 (SPY)", f"${last_spy:.2f}", f"{spy_change:.2f}%")
    
    with col2:
        last_qqq = market_data['NASDAQ (QQQ)'].iloc[-1]
        qqq_change = (last_qqq - market_data['NASDAQ (QQQ)'].iloc[-2]) / market_data['NASDAQ (QQQ)'].iloc[-2] * 100
        st.metric("NASDAQ (QQQ)", f"${last_qqq:.2f}", f"{qqq_change:.2f}%")
    
    with col3:
        last_vti = market_data['Total Market (VTI)'].iloc[-1]
        vti_change = (last_vti - market_data['Total Market (VTI)'].iloc[-2]) / market_data['Total Market (VTI)'].iloc[-2] * 100
        st.metric("Total Market (VTI)", f"${last_vti:.2f}", f"{vti_change:.2f}%")
    
    st.info("💡 **What this means:** These indices track the performance of large groups of stocks. They're often used as benchmarks to measure how well investments are performing.")

with market_tab3:
    st.markdown("### Student Financial Insights")
    
    # Student loan interest rates
    st.markdown("#### Current Student Loan Interest Rates")
    
    # Get loan data
    loan_df = get_loan_data()
    
    # Bar chart for loan rates
    fig = px.bar(
        loan_df,
        x='Loan Type',
        y='Interest Rate',
        title="Student Loan Interest Rates (%)",
        color_discrete_sequence=['#3B82F6']
    )
    st.plotly_chart(fig)
    
    # Recent news relevant to students
    st.markdown("### Beginner-Friendly Market News")
    
    with st.expander("What Rising Interest Rates Mean for Students", expanded=True):
        st.markdown("""
        Interest rates have increased over the past year. Here's what this means for students:
        
        * **Student Loans**: Variable rate private loans may see payment increases
        * **Savings Accounts**: Higher interest rates on savings (a good thing!)
        * **Credit Cards**: Higher interest on unpaid balances - try to pay in full each month
        * **Job Market**: Can impact hiring in some sectors as companies adjust spending
        
        **Action Item**: Now is a good time to check if your savings account is offering a competitive interest rate.
        """)
    
    with st.expander("Budget Apps Gaining Popularity Among Students"):
        st.markdown("""
        Recent surveys show more students are using budgeting apps to track expenses.
        
        Popular free options include:
        * Mint
        * EveryDollar
        * Personal Capital
        
        These apps can connect to your accounts and help categorize spending automatically,
        making it easier to see where your money goes each month.
        """)

# Disclaimer
st.markdown("---")
st.caption("Disclaimer: This information is for educational purposes only and not financial advice. Market data simulated for demonstration purposes.")