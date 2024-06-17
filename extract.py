# extract_audio.py
import argparse
from moviepy.editor import VideoFileClip
import os

def extract_audio(video_file, output_file):
    try:
        video_clip = VideoFileClip(video_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_file)
        audio_clip.close()
        video_clip.close()
        print(f"Audio has been successfully extracted to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Extract audio from a video file")
    parser.add_argument("video_file", type=str, help="Path to the input video file")
    parser.add_argument("output_audio_file", type=str, help="Path to the output MP3 file")

    args = parser.parse_args()

    extract_audio(args.video_file, args.output_audio_file)


if __name__ == "__main__":
    main()
