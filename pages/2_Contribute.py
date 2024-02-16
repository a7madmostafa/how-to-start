import streamlit as st
import pandas as pd

st.set_page_config(page_title="Contribute", page_icon=":wave:", layout="centered")

st.title("Contribute")

st.markdown(
    """This app helps you to get started with the most demanding fields in Tech.  
    The app is under development.  
    Be patient :smile:"""
)

st.markdown("""You can contribute to this project by submitting an awesome resource!""")

with st.form(key="contribute"):
    field = st.selectbox("Field", ["Data Analysis", "Machine Learning", "Web Development", "Mobile Development", "Cyber Security"])
    url = st.text_input(label="URL")
    description = st.text_input(label="Description")
    submit = st.form_submit_button(label="Submit")

if submit:
    contribution = pd.DataFrame({
        "Field": [field],
        "URL": [url],
        "Description": [description]
    })

    contribution.to_csv("Contribution1.csv")
    st.success("Thank you for your contribution!")
