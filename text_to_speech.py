from gtts import gTTS

text = "Hello, how are you?"
tts = gTTS(text=text, lang='en')
tts.save('hello.mp3')
