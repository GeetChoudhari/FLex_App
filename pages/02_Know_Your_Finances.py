import streamlit as st
import plotly.express as px
import pandas as pd
from utils import load_css, display_sidebar, calculate_financial_score, get_savings_allocation
from config import PROFILE_OPTIONS

# Configure page
st.set_page_config(
    page_title="Know Your Finances - FLex",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_css()

# Display sidebar
display_sidebar()

# Page header
st.markdown("<div class='main-header'>Know Your Finances</div>", unsafe_allow_html=True)

# Check if profile exists or edit requested
if 'profile_complete' not in st.session_state or st.session_state.get('edit_profile', False):
    if 'edit_profile' in st.session_state:
        del st.session_state.edit_profile
        
    st.info("Let's get to know your financial situation to provide personalized guidance.")
    
    # Financial profile form
    with st.form("financial_profile"):
        st.write("### Basic Information")
        name = st.text_input("Name", value=st.session_state.get('user_name', ''))
        age = st.number_input("Age", min_value=16, max_value=100, value=st.session_state.get('user_age', 20))
        
        status_options = PROFILE_OPTIONS["status"]
        status = st.selectbox("Status", 
                             status_options,
                             index=status_options.index(st.session_state.get('user_status', "Undergraduate")) if st.session_state.get('user_status') in status_options else 0)
        
        st.write("### Financial Snapshot")
        income_options = PROFILE_OPTIONS["income"]
        income = st.selectbox("Monthly Income", 
                             income_options,
                             index=income_options.index(st.session_state.get('user_income', "$0-500")) if st.session_state.get('user_income') in income_options else 0)
        
        savings_options = PROFILE_OPTIONS["savings"]
        savings = st.selectbox("Current Savings", 
                              savings_options,
                              index=savings_options.index(st.session_state.get('user_savings', "$0-100")) if st.session_state.get('user_savings') in savings_options else 0)
        
        debt_options = PROFILE_OPTIONS["debt"]
        debt = st.selectbox("Current Debt", 
                           debt_options,
                           index=debt_options.index(st.session_state.get('user_debt', "None")) if st.session_state.get('user_debt') in debt_options else 0)
        
        st.write("### Financial Goals")
        goals = st.multiselect(
            "Select your top financial goals",
            PROFILE_OPTIONS["goals"],
            default=st.session_state.get('user_goals', ["Emergency Fund"])
        )
        
        submitted = st.form_submit_button("Save My Profile")
        if submitted:
            st.session_state.user_name = name
            st.session_state.user_age = age
            st.session_state.user_status = status
            st.session_state.user_income = income
            st.session_state.user_savings = savings
            st.session_state.user_debt = debt
            st.session_state.user_goals = goals
            st.session_state.profile_complete = True
            st.success("Profile saved! Refreshing with your personalized insights...")
            st.experimental_rerun()

# If profile is complete, show personalized recommendations
else:
    st.markdown(f"### Hello, {st.session_state.user_name}!")
    st.markdown("<div class='highlight'>Based on your profile, here are your personalized recommendations:</div>", unsafe_allow_html=True)
    
    # Financial health overview
    st.markdown("### Your Financial Health")
    
    # Calculate financial health score
    financial_score = calculate_financial_score()
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Financial health visualization
        st.markdown(f"Financial Health Score: {financial_score}/100")
        st.progress(financial_score/100)
        
        # Score interpretation
        if financial_score < 40:
            st.warning("You're at the beginning of your financial journey. Focus on building stability.")
        elif financial_score < 70:
            st.info("You're on the right track. Continue building your financial foundation.")
        else:
            st.success("You're doing well! Focus on growth and future planning.")
    
    with col2:
        st.markdown("#### Action Items:")
        
        # Personalized action items based on profile
        action_items = []
        
        # Check savings
        if st.session_state.user_savings in ["$0-100", "$101-500"]:
            action_items.append("• Build emergency fund of at least $1,000")
        
        # Check debt
        if st.session_state.user_debt not in ["None", "Less than $1000"]:
            action_items.append("• Focus on paying down high-interest debt")
        
        # Check income vs savings
        if st.session_state.user_income in ["$1001-2000", "$2001-3000", "$3000+"] and st.session_state.user_savings in ["$0-100", "$101-500"]:
            action_items.append("• Increase savings rate to at least 15% of income")
        
        # If doing well, suggest investing
        if financial_score > 60:
            action_items.append("• Consider starting with low-risk investments")
        
        # If no specific actions generated, provide default
        if not action_items:
            action_items = ["• Continue current financial habits", "• Review your budget monthly", "• Consider learning about investing"]
        
        # Display action items
        st.markdown("\n".join(action_items))
    
    # Recommendations section
    st.markdown("### Personalized Recommendations")
    
    tab1, tab2 = st.tabs(["Savings Strategy", "Investment Options"])
    
    with tab1:
        # Different savings strategies based on user situation
        if st.session_state.user_debt in ["$5001-25000", "$25000+"]:
            st.markdown("Based on your current debt level, we recommend a debt-focused savings strategy:")
            st.markdown("• 50% for Essentials\n• 20% for Debt Repayment\n• 20% for Emergency Fund\n• 10% for Flexible Spending")
        elif st.session_state.user_income in ["$0-500", "$501-1000"]:
            st.markdown("With your current income level, focus on a simplified savings approach:")
            st.markdown("• 60% for Essentials\n• 20% for Emergency Fund\n• 20% for Education & Flexible Spending")
        else:
            st.markdown("Based on your profile, we recommend a balanced savings strategy:")
            st.markdown("• 50% for Essentials\n• 30% for Financial Goals\n• 20% for Flexible Spending")
        
        # Get savings allocation data
        savings_data = get_savings_allocation(st.session_state.user_debt, st.session_state.user_income)
        
        # Pie chart for savings allocation
        fig = px.pie(
            savings_data, 
            values='Percentage', 
            names='Category', 
            title="Recommended Budget Allocation",
            color_discrete_sequence=px.colors.sequential.Blues
        )
        st.plotly_chart(fig)
        
    with tab2:
        st.markdown("When you're ready to invest, consider these options based on your profile:")
        
        # Different investment recommendations based on profile
        if financial_score < 50:
            st.markdown("Before investing, focus on building a solid financial foundation:")
            st.markdown("• High-yield savings account for emergency fund\n• Pay down high-interest debt first\n• Learn about investment basics while saving")
        else:
            st.markdown("Based on your profile, consider these beginner-friendly investments:")
            st.markdown("• Low-cost index funds (S&P 500 index funds)\n• Target-date retirement funds\n• Education-focused accounts (529 plans)")
            
            # Simple investment comparison
            investment_data = pd.DataFrame({
                'Option': ['High-Yield Savings', 'Index Funds', 'Target-Date Funds'],
                'Risk Level': ['Very Low', 'Moderate', 'Moderate'],
                'Potential Return': ['1-2%', '7-10%', '6-9%'],
                'Minimum Investment': ['$0', '$0-100', '$0-1000'],
                'Best For': ['Emergency Fund', 'Long-term Growth', 'Retirement']
            })
            
            st.dataframe(investment_data, hide_index=True)
    
    # Profile options
    with st.expander("Profile Options"):
        if st.button("Edit Profile"):
            st.session_state.edit_profile = True
            st.experimental_rerun()
        
        if st.button("Reset Profile (Demo)"):
            for key in ['profile_complete', 'user_name', 'user_age', 'user_status', 
                        'user_income', 'user_savings', 'user_debt', 'user_goals', 'edit_profile']:
                if key in st.session_state:
                    del st.session_state[key]
            st.experimental_rerun()

# Footer
st.markdown("<div class='footer'>FLex - Financial Literacy Assistant for Students<br>Educational purposes only. Not financial advice.</div>", unsafe_allow_html=True)