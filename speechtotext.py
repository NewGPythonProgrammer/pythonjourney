from gtts import gTTS 
import os

text = "lol"
speech = gTTS(text=text, lang='en', slow=False)
speech.save("voice.mp3")
os.system("voice.mp3")
# you you must put en not english because grrs library dont has english
