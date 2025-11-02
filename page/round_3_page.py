import streamlit as st
import streamlit.components.v1 as components

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
            ### Please scan the QR code below to begin scoring the statements
            ''')
st.markdown("")
st.image("images/R3QR.jpeg",  use_container_width=True)

st.markdown('''
            ### Round 3 Statement Review
            ''')
components.iframe(
    "https://docs.google.com/presentation/d/e/2PACX-1vRon98Fp2lP12rsizkNDmXtrTP5wy7rY8_O8fAGgcCooiUk-b8bPZ5WiN1iwU08xy3Ha6rFEmHse2LK/pubembed?start=false&loop=false&delayms=60000",
    width=960,
    height=540,
)