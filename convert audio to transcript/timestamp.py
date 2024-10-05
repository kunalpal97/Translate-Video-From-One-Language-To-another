import datetime

test_sentence = "You can publish the Google script and deploy it as a web app with parameters for source and target languages and the text query. You can specify any ISO language pair or say “auto” and the Google Translation API will auto detect the language of the source text"

start_time = datetime.datetime(100,1,1,0,7,20)
#time will start from 00:00:00

block_num = "14"

def time_addition(sentence , current_time):

    time_add = (len(sentence.split()))*0.5

    end_time = current_time + datetime.timedelta(0, time_add)

    str_current_time = str(current_time.time())

    str_end_time = str(end_time.time())


    with open("sample_srt_timeadd.txt","w") as f:
        f.write(block_num)
        f.write("\n")
        f.write(str_current_time)
        f.write("--->")
        f.write(str_end_time)
        f.write("\n")
        f.write(sentence)
        f.write("\n")
        f.write("\n")

time_addition(test_sentence , start_time)



