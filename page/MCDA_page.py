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

st.markdown('''
            # DEFINE-IO Priority Setting Workshop
            ## Phase 2: Multi-Criteria Decision Analysis (MCDA)
            ''')

tab1, tab2, tab3 = st.tabs(["Assessing Deliverability", "Scoring the Priorities", "Weighting the Criteria"])
st.markdown('''# Please scan the QR code below to begin scoring the statements
            ''')
st.markdown("")
st.image("images/MCDAQR.jpeg",  use_container_width=True)
