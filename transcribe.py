import argparse
import os
from openai import OpenAI

def transcribe_audio_chunk(audio_chunk):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("The environment variable OPENAI_API_KEY is not set.")
    
    client = OpenAI(api_key=api_key)
    
    with open(audio_chunk, "rb") as file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=file
        )

    return transcription.text

def transcribe_chunks(chunk_folder):
    full_transcription = ""
    
    for chunk in sorted(os.listdir(chunk_folder)):
        chunk_path = os.path.join(chunk_folder, chunk)
        if os.path.isfile(chunk_path):
            full_transcription += transcribe_audio_chunk(chunk_path) + "\n"
    
    return full_transcription

def main():
    parser = argparse.ArgumentParser(description="Transcribe audio chunks using OpenAI API")
    parser.add_argument("chunk_folder", type=str, help="Path to the folder containing audio chunks")
    parser.add_argument("output_text_file", type=str, help="Path to the output text file")

    args = parser.parse_args()

    try:
        transcription = transcribe_chunks(args.chunk_folder)
        with open(args.output_text_file, 'w') as file:
            file.write(transcription)
        print(f"Transcription saved to {args.output_text_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
