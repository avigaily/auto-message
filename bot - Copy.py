# Schedual it in task schedual
# Change values of: phone, abspath (absolute path of an empty logs file)
# The message is not automaticaly sent but is written and we just need to press enter. Might change that, using "pyautogui".

import pywhatkit as kit
import random
import os
from datetime import datetime
from selenium.webdriver.common.keys import Keys 

def check_if_sent():
    # When using Task Manager use absolute path
    abspath = r"C:\Users\Avigail\Desktop\last_run.txt"
    if os.path.exists(abspath) and os.path.getsize(abspath)>0:
        with open(abspath, "r") as f:
            last_run = f.readline()
            last_run_time = datetime.strptime(last_run.split("at ")[1].strip(), "%Y-%m-%d %H:%M:%S.%f")
            # Check if it ran today 
            return last_run_time.date() == datetime.now().date() 
    return False

# select random message
def select_random_message():
    emojis=["❤️","❤️","💕","🌈"]
    emoji = emojis[random.randint(0,3)]
    text ="שבת שלום "
    # pywhatkit supports "\n" ---> https://github.com/Ankit404butfound/PyWhatKit/issues/346
    messages = [text + emoji, text + emoji + emoji, text + emoji+ "\nמה שלומכם?"]
    return messages[random.randint(0,2)]

# Send the message within 30 minutes
def send_message():
    hour = datetime.now().hour
    currmin = datetime.now().minute
    minute = random.randint((currmin + 1) % 60, (currmin + 30) % 60)
    phone = "+972****" # Enter reciver phone here

    message = select_random_message()
    kit.sendwhatmsg(phone, message, hour, minute)
    
    # Log success
    abspath = r"C:\Users\Avigail\Desktop\last_run.txt"
    if os.path.exists(abspath):
        with open(abspath, "w") as f:
            f.write(f"Message sent at {datetime.now()}\n")

# Check if message not sent and send the message
if not check_if_sent():
    send_message()
else:
    print("Already sent message")
