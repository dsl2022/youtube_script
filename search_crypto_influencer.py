from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
load_dotenv()

# Set up API key and YouTube API client
api_key = os.environ.get('GOOGLE_YOUTUBE_API_KEY')  # Set your API key as an environment variable
youtube = build('youtube', 'v3', developerKey=api_key)

def search_youtube(query, max_results=50):
    request = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=max_results,
        type='channel'
    )
    response = request.execute()

    influencer_ids = []
    for item in response['items']:
        print(item)
        channel_id = item['id']['channelId']
        influencer_ids.append(channel_id)

    return influencer_ids

# Search for crypto influencers
crypto_influencers = search_youtube("crypto influencer")
print(crypto_influencers)
