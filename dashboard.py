import streamlit as st
import pandas as pd
import numpy as np

st.title("Adherence")

chart_data=pd.DataFrame(
    np.random.randn(3,3),
    columns=["Taken On Time","Taken Late","Missed"]
)
st.bar_chart(chart_data, use_container_width=True)

# df = pd.DataFrame({"Category": ["A", "B", "C"], "Values": [10, 20, 30]})
#
# st.bar_chart(df, x="Category", y="Values", height=300, width=600, title="Bar Chart", x_label="Category", y_label="Values")

st.text("Total Reminder: 145, Late: 47, Missed: 72")

st.write("Current Medication", align='right')

# st.bullet("VITAMIN A AND VITAMIN D; 929.3mg/g OINTMENT",align='right')
# st.bullet("IBUPROFEN; 100mg/5ml SUSPENSION",align='right')
# st.bullet("TYLENOL COLD; 325mg.15ml LIQUID",align='right')
# st.bullet("PREDNISONE; 20mg/1 TABLET",align='right')

# st.sidebar.markdown("<div style='text-align:right'>- VITAMIN A AND VITAMIN D; 929.3mg/g OINTMENT\n- IBUPROFEN; 100mg/5ml SUSPENSION\n- TYLENOL COLD; 325mg.15ml LIQUID\n - PREDNISONE; 20mg/1 TABLET</div>", unsafe_allow_html=True)

st.markdown("- VITAMIN A AND VITAMIN D; 929.3mg/g OINTMENT\n- IBUPROFEN; 100mg/5ml SUSPENSION\n- TYLENOL COLD; 325mg.15ml LIQUID\n- PREDNISONE; 20mg/1 TABLET", unsafe_allow_html=True)

