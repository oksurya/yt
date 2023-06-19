import streamlit as st
from pytube import YouTube

def main():
    st.title("PyTube Downloader")
    st.write("Enter the YouTube video URL below:")

    video_url = st.text_input("Video URL", "")

    if st.button("Download"):
        try:
            yt = YouTube(video_url)
            video = yt.streams.first()
            st.write("Downloading video...")
            video.download()
            st.write("Video downloaded successfully.")
        except Exception as e:
            st.write("An error occurred:", str(e))

if __name__ == "__main__":
    main()
