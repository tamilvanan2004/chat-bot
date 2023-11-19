import streamlit as st
import google.generativeai as palm
import os
api_key=os.environ['GOOGL_API_KEY']="AIzaSyAXvYN_2t4W_3PcvsCJ8Uh1SRDGRlTcgM4"
palm.configure(api_key=api_key)

st.title("Chat-Bot")

query = st.text_area("Enter Your Query")

if st.button("Generate"):
    with st.spinner(" Genenrating"):
        st.write(query)
        st.success("Answer")
        response = palm.generate_text(prompt=query)
        st.success(response.result)