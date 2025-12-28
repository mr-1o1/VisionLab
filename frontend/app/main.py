import streamlit as st
import requests

# Docker networking: 'backend' refers to the service name in docker-compose
BACKEND_URL = "http://backend:8000"

st.title("VisionLab 🧪")
st.write("Modular Computer Vision Pipeline")

# Check connection
if st.button("Check Backend Status"):
    try:
        response = requests.get(f"{BACKEND_URL}/")
        if response.status_code == 200:
            st.success(f"Backend says: {response.json()['message']}")
        else:
            st.error("Backend is reachable but returned an error.")
    except Exception as e:
        st.error(f"Connection Failed: {e}")
