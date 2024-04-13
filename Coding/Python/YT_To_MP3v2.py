import os
from pytube import YouTube
from pydub import AudioSegment
import concurrent.futures

def download_youtube_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    # Generate a unique filename based on video ID
    downloaded_file_path = stream.download(output_path=output_path, filename=f'{yt.video_id}_temp')
    return downloaded_file_path, yt.title

def convert_to_mp3(input_path, output_path):
    audio = AudioSegment.from_file(input_path)
    output_file_path = os.path.join(output_path, os.path.basename(input_path)) + ".mp3"
    audio.export(output_file_path, format="mp3")
    return output_file_path

def process_url(url, output_directory):
    try:
        print(f"Downloading {url}")
        temp_file_path, video_title = download_youtube_video(url, output_directory)
        print(f"Converting {temp_file_path} to mp3")
        output_file_path = convert_to_mp3(temp_file_path, output_directory)
        os.remove(temp_file_path)
        # Rename the MP3 file to the video title
        os.rename(output_file_path, os.path.join(output_directory, f"{video_title}.mp3"))
        print(f"Conversion completed: {os.path.join(output_directory, f'{video_title}.mp3')}")
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")

def main():
    urls = []
    more_links = True
    while more_links:
        link = input("Please enter a YouTube link (or type 'done' if you have no more links): ")
        if link.lower() == "done":
            more_links = False
        else:
            if "youtube.com" not in link:
                print("Error: Not a valid YouTube link.")
            else:
                urls.append(link)
    if not urls:
        print("No valid YouTube links provided.")
        return

    output_directory = "mp3_files"  # Relative path to the current working directory

    # Create the output directory if it does not exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for url in urls:
        process_url(url, output_directory)

if __name__ == "__main__":
    main()
