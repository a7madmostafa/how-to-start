import streamlit as st

st.set_page_config(page_title="Start Here", page_icon=":wave:", layout="centered")

st.title("Start Here")

st.markdown(
    """This app helps you to get started with the most demanding fields in Tech.  
    The app is under development.  
    Be patient :smile:"""
)

fields = {
    "Data Analysis": [ 'https://www.youtube.com/watch?v=rGx1QNdYzvs&list=PLUaB-1hjhk8FE_XZ87vPPSfHqb6OcM0cF', 'https://www.youtube.com/watch?v=dEYhq4KBaXU&list=PLWQgptB2ttLvOaVlohjV_0t9n5f9m5c_W&pp=iAQB' ],
    "Machine Learning":['https://www.youtube.com/watch?v=ZkHCcvjXjb4&list=PLYgoNb4RaVpVBf8EXw8Eca7eko9Xc4dJh'],
    "Web Development":['https://www.youtube.com/watch?v=yBDHkveJUf4&pp=ygUPV2ViIGRldmVsb3BtZW50'],
    "Mobile Development":['https://www.youtube.com/watch?v=VPvVD8t02U8&pp=ygUZcHl0aG9uIE1vYmlsZSBkZXZlbG9wbWVudA%3D%3D'],
    "Cyber Security":['https://www.youtube.com/watch?v=FARSxWjlPkk&pp=ygUaY3liZXIgc2VjdXJpdHkgZnVsbCBjb3Vyc2U%3D']
}



field = st.selectbox("Field", fields.keys())

st.markdown(f"You selected: **{field}**")

for url in fields[field]:
    st.video(url)

