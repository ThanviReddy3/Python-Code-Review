from openai import OpenAI
import streamlit as st

# Read the API key and setup an OpenAI client
with open(r'D:\chatbot\Internship\code_review\keys\key.txt') as f:
    openai_api_key = f.read()
st.image('https://innomatics.in/wp-content/uploads/2023/01/Innomatics-Logo1.png')
st.markdown("<h1 style='color:green;'>An AI code reviewer</h1>", unsafe_allow_html=True)
st.subheader("Python Code Reviewer and Bug Fixer")

client = OpenAI(api_key=openai_api_key)

prompt = st.text_area("Enter your code", height=150)

if st.button("Get Review"):
    st.markdown("<h2 style='color:black;'>Review:</h2>", unsafe_allow_html=True)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI Assistant. Given a Python code snippet, you will review it for potential bugs and suggest fixes."},
            {"role": "user", "content": prompt}
        ]
    )
    corrected_code = response.choices[0].message.content
    st.markdown("<h3 style='color:black;font-size:20px;'>Code Review Result:</h3>", unsafe_allow_html=True)
    st.write(response.choices[0].message.content)