# Transcriber

## Setup

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

### 1) Download File

Either download manually or with the download script from drive.


```
python ./download.py <file_id> ./tmp/temp_video_file.mp4
```

### 2) Extract Audio

```
python ./extract.py ./tmp/temp_video_file.mp4 ./tmp/temp_audio_file.mp3
```


### 3) Transcribe

```
python ./transcribe.py ./tmp/temp_audio_file.mp3 ./tmp/transcript.txt
```

### 4) Document
```
python ./document.py ./tmp/transcript.txt ./tmp/meeting.md
```