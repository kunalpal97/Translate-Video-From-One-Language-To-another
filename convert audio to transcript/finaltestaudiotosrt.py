import datetime
import pyaudio
import speech_recognition as sr

r = sr.Recognizer()

start_time  = datetime.datetime(100,1,1,0,7,10)

#00:07:10

max_time = datetime.datetime(100,1,1,0,8,30)
#00:8:20

block_num = 13

def speech_to_srt(current_time,block):

    if current_time >= max_time:
        return "Speech recognition complete"
    else:
        block +=1
        block_str = str(block)

        with sr.Microphone() as source:
            print("Now recording sentence: ")
            audio = r.listen(source)

            try:
                sentence = (r.recognize_google(audio))

            except sr.UnknownValueError:
                print("Google speech Recognition could not understand audio")

            except sr.RequestError as e:
                print("Could not request result from google speech recognition services; {0}",format(e))


            if sentence == "Speech recognition is over":
                return "speech recognition has ended by user request."

            else:
                time_add = len(sentence.split())

                end_time = current_time + datetime.timedelta(0,time_add)

                str_current_time = str(current_time.time())

                str_end_time = str(end_time.time())

                with open("speech_to_text.srt", "a") as f:
                    f.write(block_num)
                    f.write("\n")
                    f.write(str_current_time)
                    f.write("--->")
                    f.write(str_end_time)
                    f.write("\n")
                    f.write(sentence)
                    f.write("\n")
                    f.write("\n")
                return speech_to_srt(end_time,block)

speech_to_srt(start_time,block_num)






