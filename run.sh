#!/bin/bash

input_file=$1
base_name=$(dirname $input_file)


echo "Running process in $base_name on video $input_file"


echo "Extracting audio from video" && \
echo "python ./extract.py $input_file $base_name/audio.mp3" && \
echo "Transcribing audio to text" && \
echo "python ./transcribe.py $base_name/audio.mp3 $base_name/transcript.txt" && \
echo "Generating document" && \
echo "python ./document.py $base_name/transcript.txt $base_name/document.md"


exit 0


echo "Extracting audio from video" && \
echo "python ./extract.py $input_file $base_name/audio.mp3" && \
# python ./extract.py $input_file $base_name/audio.mp3 && \
echo "Transcribing audio to text" && \
echo "python ./transcribe.py $base_name/audio.mp3 $base_name/transcript.txt" && \
# python ./transcribe.py $base_name/audio.mp3 $base_name/transcript.txt && \
echo "Generating document" && \
echo "python ./document.py $base_name/transcript.txt $base_name/document.md" && \
# python ./document.py $base_name/transcript.txt $base_name/document.md