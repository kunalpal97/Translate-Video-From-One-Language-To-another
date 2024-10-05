import gtts 
import playsound
text = input("enter the text here : ")
sound = gtts.gTTS(text, lang="en")
sound.save("welcome.mp3")
playsound.playsound("welcome.mp3")