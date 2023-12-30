from youtube_transcript_api import YouTubeTranscriptApi
def get_transcript(video_id):
    try:
        # Get a list of available transcripts for the video
        available_transcripts = YouTubeTranscriptApi.list_transcripts(video_id)        
        # Iterate through available transcripts and try to fetch each one
        for transcript in available_transcripts:
            try:
                # Attempt to fetch the transcript
                transcript_text = transcript.fetch()                
                return "\n".join([segment['text'] for segment in transcript_text])
            except Exception as e:
                print(f"Failed to fetch transcript in language: {transcript.language}")

    except Exception as e:
        print("Error:", e)
        return None

