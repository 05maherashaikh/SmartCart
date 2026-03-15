from google import genai
from google.genai import types
import streamlit as st

response = None

client = genai.Client(api_key="AIzaSyCg1i8atHr2yrb4G8bISjcL638hLQxWnhM")

st.title("YOUTUBE VIDEO SUMMARIZER")


video_link = st.text_input("Enter your YouTube video link")


if video_link:
    with st.chat_message("user"):
        st.write(video_link)


if st.button("Summarize Video"):

    if video_link:

        with st.spinner("Generating summary..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                config=types.GenerateContentConfig(
                    system_instruction="""
You are EduBot that summarizes YouTube videos.

When a user gives a YouTube link:
1. Explain the main topic
2. Provide a short summary
3. Give key points

Keep the explanation simple.
"""
                ),
                contents=f"Summarize this YouTube video: {video_link}"
            )


if response:
    st.subheader("📄 Video Summary")

    with st.chat_message("assistant"):
        st.write(response.text)