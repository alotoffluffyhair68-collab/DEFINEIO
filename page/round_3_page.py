import streamlit as st
import streamlit.components.v1 as components
import base64

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

st.markdown('''
            # DEFINE-IO Priority Setting Workshop
            ## Phase 1: Round 3 Final priority scoring
            ### Please follow the email link to begin scoring the statements for round 3
            ''')
st.markdown("")

st.markdown('''
            ### Round 3 Statement Review
            ''')
components.iframe(
    "https://docs.google.com/presentation/d/e/2PACX-1vR-CnSpmbKGJyd2pCjLyrySQJFagkWINzBUF99D4fPDcbH3PCEDxwvmlou7p3KAYg/pubembed?start=false&loop=false&delayms=60000",
    width=960,
    height=540,
)