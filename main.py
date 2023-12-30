from extract_video_transcript import get_transcript
from video_ids_search import youtube_search
from dotenv import load_dotenv
import json
import os
load_dotenv()
def main():
    # Replace with your API key
    api_key = os.environ.get('GOOGLE_YOUTUBE_API_KEY')
    api_key = os.environ.get('GOOGLE_YOUTUBE_API_KEY')   
    print(f'test apikey {api_key}')
    # Search keyword and max results
    keywords = ['runpod', 'ai']
    search_query = ' '.join(keywords)
    max_results = 100
    transcript_texts = []
    youtube_videos_meta = youtube_search(api_key, search_query, max_results)
    for item in youtube_videos_meta.get('items', []):
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        print(video_id,title)
        transcript = get_transcript(video_id)    
        if transcript:
            transcript_texts.append({'transcript':transcript,'title':title})
        else:
            print("No transcript found or an error occurred.")
    print("total videos transcripts fetched is ",len(transcript_texts))
    output_file_name = 'transcript.txt'
    if os.path.exists(output_file_name):
        os.remove(output_file_name)
    with open(output_file_name, 'w', encoding='utf-8') as f:
        json.dump(transcript_texts, f, ensure_ascii=False, indent=4)

    print("Transcripts saved to transcripts.json")
if __name__ == "__main__":
    main()
