import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt

rawdf = None
sumdf = None
countdf = None

#Set up every page
st.logo("images\\UNITE LOGO.avif", size="large")
st.image("images\\DEFINEIO.png")

# Welcome page content
st.markdown("# Round 3 Results")

# File uploader for round 3 data.
uploaded_file = st.file_uploader("Choose a file.")
if uploaded_file is not None:
   #read xls or xlsx
   rawdf=pd.read_excel(uploaded_file, header=0)
   sumdf=pd.read_excel(uploaded_file, header=0, sheet_name=1, index_col=0)
   countdf=pd.read_excel(uploaded_file, header=0, sheet_name=2, index_col=0)
else:
    st.warning("you need to upload a csv or excel file.")


#Display data for the uploaded file
tab1, tab2, tab3, tab4 = st.tabs(["Raw Data", "Summary Data", "Consensus Counts", "Top Statements"])

#Raw data
tab1.subheader("Raw Data")
if rawdf is not None:
    tab1.write(rawdf)

#Analyse the data and display new table
tab2.subheader("Summary Data")
if sumdf is not None:
   tab2.write(sumdf)
    #sumdf[sumdf['A'].str.match("hello")] #############

# Show consensus 
tab3.subheader("Consensus Counts")
if countdf is not None:
   #Chart 1 - Classical vs IPRAS
   tab3.markdown("# Classical vs IPRAS")
   tab3.bar_chart(data=countdf[["Consensus", "No Consensus"]], stack=False, x_label="Consensus by System", y_label="Count")

   #Chart 2 - Detailed Breakdown
   tab3.markdown("# Outcomes")
   tab3.bar_chart(data=countdf[["Agreement & Consensus","Agreement & No Consensus","Uncertain & Consensus",
                                "Uncertain & No Consensus","Disagreement & Consensus","Disagreement & No Consensus"]],
                                  stack=False, x_label="Consensus by System", y_label="Count")
   #tab3.pyplot(plt.gcf())

#Tab 4
tab4.subheader("Top Statements")
if sumdf is not None:
   filtered = sumdf.loc[:, sumdf.loc["Consensus"] == "CONSENSUS"]
   top_statements = filtered.loc["Median"].astype(int).nlargest(10).index
   #rank by IPR
   top_statements.name = "Top Statements"
   tab4.write(top_statements) 
   

   