import streamlit as st
import pandas as pd

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

# Intro page content
st.markdown('''
            # DEFINE-IO Priority Setting Workshop
            ## Goal: Build the UK's First IO Research Roadmap
            ### Why We Are Here:
            ''')
st.markdown('''
            <div style='font-size:22px; line-height:1.6;'>
            <li>

            **Gap:** Research in Interventional Oncology (IO) currently lacks a unified national strategy.</li>
            <li>

            **Need:** Limited funding requires us to focus resources on the **most critical** questions.</li>
            </div>
            ''', unsafe_allow_html=True)
st.divider()
st.markdown('''
            ### Today's Run-Down (15:15 - 17:00)
            ''')
table_1 = pd.DataFrame(
        {
        "**Activity**": [
            "Welcome & Introductions",
            "Phase 1 Finale: Round 3 Final priority scoring",
            "**Break**",
            "Phase 2: MCDA - Performance Scoring",
            "Phase 2: MCDA - Criteria Weighting",
            "Next Steps & Close",
        ],
        "**Focus**": [
            "Setting the stage; Overview of the day (**5 minutes**)",
            "Final review and clarification on research topics (**40 minutes**)",
            "**10-minute comfort and stretch break**",
            "Panellists score the top 25 priorities against the criteria (**30 minutes**)",
            "Group exercise to determine the relative importance of **Urgency, Feasibility/ Equipoise, & Affordability (20 minutes)**",
            "Discussion on dissemination; Thank you and close",
        ],
    }, index=["**15:15 - 15:20**", "**15:20 - 16:00**", "**16:00 - 16:10**", "**16:10 - 16:40**", "**16:40 - 17:00**", "**17:00**"]
)
table_1.index.name = "**Time**"
st.table(table_1, border=True)
st.divider()
st.markdown('''
            ### What We Do Today:
            ''')
table_2 = pd.DataFrame(
        {
        "**Method**": [
            "Round 3 e-Delphi Consensus",
            "Multi-Criteria Decision Analysis (MCDA)",
        ],
        "**Output**": [
            "Final list of top **25 research priorities**",
            "Priorities ranked by **Urgency, Feasibility, & Affordability**",
        ],
    }, index=["Phase 1 Finale", "Phase 2 Launch"]
)
table_2.index.name = "**Phase**"
st.table(table_2, border=True)
st.markdown('''
            <div style='font-size:22px; line-height:1.6;'>
              <br>
            
            **Thank you for your commitment to shaping the future of IO research!**
            </div>
            ''', unsafe_allow_html=True)