import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

rawdf = None
sumdf = None
count_df = None
transposed_df = None

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
st.markdown('''
            # DEFINE-IO Priority Setting Workshop
            ## Phase 1: Round 3 Key Results
            ''')

# File uploader for round 3 data.
uploaded_file = st.file_uploader("Choose a file.")
if uploaded_file is not None:
   #read xls or xlsx
   rawdf=pd.read_excel(uploaded_file, header=0)
   sumdf=pd.read_excel(uploaded_file, header=0, sheet_name=1, index_col=0)
   count_df=pd.read_excel(uploaded_file, header=0, sheet_name='Counts of Consensus Types')
   transposed_df = pd.read_excel(uploaded_file, header=0, sheet_name='Transposed')
else:
    st.warning("You need to upload a csv or excel file.")


#Display data for the uploaded file
tab1, tab2 = st.tabs(["Consensus Outcomes", "Top Statements"])

#Tab 1: Consensus Outcomes
tab1.subheader("Consensus Outcomes")
if count_df is not None:
    count_subset = count_df.drop(["Consensus",	"No Consensus"], axis='columns')
    df_melt2 = count_subset.melt(var_name='Outcome', value_name='Count')
    # Create Altair chart
    chart = (
        alt.Chart(df_melt2)
        .mark_bar()
        .encode(
            x=alt.X('Outcome:N', axis=alt.Axis(labels=False)),
            y='Count:Q',
            color=alt.Color('Outcome:N', legend=alt.Legend(labelFontSize=14, titleFontSize=20, labelLimit=1000))
        )
    )
    tab1.altair_chart(chart, use_container_width=True)



#Raw data
#tab1.subheader("Raw Data")
#if rawdf is not None:
   # tab1.write(rawdf)

#Analyse the data and display new table
#tab2.subheader("Summary Data")
#if sumdf is not None:
  # tab2.write(sumdf)
    #sumdf[sumdf['A'].str.match("hello")] #############

# Show consensus 
#tab3.subheader("Consensus Counts")
#if countdf is not None:
   #Chart 1 - Classical vs IPRAS
   #tab3.markdown("## Classical vs IPRAS")
   #tab3.bar_chart(data=countdf[["Consensus", "No Consensus"]], stack=False, x_label="Consensus by System", y_label="Count")


#Tab 4: Top Statements
tab2.subheader("Top 25 Statements with Consensus")
if transposed_df is not None:
   columns_to_drop = ['0.15 Quartile', '0.85 Quartile', 'IPRcp', 'AI', 'IPRAS', 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Sum','No. outside range (AGREE, UNCERTAIN)', 'No. outside range (DISAGREE)', 'Classical Consensus', 'Outcome']
   df_sorted = transposed_df.query("Consensus == 'CONSENSUS'").sort_values(by=['Median', 'IPR'], ascending=[False, True]).head(25).reset_index(drop=True)
   df_dropped = df_sorted.drop(columns_to_drop, axis='columns')
   df_dropped['Cleaned'] = df_dropped['Statement'].str.replace(r'^\d+\.\s*Statement\s*\d+:', '', regex=True).str.strip()
   df_dropped['Cleaned2'] = df_dropped['Cleaned'].str.replace('(1-9 numeric rating)', '', regex=False).str.strip()
   df_dropped['ranked'] = [f"**Rank {i+1}:** {text}" for i, text in enumerate(df_dropped['Cleaned2'])]
   tab2.write("Statements that have reached consensus are listed below in rank order (based on median score and inter-percentile range).")
   tab2.write("")
   for value in df_dropped['ranked']:
      tab2.markdown(value)
      tab2.write("")

   

   