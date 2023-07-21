from reddit_api import get_bearer_token
import requests


# Function to get ids of posts from a subreddit
def get_postid(subreddit_name, limit=100, client_id=None, client_secret=None, user_agent=None):
    TOKEN = get_bearer_token(client_id, client_secret, user_agent)
    headers = {'Authorization': f'bearer {TOKEN}', 'User-Agent': user_agent}
    response = requests.get(f'https://oauth.reddit.com/r/{subreddit_name}/hot', headers=headers, params={'limit': limit})
    if response.status_code != 200:
        raise Exception(f'Failed to get comments: {response.content}')
    result = response.json()
    posts = result['data']['children']
    ids = []
    # loop through each post retrieved from GET request
    for post in posts:
        ids.append(post['data']['id'])
    return ids
