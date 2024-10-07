# YouTube Transcript to Detailed Notes Summarizer

This application allows users to generate a concise summary of any YouTube video by fetching its transcript and summarizing the content using Google Gemini (Generative AI). The app is built with [Streamlit](https://streamlit.io/), and it utilizes the [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/) for transcript extraction.

## Features

- Fetches the transcript from a YouTube video.
- Uses Google Gemini's AI model to summarize the video into key points.
- Displays the video thumbnail and provides a summary in under 250 words.

## Demo

You can try the live demo [here](https://youtube-summarizer-llm.streamlit.app/)

## Requirements

Before running the application, ensure you have the following dependencies installed:

- **Python 3.7+**
- **Streamlit**
- **Google Generative AI SDK**
- **YouTube Transcript API**
- **python-dotenv**

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SKAT-16/youtube-summarizer-llm.git
   cd youtube-transcript-summarizer
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   - Create a `.env` file in the root of the project and add your Google Gemini API key:

   ```bash
   GOOGLE_API_KEY=<your_google_api_key>
   ```

5. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Enter a YouTube video link:**

   - Paste the link to the YouTube video for which you'd like to generate a summary.

2. **Get the transcript and summary:**

   - After entering the YouTube link, click on the "Get Detailed Notes" button. The app will fetch the transcript, generate a summary using the Gemini model, and display it.

3. **View the summary:**
   - The AI-generated summary of the transcript will appear on the page.

## Example

1. **Input:**
   - YouTube video URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
2. **Output:**
   - A brief summary of the video's content, highlighting key points within 250 words.

## Tech Stack

- **Backend**: Streamlit, YouTube Transcript API, Google Generative AI SDK
- **Frontend**: Streamlit
