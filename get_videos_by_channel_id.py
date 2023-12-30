from googleapiclient.discovery import build
import os
from extract_video_transcript import get_transcript
from dotenv import load_dotenv
load_dotenv()
# Set up API key and YouTube API client
api_key = os.environ.get('GOOGLE_YOUTUBE_API_KEY')  # Replace with your actual API key
youtube = build('youtube', 'v3', developerKey=api_key)

def search_youtube(query):
    video_details = []
    next_page_token = None

    while True:
        request = youtube.search().list(
            q=query,
            part='id,snippet',
            maxResults=50,  # Adjust as needed, maximum is 50
            type='video',
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response.get('items', []):
            video_details.append({
                'videoId': item['id']['videoId'],
                'publishedAt': item['snippet']['publishedAt']
            })

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return video_details

full_transcript = ""
transcript_index = 0
# Search for videos related to 'virtualbacon'
virtualbacon_videos = search_youtube("virtualbacon")
for video in virtualbacon_videos:
    transcript = get_transcript(video['videoId'])
    full_transcript += f"Title {transcript_index} Transcript (Published on {video['publishedAt']}):\n{transcript}\n\n"
    print(f"Title {transcript_index} Transcript (Published on {video['publishedAt']})")
    transcript_index += 1

with open('combined_transcript_with_date.txt', 'w', encoding='utf-8') as file:
    file.write(full_transcript)
