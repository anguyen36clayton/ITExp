import os
from pytube import YouTube
from pydub import AudioSegment
import concurrent.futures

def download_youtube_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    downloaded_file_path = stream.download(output_path=output_path, filename='temp')
    return downloaded_file_path

def convert_to_mp3(input_path, output_path):
    audio = AudioSegment.from_file(input_path)
    output_file_path = output_path + ".mp3"
    audio.export(output_file_path, format="mp3")
    return output_file_path

def process_url(url, output_directory):
    try:
        print(f"Downloading {url}")
        temp_file_path = download_youtube_video(url, output_directory)
        print(f"Converting {temp_file_path} to mp3")
        output_file_path = convert_to_mp3(temp_file_path, os.path.join(output_directory, url.split("=")[-1]))
        os.remove(temp_file_path)
        print(f"Conversion completed: {output_file_path}")
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")

def main():
    urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # Example URL, you can add more
        "https://www.youtube.com/watch?v=sbY9ALoe8Ew",  # Example URL, you can add more
        # Add more URLs here if needed
    ]
    output_directory = "mp3_files"  # Relative path to the current working directory

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(lambda url: process_url(url, output_directory), urls)

if __name__ == "__main__":
    main()


