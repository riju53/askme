import streamlit as st
import os
from langchain_groq import ChatGroq

# Load API key from Streamlit secrets
groq_api_key = st.secrets["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] = "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"

# Initialize Groq model
model = ChatGroq(
    model="llama-3.1-8b-instant",   # ✅ working model
    temperature=0.7,
    max_tokens=256
)

# UI
st.title("Askme anything 🚀")

with st.form('my_form'):
    text = st.text_input('Enter text:')
    submit = st.form_submit_button('Ask me')

if submit:
    if text.strip():
        with st.spinner("Thinking..."):
            st.write("Model loaded ✅")
            response = model.invoke(text)
            st.write(response.content)
    else:
        st.warning("Please enter a question!")
