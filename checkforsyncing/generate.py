from gtts import gTTS

language = "hi"

text = "Now, there are so many languages spoken across the world. So in all languages, there are singers who sing to please the audience. As we know English is a global language, so English songs are very popular in the world as it has the largest number of audience."

speech = gTTS(text=text , lang=language, slow=False, tld="com.au")

speech.save("check.mp3")