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
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
with col1:
    st.image("images/VinsonChan.jpg", caption="Vinson Wai-Shun Chan")
with col2:
    st.image("images/HelenNg.jpg", caption="Helen Hoi-Lam Ng")
with col3:
    st.image("images/ScottGriffiths.jpeg", caption="Scott Griffiths")
with col4:
    st.image("images/BlairGraham.jpg", caption="Blair Graham")
with col5:
    st.image("images/DeeviaKotecha.avif", caption="Deevia Kotecha")
with col6:
    st.image("images/HanifIsmail.jpeg", caption="Hanif Ismail")
with col7:
    st.image("images/PaulJenkins.png", caption="Paul Jenkins")
with col8:
    st.image("images/JimZhong.avif", caption="Jim Zhong")
with col9:
    st.image("images/RaghuL.avif", caption="Raghuram Lakshminarayan")
with col10:
    st.image("images/TzeMinWah.jpg", caption="Tze Min Wah")