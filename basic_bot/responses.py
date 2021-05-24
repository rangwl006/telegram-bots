'''
This file contains the responses.
Can insert more functionality depending on what the purpose of the bot is. 
'''
from datetime import datetime

# the responses function takes in a user input and returns a reply to the caller
def responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi"):
        return "Hello!"

    if user_message in ("who are you", "who are you?"):
        return "I am the basic bot"

    if user_message in ("time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)
    
    return "What are you saying?"
