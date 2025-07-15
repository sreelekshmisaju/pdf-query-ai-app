import streamlit as st
import sys

st.title("✅ App Startup Test")

st.write("Python Version:", sys.version)
st.write("Streamlit Version:", st.__version__)
st.write("✅ If you see this, Streamlit is working fine.")
