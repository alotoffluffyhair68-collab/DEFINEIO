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
            ### Please scan the QR code below to begin scoring the statements
            ''')
st.markdown("")

# Display centered image
image_path = "images/R3QR.jpeg"
with open(image_path, "rb") as img_file:
    img_base64 = base64.b64encode(img_file.read()).decode()
st.markdown(
    f"""
    <style>
    .centered-image {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 120px 0;
    }}
    .centered-image img {{
        transform: scale(1.8);  /* 👈 scales the image up by 80% */
        width: auto !important; /* override Streamlit’s auto-scaling */
        height: auto !important;
        max-width: none !important;
    }}
    </style>

    <div class="centered-image">
        <img src="data:image/jpeg;base64,{img_base64}" alt="image">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('''
            ### Round 3 Statement Review
            ''')
components.iframe(
    "https://docs.google.com/presentation/d/e/2PACX-1vRon98Fp2lP12rsizkNDmXtrTP5wy7rY8_O8fAGgcCooiUk-b8bPZ5WiN1iwU08xy3Ha6rFEmHse2LK/pubembed?start=false&loop=false&delayms=60000",
    width=960,
    height=540,
)