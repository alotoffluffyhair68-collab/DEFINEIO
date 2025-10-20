import streamlit as st

#Set up every page
st.logo("images/UNITE LOGO.avif", size="large")
st.image("images/DEFINEIO.png")

# Welcome page content
st.markdown("# Round 2 Results")

# File uploader for round 2 data.
uploaded_file = st.file_uploader("Choose a file.")
if uploaded_file is not None:
    st.text("File uploaded successfully.")
   #read xls or xlsx
   #rawdf=pd.read_excel(uploaded_file, header=0)
   #sumdf=pd.read_excel(uploaded_file, header=0, sheet_name=1, index_col=0)
   #countdf=pd.read_excel(uploaded_file, header=0, sheet_name=2, index_col=0)
else:
    st.warning("You need to upload a csv or excel file.")