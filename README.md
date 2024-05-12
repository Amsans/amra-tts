### 1. Downloading from YouTube
https://github.com/yt-dlp/yt-dlp <br>
Use the tool to download `mp3` (and/or video) file from YouTube.

### 2. Transcribe subtitles
https://alphacephei.com/vosk/install <br>
Use Vosk to make subtitles with timestamp from downloaded mp3 file

### 3. Translate subtitle file
https://translatesubtitles.co/ <br>
Use the service to translate and edit subtitles file

### 4. TTS translated subtitles
Run `python3 main.py` with translated file specified to make audio 

### 5. Create video with additional audiotrack
Use VEGAS Pro or similar software to create video with translated audio in it.

#### Converting MKV video
`ffmpeg -i videofile.mkv videofile.mp4`

#### Reduce file size
`ffmpeg -i input.mp4 -vcodec libx265 -crf 28 output.mp4`

