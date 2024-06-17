import argparse
import os
from pydub import AudioSegment

def split_audio(audio_file, chunk_length_ms=600000):  # 10 minutes = 600,000 milliseconds
    audio = AudioSegment.from_file(audio_file)
    base_path = os.path.dirname(audio_file)
    chunk_folder = os.path.join(base_path, "chunks")

    if not os.path.exists(chunk_folder):
        os.makedirs(chunk_folder)

    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i+chunk_length_ms]
        chunk_name = os.path.join(chunk_folder, f"chunk_{i//chunk_length_ms}.mp3")
        chunk.export(chunk_name, format="mp3")
    
    print(f"Chunks saved to folder: {chunk_folder}")

def main():
    parser = argparse.ArgumentParser(description="Split an audio file into chunks")
    parser.add_argument("audio_file", type=str, help="Path to the input audio file")

    args = parser.parse_args()

    try:
        split_audio(args.audio_file)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
