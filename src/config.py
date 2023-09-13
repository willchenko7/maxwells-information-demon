import os
import json

# Path to the config file
p = '/path/to/your/config/file'
CONFIG_PATH = os.path.join(p ,'gpt3-keys.json')
# Load the config file
with open(CONFIG_PATH) as f:
    config = json.load(f)

# Get the API key
GPT3_API_KEY = config['openai_api_key']
