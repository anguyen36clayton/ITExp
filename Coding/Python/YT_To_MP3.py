import os
import youtube_dl
from moviepy.editor import VideoFileClip

def download_youtube_video(video_id, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, 'temp.%(ext)s'),
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=' + video_id])
    return os.path.join(output_path, 'temp.mp4')

def convert_to_mp3(input_path, output_path):
    video = VideoFileClip(input_path)
    audio = video.audio
    audio.write_audiofile(output_path)
    video.close()
    audio.close()

def main():
    urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # Example URL, you can add more
        "https://www.youtube.com/watch?v=sbY9ALoe8Ew",  # Example URL with only video ID
        # Add more URLs here if needed
    ]
    output_directory = "mp3_files"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for url in urls:
        try:
            video_id = url.split('=')[-1].split('&')[0]  # Extract video ID from URL
            print(f"Downloading {url}")
            temp_file_path = download_youtube_video(video_id, output_directory)
            output_file_path = os.path.join(output_directory, f'{video_id}.mp3')
            print(f"Converting {temp_file_path} to {output_file_path}")
            convert_to_mp3(temp_file_path, output_file_path)
            os.remove(temp_file_path)
            print(f"Conversion completed: {output_file_path}")
        except Exception as e:
            print(f"Error processing {url}: {str(e)}")

if __name__ == "__main__":
    main()


