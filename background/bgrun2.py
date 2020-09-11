import speech_recognition as sr
import os
import time

time.sleep(1)

r1 = sr.Recognizer()

names = []

while True:
    f = open("./temp/tempfile2.txt",'+a')
    flag = 0
    with sr.Microphone() as source :
        #print('\nSPEAK NOW\n')
        r1.adjust_for_ambient_noise(source, duration=0.2)
        audio = r1.listen(source, phrase_time_limit = 3)
        text = r1.recognize_google(audio, language="en-IN", show_all=True)
        try:
            dict = text['alternative']
            for i in dict:
                s = i["transcript"].lower()
                k = s.split(" ")
                for j in k:
                    j = str(j)
                    f.write(j+'\n')
        except Exception as e:
            continue
    f.close()
