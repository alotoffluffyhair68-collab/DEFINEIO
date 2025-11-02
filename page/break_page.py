import streamlit as st
import time
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


# Welcome page content
st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('''
            # DEFINE-IO Priority Setting Workshop
            ## Break Time
            ''')
st.image("images/coffee.jpg")

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

def count_down(mins):
    with st.empty():
        secs = mins*60
        for secs in range(secs,-1,-1):
            mm, ss = secs//60, secs%60
            disp_time = f"{mm:02d}:{ss:02d}"
            st.markdown(f'''<h1 class="title">{disp_time} </h1>''', unsafe_allow_html=True)
            time.sleep(1)
        autoplay_audio("alarm.mp3")

st.markdown(
        """<style>
    div[class*="stSlider"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 26px;
    }
        </style>
        """, unsafe_allow_html=True)

mins = st.select_slider(
    "Duration of break",
    options=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 
)

if st.button("Start"):
    count_down(mins)
