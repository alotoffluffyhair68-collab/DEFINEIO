import streamlit as st
import pandas as pd
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

# Common page content
st.markdown('''
            # DEFINE-IO Priority Setting Workshop
            ## Phase 2: Multi-Criteria Decision Analysis (MCDA)
            ''')
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Assessing Deliverability", "Scoring the Priorities", "Scoring QR", "Weighting the Criteria", "Weighting QR"])

# Tab 1: Assessing Deliverability
tab1.markdown(''' ### Purpose: Beyond Importance—Assessing Deliverability''')
tab1.markdown('''
            <div style='font-size:22px; line-height:1.6;'>
            We now transition from consensus (Delphi) to strategic prioritisation (MCDA). Our goal is to rank the top 25 research topics based on their real-world deliverability.
            </div>
              
            <br>  
            <div style='font-size:26px; line-height:1.6;'>
              
            **The Decision Criteria**
            </div>
            <div style='font-size:22px; line-height:1.6;'>
            We will score each of the 25 topics against three defined criteria:
            </div>
            <br>  
            ''', unsafe_allow_html=True)
table_1 = pd.DataFrame(
        {
        "**Definition**": [
            "The degree to which the research topic addresses a pressing clinical or patient need that requires immediate attention. This considers the potential for the research to rapidly impact patient outcomes or resolve significant existing uncertainties in clinical practice.",
            "The likelihood that a research project on this topic can be successfully designed, executed, and completed within the typical constraints of the UK research environment. This includes considerations of patient recruitment, ethical approval complexity, the availability of required technical expertise and infrastructure, and whether there is equipoise for that investigation.",
            "The estimated cost and resource requirements for conducting research on this topic. This is a 'cost' criterion, where a more affordable topic is considered more favourable. It encompasses not only direct financial costs but also demands on personnel, equipment, and facilities.",
        ],
        "**Rationale**": [
            "*Focuses on clinical impact.*",
            "*Focuses on practical achievability.*",
            "*Focuses on resource efficiency (Lower cost = More affordable/Favorable).*",
        ],
    }, index=["1. Urgency", "2. Feasibility / Equipoise", "3. Affordability"]
)
table_1.index.name = "**Criterion**"
tab1.table(table_1, border=True)
tab1.markdown('''
            <div style='font-size:22px; line-height:1.6;'>
            <br>
               
            **Outcome**: A final, ranked strategy reflecting both clinical importance *and* practical implementation.
            </div>
            ''', unsafe_allow_html=True)



# Tab 2: Scoring the Priorities
tab2.markdown(''' ### Scoring the Priorities (30 minutes)''')
tab2.markdown('''
            <div style='font-size:22px; line-height:1.6;'>
            You will assess all 25 research topics against the three criteria (Urgency, Feasibility/Equipoise, Affordability) using a structured 5-point Likert Scale.
            </div>
              
            <br>  
            <div style='font-size:26px; line-height:1.6;'>
              
            **The 5-Point Scale Instructions**
            </div>
            
            ''', unsafe_allow_html=True)
table_2 = pd.DataFrame(
        {
        "**Urgency**": [
            "**Very High** Urgency/Need",
            "High Urgency",
            "Moderate Urgency",
            "Low Urgency",
            "**Very Low** Urgency/Need",
        ],
        "**Feasibility/Equipoise**": [
            "**Very High** Feasibility/Equipoise",
            "High Feasibility/Equipoise",
            "Moderate Feasibility/Equipoise",
            "Low Feasibility/Equipoise",
            "**Very Low** Feasibility/Equipoise",
        ],
        "**Affordability**": [
            "**Very High** Affordability (*Very Low Cost*)",
            "High Affordability (*Low Cost*)",
            "Moderate Affordability (*Moderate Cost*)",
            "Low Affordability (*High Cost*)",
            "**Very Low** Affordability (*Very High Cost*)",
        ],
    }, index=["**5**", "**4**", "**3**", "**2**", "**1**"]
)
table_2.index.name = "**Score**"
tab2.table(table_2, border=True)
tab2.markdown('''
            <div style='font-size:26px; line-height:1.6;'>
            <br>
              
            **Key Point for Scoring**
            </div>   
            
            <div style='font-size:22px; line-height:1.6;'>
            <li>Affordability is an inverse criterion: A lower cost/resource requirement is scored higher e.g. 5.</li>
            <li>Please focus only on the topic description and the criteria definitions provided.</li>

            ''', unsafe_allow_html=True)


#Tab 3:
tab3.markdown('''### Please scan the QR code below to begin scoring the statements''')
tab3.markdown("")
# Display centered image
image_path = "images/MCDAQR.jpeg"
with open(image_path, "rb") as img_file:
    img_base64 = base64.b64encode(img_file.read()).decode()
tab3.markdown(
    f"""
    <style>
    .centered-image {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 120px 0;
    }}
    .centered-image img {{
        transform: scale(1.8);  /*  scales the image up by 80% */
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

# Tab 4: Weighting the Criteria
tab4.markdown(''' ### Weighting the Criteria (20 minutes)''')
tab4.markdown('''
            <div style='font-size:22px; line-height:1.6;'>
              
            Before we finalize the ranks, we must determine the relative importance (weight) of the three criteria (**Urgency, Feasibility/Equipoise, Affordability**).
            </div>
              
            <br>  
            <div style='font-size:26px; line-height:1.6;'>
              
            **The Swing Weighting Process**
            </div>
            
            <div style='font-size:22px; line-height:1.6;'>
            <ol>
                <li>
              
              **Establish Baseline:** Imagine a research topic performing at the worst possible level (Score 1) on all three criteria.</li>
                <li>**Identify Primary Criterion:** If you could only "swing" ONE criterion from its worst level (1) to its best level (5), which change would provide the **MOST significant improvement** to the overall research portfolio?
                    <ul>
                        <li>*Group vote will determine the Primary Criterion (Score 100)*.</li>
                    </ul>
                </li>
                <li>**Relative Scoring:** You will privately score the remaining two criteria relative to the Primary Criterion's benchmark of 100.
                    <ul>
                        <li>*Example: If Urgency is 100, how many points (0-100) would you assign to the 'swing' of Feasibility?*</li>
                    </ul>
                </li>           
            </ol>
            <br>
                
            **Output:** A set of weights (summing to 1.0) reflecting the collective judgment of the panel. These weights will be applied to the scores to generate the final, strategic ranking.  
            </div>
            ''', unsafe_allow_html=True)