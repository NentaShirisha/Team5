import streamlit as st
from streamlit_option_menu import option_menu
import os
from pages.inclusive_companion import show_inclusive_companion
from pages.fan_engagement import show_fan_engagement

# Page configuration
st.set_page_config(
    page_title="Ai.lonso - F1 Digital Companion",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .feature-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
    }
    .stButton > button {
        background-color: #1f77b4;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #0d5aa7;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🏎️ Ai.lonso - F1 Digital Companion</h1>', unsafe_allow_html=True)
    
    # Sidebar navigation
    with st.sidebar:
        # Try to load logo, fallback to text if not available
        try:
            st.image("assets/ai_lonso_logo.png", width=200)
        except:
            st.markdown("### 🏎️ Ai.lonso")
            st.markdown("*F1 Digital Companion*")
        
        selected = option_menu(
            menu_title="Navigation",
            options=["Home", "Inclusive Companion", "Fan Engagement"],
            icons=["house", "accessibility", "emoji-heart-eyes"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "#1f77b4", "font-size": "20px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "#1f77b4"},
            }
        )
    
    # Main content based on selection
    if selected == "Home":
        show_home_page()
    elif selected == "Inclusive Companion":
        show_inclusive_companion()
    elif selected == "Fan Engagement":
        show_fan_engagement()

def show_home_page():
    st.markdown("""
    ## Welcome to Ai.lonso - The Future of F1 Fan Experience! 🏁
    
    Ai.lonso is a revolutionary AI-powered digital companion designed to make Formula 1 racing accessible, 
    engaging, and inclusive for fans of all backgrounds and abilities.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🧑‍🤝‍🧑 Inclusive Digital Companion
        
        Making F1 accessible for everyone:
        - **Sign Language Avatar**: Live race commentary in sign language
        - **Haptic Vibrations**: Feel the race through vibrations
        - **Emotional Mirror**: AI reflects your emotions in real-time
        - **Memory Palace**: Connect current events with F1 history
        - **Multilingual Commentary**: Simplified commentary for all fans
        """)
        
        if st.button("Explore Inclusive Features", key="inclusive_btn"):
            st.switch_page("pages/inclusive_companion.py")
    
    with col2:
        st.markdown("""
        ### 🎉 Viral Fan Engagement Engine
        
        Creating shareable F1 moments:
        - **Meme Generator**: Turn race moments into viral memes
        - **Reel Creator**: Auto-generate highlight videos
        - **Photo Generator**: AR selfies with drivers and cars
        - **Pit-Stop Game**: Fun mini-games with leaderboards
        - **Live Chatbot**: Real-time Q&A with AI.lonso
        - **Fan Polls**: Gamified predictions and voting
        """)
        
        if st.button("Explore Engagement Features", key="engagement_btn"):
            st.switch_page("pages/fan_engagement.py")
    
    # Demo section
    st.markdown("---")
    st.markdown("### 🚀 Quick Demo")
    
    demo_col1, demo_col2, demo_col3 = st.columns(3)
    
    with demo_col1:
        st.markdown("""
        **Try the Meme Generator:**
        Upload any image and create F1-themed memes instantly!
        """)
    
    with demo_col2:
        st.markdown("""
        **Experience Emotional Mirror:**
        Use your webcam to see Ai.lonso mirror your emotions!
        """)
    
    with demo_col3:
        st.markdown("""
        **Play Pit-Stop Game:**
        Test your reflexes in our tire-changing mini-game!
        """)

if __name__ == "__main__":
    main()
