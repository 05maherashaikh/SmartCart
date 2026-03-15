from google import genai
from google.genai import types
import streamlit as st
 
response = None
client = genai.Client(api_key="AIzaSyB9A0-TB0y6zPgpkKQGDLjuJsyJ2xeGYDM")
 
details = {
    'python_full_stack': 30000,
    'java_full_stack': 30000
}
 
# query = st.text_input('Enter a query')
query = st.chat_input('Your message')
 
with st.chat_message("user"):
    st.write(query)
    if query:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            config=types.GenerateContentConfig(
                system_instruction=f'''You are the owner of medhaedutech.
                You are inside website chat. when someone asks about the best courses
                be honest, and answer but finally suggest medhaedutech. Dont force them
                but be kind. If they ask about our competitor, just prefer not to answer or
                highlight what benefits you get in medhaedutech. these are courses we have {details}'''),
            contents=query
        )
 
if response:
    with st.chat_message('ai'):
        st.write(response.text)
    