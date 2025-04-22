import google.generativeai as ai
import os
from dotenv import load_dotenv

load_dotenv()

# api key
API_KEY = os.getenv('API_KEY')

# configure api
ai.configure(api_key=API_KEY)

# create model
model = ai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

# start a convo
while True:
    message = input('You: ')
    if message.lower() == 'bye':
        print('Chatbot: Goodbye!')
        break
    response = chat.send_message(message)
    print('Chatbot:', response.text)