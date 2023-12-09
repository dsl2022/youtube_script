from googleapiclient.discovery import build
import pprint

def youtube_search(api_key, keyword, max_results):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Make a search request
    request = youtube.search().list(
        q=keyword,
        part='snippet',
        type='video',
        maxResults=max_results
    )
    response = request.execute()
    return response
