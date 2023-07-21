import requests
import os
import pandas as pd
# Function to get the bearer token for Reddit API
def get_bearer_token(client_id, client_secret, user_agent):
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    data = {'grant_type': 'password', 'username': os.getenv('USERNAME'), 'password': os.getenv('PASSWORD')}
    headers = {'User-Agent': user_agent}
    response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    if response.status_code != 200:
        raise Exception(f'Failed to get bearer token: {response.content}')
    result = response.json()
    try:
        TOKEN = result['access_token']
    except KeyError as error:
        print('Unable to fetch Access token!!')
    return TOKEN
