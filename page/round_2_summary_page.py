import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt

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
            ## Phase 1: Summary of Round 2 Results
            ''')

count_df = None
transposed_df = None
demographics_df = None
pie_df = None

# File uploader for round 2 data.
uploaded_file = st.file_uploader("Choose a file.")
if uploaded_file is not None:
    st.text("File uploaded successfully.")
   #read xls or xlsx into multiple dataframes
    transposed_df = pd.read_excel(uploaded_file, header=0, sheet_name='Transposed')
    demographics_df = pd.read_excel(uploaded_file, header=0, sheet_name='Demographics')
    count_df=pd.read_excel(uploaded_file, header=0, sheet_name='Counts of Consensus Types')
    pie_df=pd.read_excel(uploaded_file, header=0, sheet_name='Pie Charting')

else:
    st.warning("You need to upload a csv or excel file.")



#Display data for the uploaded file
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Demographics", "Consensus Outcomes", "Statements with Consensus", "Statements without Consensus", "Excluded Statements"])

#Tab 1: Demographics
tab1.subheader("Demographics")
if demographics_df is not None:
    #Map
    tab1.subheader("Map of Participants")
    tab1.map(demographics_df, latitude="Latitude", longitude="Longitude", color="#0D5588", zoom=5, use_container_width=True, size=10000)
    
    #Years of Experience
    tab1.subheader("Years of Experience")
    pie = px.pie(pie_df, values='Experience Count', names='Experience')
    tab1.plotly_chart(pie, use_container_width=True)

    #Areas of Practice
    pie_subset = pie_df.drop(["Experience",	"Experience Count", "Target Organ",	"Target Organ Count"], axis='columns').head(1)
    df_melt = pie_subset.melt(var_name='Area of Practice', value_name='Count')
    # Create Altair chart
    chart = (
        alt.Chart(df_melt)
        .mark_bar()
        .encode(
            x=alt.X('Area of Practice:N', axis=alt.Axis(labels=False)),
            y='Count:Q',
            color=alt.Color('Area of Practice:N', legend=alt.Legend(labelFontSize=14, titleFontSize=20))
        )
        .properties(title='Areas of Practice')
        .configure_title(fontSize=28)
    )
    tab1.altair_chart(chart, use_container_width=True)

    
    #Target Organ
    tab1.subheader("Target Organs Regularly Treated")
    pie = px.pie(pie_df, values='Target Organ Count', names='Target Organ')
    tab1.plotly_chart(pie, use_container_width=True)

#Tab 2: Consensus Outcomes
tab2.subheader("Consensus Outcomes")
if count_df is not None:
    tab2.write("Total: 112 Statements")
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
    tab2.altair_chart(chart, use_container_width=True)

#Tab 3: Statements that have reached consensus
if transposed_df is not None:
    #High priority statements
    tab3.subheader("Statements that have reached consensus and scored as High Priority")
    high_priority_statements = transposed_df.query("Outcome == 'AGREEMENT' and Consensus == 'CONSENSUS'")
    columns_to_drop = ['0.15 Quartile', '0.85 Quartile', 'IPRcp', 'AI', 'IPRAS', 1, 2, 3, 4, 5, 6, 7, 8, 9,
                        'Sum','No. outside range (AGREE, UNCERTAIN)', 'No. outside range (DISAGREE)',
                          'Classical Consensus', 'Outcome', 'Consensus']
    df_high_dropped = high_priority_statements.drop(columns_to_drop, axis='columns')
    df_high_dropped['Statement'] = df_high_dropped['Statement'].str.replace(r'^\d+\.\s*Statement\s*\d+:', '', regex=True).str.strip()
    df_high_dropped['Statement'] = df_high_dropped['Statement'].str.replace('(1-9 numeric rating)', '', regex=False).str.strip()
    tab3.dataframe(df_high_dropped, hide_index=True)
    #for value in df_high_dropped['Statement']:
    #  tab3.markdown(value)
    #  tab3.write("")


    #Uncertain or medium priority statements
    tab3.subheader("Statements that have reached consensus and scored as Medium Priority")
    medium_priority_statements = transposed_df.query("Outcome == 'UNCERTAIN' and Consensus == 'CONSENSUS'")
    columns_to_drop = ['0.15 Quartile', '0.85 Quartile', 'IPRcp', 'AI', 'IPRAS', 1, 2, 3, 4, 5, 6, 7, 8, 9,
                        'Sum','No. outside range (AGREE, UNCERTAIN)', 'No. outside range (DISAGREE)',
                          'Classical Consensus', 'Outcome', 'Consensus']
    df_medium_dropped = medium_priority_statements.drop(columns_to_drop, axis='columns')
    df_medium_dropped['Statement'] = df_medium_dropped['Statement'].str.replace(r'^\d+\.\s*Statement\s*\d+:', '', regex=True).str.strip()
    df_medium_dropped['Statement'] = df_medium_dropped['Statement'].str.replace('(1-9 numeric rating)', '', regex=False).str.strip()
    tab3.dataframe(df_high_dropped, hide_index=True)
   #for value in df_medium_dropped['Statement']:
    #  tab3.markdown(value)
    # tab3.write("")

#Tab 4: Statements that have not reached consensus
if transposed_df is not None:
    tab4.subheader("Statements that have not reached consensus")
    nocon_statements = transposed_df.query("Consensus == 'NO CONSENSUS'")
    columns_to_drop = ['0.15 Quartile', '0.85 Quartile', 'IPRcp', 'AI', 'IPRAS', 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Sum','No. outside range (AGREE, UNCERTAIN)', 'No. outside range (DISAGREE)', 'Classical Consensus']
    df_nocon_dropped = nocon_statements.drop(columns_to_drop, axis='columns')
    df_nocon_dropped['Statement'] = df_nocon_dropped['Statement'].str.replace(r'^\d+\.\s*Statement\s*\d+:', '', regex=True).str.strip()
    df_nocon_dropped['Statement'] = df_nocon_dropped['Statement'].str.replace('(1-9 numeric rating)', '', regex=False).str.strip()
    for value in df_nocon_dropped['Statement']:
      tab4.markdown(f'''
                     <div style='font-size:22px; line-height:1.6;'>
                    
                     {value}
                     </div>
                     ''', unsafe_allow_html=True)
      tab4.write("")

#Tab 5: Statements that are excluded
tab5.subheader("Excluded Statements")
if transposed_df is not None:
    excluded_statements = transposed_df.query("Outcome == 'DISAGREEMENT' and Consensus == 'CONSENSUS'")
    columns_to_drop = ['0.15 Quartile', '0.85 Quartile', 'IPRcp', 'AI', 'IPRAS', 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Sum','No. outside range (AGREE, UNCERTAIN)', 'No. outside range (DISAGREE)', 'Classical Consensus']
    df_excluded_dropped = excluded_statements.drop(columns_to_drop, axis='columns')
    df_excluded_dropped['Statement'] = df_excluded_dropped['Statement'].str.replace(r'^\d+\.\s*Statement\s*\d+:', '', regex=True).str.strip()
    df_excluded_dropped['Statement'] = df_excluded_dropped['Statement'].str.replace('(1-9 numeric rating)', '', regex=False).str.strip()
    for value in df_excluded_dropped['Statement']:
      tab5.markdown(f'''
                     <div style='font-size:22px; line-height:1.6;'>
                    
                     {value}
                     </div>
                     ''', unsafe_allow_html=True)
      tab5.write("")