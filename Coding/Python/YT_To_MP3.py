
import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

def download_youtube_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path=output_path, filename='temp')

def convert_to_mp3(input_path, output_path):
    video = VideoFileClip(input_path)
    audio = video.audio
    audio.write_audiofile(output_path)

def main():
    urls = [
        "https://www.youtube.com/watch?v=sbY9ALoe8Ew&ab_channel=Suboi",  # Example URL, you can add more
        # Add more URLs here if needed
    ]
    output_directory = "mp3_files"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for url in urls:
        try:
            print(f"Downloading {url}")
            download_youtube_video(url, output_directory)
            input_file_path = os.path.join(output_directory, 'temp.mp4')
            output_file_path = os.path.join(output_directory, f'{url.split("=")[-1]}.mp3')
            print(f"Converting {input_file_path} to {output_file_path}")
            convert_to_mp3(input_file_path, output_file_path)
            os.remove(input_file_path)
            print(f"Conversion completed: {output_file_path}")
        except Exception as e:
            print(f"Error processing {url}: {str(e)}")

if __name__ == "__main__":
    main()

