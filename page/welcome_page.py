import streamlit as st

#Set up every page
st.logo("images/UNITE.jpg", size="large")
st.image("images/DEFINEIO.png")
st.html("""
    <style>
        .stMainBlockContainer {
            max-width:60rem;
        }
    </style>
    """
)

# Welcome page content
st.markdown(''' # Welcome to the DEFINE-IO Priority Setting Workshop!''')
st.markdown('''
            <div style='font-size:22px; line-height:1.6;'>
            Dear Panellists,
            <br><br>

            A massive welcome to our in-person (and hybrid) session for the final stages of the **DEFINE-IO** study!\n\n

            Thank you so much for your commitment over the past few weeks. Your input across Rounds 1 and 2 of the e-Delphi has been invaluable, resulting in a synthesized list of the most critical research ideas for Interventional Oncology in the UK.
            </div>
            ''', unsafe_allow_html=True)
st.divider()
st.markdown('''
             ## What We Achieve Today
            
            <div style='font-size:22px; line-height:1.6;'>
            Today is where we translate those ideas into a strategic roadmap. This workshop is dedicated to the final two critical steps:
            <br><br>

            **1. Round 3: Final Delphi Consensus:** We'll quickly revisit the items where we still had some uncertainty after Round 2. Using the collective feedback and discussion from this session, you’ll submit your final, informed priority ratings.

            **2. Phase 2: Multi-Criteria Decision Analysis (MCDA):** This is the game-changer. We'll move beyond just 'importance' and use the MCDA framework to assess the top 25 priorities against real-world metrics: **Urgency, Feasibility/Equipoise, and Affordability**. This process is crucial for creating a truly actionable research strategy.
            <br><br>

            Your participation today is the most important step in establishing the first national research framework for Interventional Oncology. Let’s work together to shape the future of our specialty. 
            
            </div>
            ''', unsafe_allow_html=True)
st.divider()
st.markdown('''
            <div style='font-size:22px; line-height:1.6;'>
            Please grab a refreshment, check in with the team, and settle in. We’ll be starting promptly at 3:15 pm. 
            <br><br>

            Thank you, 
            <br><br>
            </div> 

            <div style='font-size:28px; line-height:1.6;'>

            **The DEFINE-IO Study Team**

            </div> 
            ''', unsafe_allow_html=True)
#TODO: Add Images of Study Team