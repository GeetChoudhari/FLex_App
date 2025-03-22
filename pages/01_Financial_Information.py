import streamlit as st
from utils import load_css, display_sidebar, get_financial_term_content
from config import POPULAR_TERMS

# Configure page
st.set_page_config(
    page_title="Financial Information - FLex",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_css()

# Display sidebar
display_sidebar()

# Page header
st.markdown("<div class='main-header'>Financial Information</div>", unsafe_allow_html=True)

# Introduction
st.markdown("""
Financial terms can be confusing when you're just starting out. FLex makes them easy to understand,
with explanations specifically designed for students and beginners.
""")

# Search bar for financial terms
term_query = st.text_input("Search for a financial term or concept:", placeholder="e.g., compound interest, ETF, 401k")

# Quick access buttons for common terms
st.markdown("### Popular Topics:")
cols = st.columns(4)

for i, term in enumerate(POPULAR_TERMS):
    col_idx = i % 4
    if cols[col_idx].button(term, key=f"term_{i}"):
        term_query = term

# Results area (shows up when a search is performed)
if term_query or 'last_term' in st.session_state:
    term = term_query if term_query else st.session_state.last_term
    st.session_state.last_term = term
    
    st.markdown(f"### {term.title()}")
    
    # Get content for the selected term
    term_data = get_financial_term_content(term)
    
    # Simple explanation tab
    with st.expander("Simple Explanation", expanded=True):
        st.markdown(f"<div class='highlight'>{term_data['content']}</div>", unsafe_allow_html=True)
    
    # Examples tab
    with st.expander("Real-world Examples"):
        st.markdown(term_data['examples'])
    
    # Learn more tab
    with st.expander("Learn More"):
        st.write("Additional resources and links would appear here.")
    
    # Related terms
    st.markdown("### Related Terms")
    related_cols = st.columns(len(term_data['related']))
    for i, rel_term in enumerate(term_data['related']):
        if related_cols[i].button(rel_term, key=f"related_{i}"):
            st.session_state.last_term = rel_term
            st.experimental_rerun()

# Footer
st.markdown("<div class='footer'>FLex - Financial Literacy Assistant for Students<br>Educational purposes only. Not financial advice.</div>", unsafe_allow_html=True)