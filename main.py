from handlers.reddit_api import get_postid
from pprint import pprint
import os
CLIENT_ID =  os.getenv('CLIENT_ID') 
SECRET_TOKEN = os.getenv('SECRET_TOKEN')

# BEARER_TOKEN = get_bearer_token(CLIENT_ID, SECRET_TOKEN, 'Gaming Analyzer')
post_ids = get_postid('gaming',2,CLIENT_ID,SECRET_TOKEN,'Gaming Analyzer')

pprint(post_ids)