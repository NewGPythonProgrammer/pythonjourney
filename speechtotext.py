from gtts import gTTS 
import os

text = "lol"
speech = gTTS(text=text, lang='english', slow=False)
speech.save("voice.mp3")
os.system("voice.mp3")
