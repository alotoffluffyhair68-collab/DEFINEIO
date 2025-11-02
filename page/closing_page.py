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
            ## Closing Remarks
            ''')
st.markdown('''
            <div style='font-size:22px; line-height:1.8;'>
            Thank you for participating in the DEFINE-IO Priority Setting Workshop. Your contribution will be invaluable in shaping the future direction of interventional oncology research.
            <br><br>

            We appreciate the time and effort you have dedicated to this process.
            We will be compiling the results and distributing a summary report to all panellists in the coming weeks. 
            <br><br>

            **Thank you for your commitment to shaping the future of IO research!**
            <br>
            **We hope you enjoy the remainder of the conference.**
            </div>

            <div style='font-size:28px; line-height:1.6;'>
            <br>
            
            **The DEFINE-IO Study Team**
            </div> 
            ''', unsafe_allow_html=True)
