import streamlit as st
import pandas as pd

#Define pages
welcome_page = st.Page("page\\welcome_page.py", title="Welcome", icon=":material/home:")
introduction_session_page = st.Page("page\\introduction_session_page.py", title="Introduction to the Session")
introduction_platform_page = st.Page("page\\introduction_platform_page.py", title="Introduction to the Platform")
round_2_summary_page = st.Page("page\\round_2_summary_page.py", title="Summary of Round 2 Results")
round_3_page = st.Page("page\\round_3_page.py", title="Round 3")
break_page = st.Page("page\\break_page.py", title="Break Time")
round_3_results_page = st.Page("page\\round_3_results_page.py", title="Round 3 Results")
MCDA_page = st.Page("page\\MCDA_page.py", title="Multicriteria Decision Analysis")
closing_page = st.Page("page\\closing_page.py", title="Closing the Session")

#Set up navigation
pg=st.navigation([welcome_page, introduction_session_page, introduction_platform_page,
                   round_2_summary_page, round_3_page, break_page, round_3_results_page,
                   MCDA_page, closing_page])

#Run the app
pg.run()