import streamlit as st
from contact_form import show_contact_form

st.title("How to sharpen your Decision-making skills")
st.subheader("and get ahead of your competitors ?")

st.video("https://youtu.be/CkNI0KHdOCY", format="video/mp4", start_time=0)

show_contact_form()