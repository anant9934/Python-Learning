# text_to_speech_demo.py

import pyttsx3

engine = pyttsx3.init()
engine.say('''mandeep singh is my best friend.
He is a very good person and always helps me in my studies.
He is very kind and supportive.
I am grateful to have him in my life.
.''')
engine.runAndWait()