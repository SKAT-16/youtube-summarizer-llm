import streamlit as st
import  google.generativeai as genai
import os
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import  load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_gemini_content(transcript_text, prompt):
  model = genai.GenerativeModel('gemini-1.5-flash')
  response = model.generate_content(prompt+transcript_text)
  return response.text

def fetch_transcript(youtube_video_url):
  try:
    video_id = youtube_video_url.split('=')[-1]
    transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

    transcript = ""
    for i in transcript_text:
      transcript += " " + i['text']

    return transcript
  except Exception as e:
    st.error(f"Error fetching transcript: {e}")

prompt = """You are a youtube video summurizer. You will be taking the transcript text
            and summurizing the entire video and providing the important summaru in points within
            250 words. The transcript text is: 
          """

st.title("Youtube Transcript to Detailed Notes Summarizer")
youtube_link = st.text_input("Enter the link of the youtube video")

if youtube_link:
  video_id = youtube_link.split("=")[1]
  st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
  if st.button("Get Detailed Notes"):
    transcript_text = fetch_transcript(youtube_link)
    if transcript_text:
      summary = generate_gemini_content(transcript_text, prompt)
      st.write(summary)