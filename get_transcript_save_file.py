from extract_video_transcript import get_transcript

transcript = get_transcript("SO8lBVWF2Y8")
with open("transcript_delete.txt","w",encoding='utf-8') as f:
    f.write(transcript)