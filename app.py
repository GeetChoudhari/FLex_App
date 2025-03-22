import streamlit as st
from utils import load_css, display_sidebar

# Configuration
st.set_page_config(
    page_title="FLex - Financial Literacy Assistant",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_css()

# Display sidebar
display_sidebar()

# Home page content
st.markdown("<div class='main-header'>Welcome to FLex</div>", unsafe_allow_html=True)

# About FLex section
st.markdown("""
### About FLex

**FLex** (Financial Literacy Expert) is an AI-powered assistant designed specifically for students and beginners
in the world of finance. Our mission is to simplify financial concepts, help you understand your own financial 
situation, and keep you informed about relevant market trends - all in language that's easy to understand.
""")

st.markdown("<div class='subheader'>Why Financial Literacy Matters</div>", unsafe_allow_html=True)
st.markdown("""
* 76% of college students wish they had more help preparing for financial decisions
* Understanding basic financial concepts can lead to better debt management
* Early financial literacy leads to stronger long-term financial outcomes
* Many students graduate without understanding critical financial tools
""")

# Feature tiles for home page
st.markdown("<div class='subheader'>How FLex Can Help You</div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='tile-header'>📚 Financial Information</div>", unsafe_allow_html=True)
    st.markdown("<div class='info-box'>Learn financial terms and concepts in simple language with real-world examples relevant to students.</div>", unsafe_allow_html=True)
    if st.button("Explore Finance Terms", key="btn_terms"):
        st.switch_page("pages/01_Financial_Information.py")

with col2:
    st.markdown("<div class='tile-header'>💼 Know Your Finances</div>", unsafe_allow_html=True)
    st.markdown("<div class='info-box'>Get personalized advice based on your financial situation, goals, and student status.</div>", unsafe_allow_html=True)
    if st.button("Analyze My Finances", key="btn_analyze"):
        st.switch_page("pages/02_Know_Your_Finances.py")

with col3:
    st.markdown("<div class='tile-header'>📈 Current Market</div>", unsafe_allow_html=True)
    st.markdown("<div class='info-box'>Get updates on interest rates and market performance focusing on what matters to students.</div>", unsafe_allow_html=True)
    if st.button("Check Markets", key="btn_markets"):
        st.switch_page("pages/03_Current_Market.py")

# How it works section
st.markdown("<div class='subheader'>How It Works</div>", unsafe_allow_html=True)
st.markdown("""
FLex combines advanced AI technology with financial expertise to provide personalized guidance:

1. **Real-Time Data**: We pull information from trusted financial sources 
2. **Simplified Explanations**: Complex terms translated into everyday language
3. **Personalized Insights**: Advice tailored to your specific student financial situation
4. **Educational Focus**: Everything is presented as a learning opportunity
""")

# Testimonials
st.markdown("<div class='subheader'>What Students Say</div>", unsafe_allow_html=True)
quotes_col1, quotes_col2 = st.columns(2)

with quotes_col1:
    st.markdown("<div class='info-box'><em>\"FLex helped me understand how student loans actually work in a way that finally made sense.\"</em><br>— Jamie, Undergraduate Student</div>", unsafe_allow_html=True)

with quotes_col2:
    st.markdown("<div class='info-box'><em>\"I had no idea what to do with my first paycheck until FLex helped me create a simple budget.\"</em><br>— Taylor, Graduate Student</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>FLex - Financial Literacy Assistant for Students<br>Educational purposes only. Not financial advice.</div>", unsafe_allow_html=True)