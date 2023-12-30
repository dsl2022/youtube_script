from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
from dotenv import load_dotenv
import os
load_dotenv()
YOUR_API_KEY = os.environ.get('GOOGLE_YOUTUBE_API_KEY')
# Replace with your own API key
YOUTUBE_VIDEO_ID = 'Yw7yWHigGKI'

def get_youtube_comments(youtube, video_id):
    comments = []
    try:
        # Retrieve youtube video results
        video_response = youtube.commentThreads().list(
            part='snippet,replies',
            videoId=video_id,
            textFormat='plainText',
            maxResults=100  # You can adjust this value
        ).execute()

        while video_response:
            # Extracting comments
            for item in video_response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment)
                # Check if there are replies to the comment
                if item['snippet']['totalReplyCount'] > 0:
                    for reply_item in item['replies']['comments']:
                        reply = reply_item['snippet']['textDisplay']
                        comments.append(reply)

            # Check if there are more comments
            if 'nextPageToken' in video_response:
                video_response = youtube.commentThreads().list(
                    part='snippet,replies',
                    videoId=video_id,
                    pageToken=video_response['nextPageToken'],
                    textFormat='plainText',
                    maxResults=100
                ).execute()
            else:
                break
    except HttpError as e:
        print(f'An HTTP error {e.resp.status} occurred:\n{e.content}')
    else:
        return comments

# Build the service object
youtube = build('youtube', 'v3', developerKey=YOUR_API_KEY)

# Call function to get all comments
all_comments = get_youtube_comments(youtube, YOUTUBE_VIDEO_ID)
# for comment in all_comments:
#     print(comment)
# Save comments to a text file
with open('youtube_comments.txt', 'w') as file:
    for comment in all_comments:
        file.write(comment + '\n')

# Confirm file has been saved
file_path = 'youtube_comments.txt'
if os.path.exists(file_path):
    print(f'File saved at {file_path}')
else:
    print('File was not saved.')