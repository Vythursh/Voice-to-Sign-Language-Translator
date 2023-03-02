import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk, ImageSequence
from itertools import count
import tkinter as tk
import string
from PIL import GifImagePlugin
import wave
import pyaudio
import matplotlib.animation
import apiai
import webbrowser as wb


# import selecting
# obtain audio from the microphone


def func():
    r = sr.Recognizer()
    gif = ['hello tuesday', 'welcome to',' hello friend will you assist me to home please','he didnt feel good', 'he didnt go home', 'he didnt love you', 'he doesnt feel good', 'he doesnt go home', 'he doesnt love you' , 'he feels good', 'he felt good', 'he goes home',
           'he is feeling good', 'he is going home','he is meeting my friend', 'he is nice to me', 'he loved you', 'he loves you', 'he meets my friend', 'he met my friend', 'he was nice to me', 'he went home',
           'he will be nice to me', 'he will go home', 'he will love you', 'he will feel good', 'he will meet my friend', 'he wont feel good', 'he wont go home',
           'he wont love you', 'how are you', 'i am feeling good', 'i am going home', 'i am meeting my friend', 'i didnt feel good' , 'i didnt go home','i didnt love you', 'i dont feel good', 'i dont go home', 'i dont love you',
           'i feel good', 'i felt good', 'i go home', 'i love you', 'i loved you', 'i meet my friend', 'i met my friend','i went home', 'i will feel good', 'i will go home', 'i will love you',
           'i will meet my friend', 'i wont feel good', 'i wont go home', 'i wont love you', 'she didnt feel good', 'she didnt go home', 'she didnt love you', 'she doesnt feel good', 'she doesnt go home', 'she doesnt love you', 'she feels good',
           'she felt good', 'she goes home', 'she is feeling good', 'she is going home', 'she is meeting my friend', 'she is nice to me', 'she loved you','she loves you', 'she meets my friend', 'she met my friend', 'she was nice to me',
           'she went home', 'she will be nice to me', 'she will feel good', 'she will go home', 'she will love you', 'she will meet my friend' , 'she wont feel good' ,'she wont go home' , 'she wont love you', 'welcome to my home', 'where is he',
           'where is my friend', 'where is my home', 'where is she', 'where is the bathroom', 'you will be nice to me','will you please help me', 'ac', 'air conditioner', 'alarm clock', 'alcohol', 'animals', 'animal', 'appetizer', 'april fools day', 'are you alright', 'assist', 'avocado', 'awesome', 'baby sitter', 'bad', 'balloon', 'bathroom', 'beautiful', 'bed', 'big', 'bird', 'birthday', 'black hair', 'both of them', 'bowling',
           'boxing day', 'breakup', 'bright light', 'broken hearted', 'bull', 'cabbage', 'cake', 'can', 'can i borrow that', 'cap','carnival', 'cartoon', 'caterpillar', 'chair', 'childish', 'chop', 'circle', 'coconut', 'collapse', 'confused','cool', 'could', 'could you pour some more drink for me', 'cousin','coustume', 'crackers',
           'cube', 'cute', 'dancing', 'day', 'dead', 'deaf', 'delete', 'dentist', 'diabetes', 'directions', 'disconnect', 'disrespect', 'do', 'do not', 'dont', 'earthquake', 'eating','engagement party', 'engineer', 'enlarge', 'entertainment','equal', 'escape','evacuate','evening', 'event coordinator', 'every week', 'everyday', 'everything',
           'excuse', 'exhausted', 'expand', 'extra large','facebook', 'family', 'fashion show', 'fast', 'fast food', 'fat', 'feel', 'field', 'fish', 'flag day', 'flirt', 'forgive', 'foul', 'fox', 'friday', 'friend', 'frustrated', 'fun','game', 'garlic', 'generator', 'giant', 'go', 'go away and leave me alone', 'golf', 'good', 'good bye', 'good luck',
           'good night', 'goodbye', 'gossip', 'governor', 'great', 'grow up', 'happy', 'happy fathers day', 'happy valentines day', 'he', 'hearing aid', 'heater', 'height', 'hello', 'help', 'help your self', 'helpless', 'her', 'hi', 'him', 'hiv', 'home', 'how', 'how are you', 'how much does it cost', 'how are you', 'huge', 'hurt', 'husband', 'i', 'i am fine',
           'i am lost', 'i cant focus', 'i dont care', 'i dont know','i dont like this', 'i dont understand', 'i hate you', 'i love you','i will help you','ice cream','internet', 'is it close', 'is it far', 'isolated', 'it', 'it is clear', 'jealous', 'joy', 'just a moment', 'hold on','keep calm and stay home', 'kiss', 'large bowl', 'late', 'later', 'laugh', 'lawyer',
           'lazy', 'learning disability', 'length', 'live', 'lonely', 'love', 'mad', 'magic', 'many', 'may', 'may you feel at ease', 'may you fel safe', 'may you feel strong', 'maybe', 'me', 'medium', 'meet', 'mental illness', 'menu', 'merry christmas', 'mine', 'miscommunication', 'money', 'morning', 'mother', 'mother in law', 'movie', 'murderer', 'music', 'my', 'near',
           'need', 'nervous', 'next day', 'next week', 'nice', 'nice to meet you', 'night', 'no', 'no one', 'none', 'noon', 'nothing', 'november', 'nurse', 'nursing home', 'oh god', 'oh shit', 'old', 'olympics', 'open minded', 'overweight', 'owl', 'pain', 'pants', 'paralyzed', 'party', 'penalty', 'phone', 'phone charger', 'plate', 'please', 'please clean up', 'please close the door',
           'please enjoy', 'please repeat', 'please stop', 'please turn on the lights', 'please turn the lights off', 'popcorn', 'potato chips', 'practice', 'presidents day', 'rabbit', 'recording', 'red cross', 'releived', 'repeat', 'ride', 'sad', 'safe', 'saturday', 'school bus', 'seafood', 'seal', 'seatbelt', 'seriously', 'shapes', 'share', 'shark', 'she', 'shocked', 'short', 'shrink',
           'shut up', 'shy', 'siblings', 'sick', 'sky', 'slap you', 'sleep', 'small', 'small chair', 'small table', 'so angry', 'social media', 'some', 'sore throat', 'sorry', 'sound', 'speech therapy', 'sphere', 'squirrel', 'steal', 'step sister', 'stomach ache', 'stroke', 'sunday', 'sunscreen', 'sunset', 'super', 'supper bowl', 'sweet potato', 'take your time', 'tall', 'tease', 'tennis',
           'thank you', 'thankyou', 'thanks', 'them', 'they','thirsty', 'ticket', 'time change', 'tired', 'to', 'travel guide book', 'treat', 'tree', 'truth or dare', 'tuesday', 'turn around', 'u turn', 'understand', 'us', 'very small', 'vest', 'vice president', 'volleyball', 'vomit', 'wait a moment', 'want', 'was', 'water', 'we are out of gas', 'wednesday', 'weekend', 'welcome', 'went', 'what happened',
           'what is for lunch', 'where', 'where is a hotel', 'where is a phone', 'where is the classroom', 'where is the next class', 'which', 'wide', 'will', 'will you help me', 'win', 'wine', 'wonderful', 'work', 'world series', 'wow', 'write', 'yes', 'you', 'you are cherished', 'you are doing great', 'you got this', 'yourself', 'address', 'all', 'any questions', 'are you angry', 'are you hungry', 'banana',
           'be careful', 'bridge', 'cat', 'christmas', 'church', 'clinic', 'did you finish homework', 'do you have money', 'do you want something to drink', 'dont worry', 'flower is beautiful', 'good question', 'grapes', 'hindu','i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i go to a theatre', 'i had to say something but i forget', 'job', 'lets go for lunch', 'mango', 'nice to meet you', 'open the door',
           'please call me later', 'police station', 'post office', 'shall i help you', 'shall we go together tomorrow', 'shop', 'sign language iterpreter', 'sit down', 'stand up', 'take care','temple', 'there was traffic jam', 'toilet', 'tomato', 'village', 'what is the problem', 'what is todays date', 'what is your father do', 'what is your name', 'whatsup', 'where is the bathroom', 'you are wrong']



    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)
        i = 0
        while True:
            print('Say something...............')
            audio = r.listen(source)

            # recognize speech using Sphinx
            try:
                a = r.recognize_google(audio)
                print("you said " + a.lower())

                for c in string.punctuation:
                    a = a.replace(c, "")
                if (a.lower() == 'go to main page'):
                    print("oops!It's time to leave. Thank you for your patient......")
                    break

                elif (a.lower() in gif):

                    path = 'GIF/{}.gif'.format(a.lower())

                    for img in ImageSequence.Iterator(Image.open(path)):
                        ImageNumpyFormat = np.asarray(img)
                        plt.imshow(ImageNumpyFormat)
                        plt.draw()
                        plt.pause(0.0000000000001)
                else:

                    for i in range(len(a)):

                        if (a[i] in arr):

                            ImageAddress = 'Alphabat/' + a[i] + '.jpg'
                            ImageItself = Image.open(ImageAddress)
                            ImageNumpyFormat = np.asarray(ImageItself)
                            plt.imshow(ImageNumpyFormat)
                            plt.draw()
                            plt.pause(0.8)

                        else:
                            continue

            except:
                print("Could not listen")
            plt.close()

def frequency():

    RATE = 44100
    BUFFER = 882

    p = pyaudio.PyAudio()

    stream = p.open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=RATE,
        input=True,
        output=False,
        frames_per_buffer=BUFFER
    )

    fig = plt.figure()
    line1 = plt.plot([], [])[0]
    line2 = plt.plot([], [])[0]

    r = range(0, int(RATE / 2 + 1), int(RATE / BUFFER))
    l = len(r)

    def init_line():
        line1.set_data(r, [-1000] * l)
        line2.set_data(r, [-1000] * l)
        return (line1, line2,)

    def update_line(i):
        try:
            data = np.fft.rfft(np.fromstring(
                stream.read(BUFFER), dtype=np.float32)
            )
        except IOError:
            pass
        data = np.log10(np.sqrt(
            np.real(data) ** 2 + np.imag(data) ** 2) / BUFFER) * 10
        line1.set_data(r, data)
        line2.set_data(np.maximum(line1.get_data(), line2.get_data()))
        return (line1, line2,)

    plt.xlim(0, RATE / 2 + 1)
    plt.ylim(-60, 0)
    plt.xlabel('Frequency')
    plt.ylabel('dB')
    plt.title('Spectrometer')
    plt.grid()

    line_ani = matplotlib.animation.FuncAnimation(
        fig, update_line, init_func=init_line, interval=0, blit=True
    )

    plt.show()



# Recording speech via pyaudio and wave
import pyaudio
import wave


def sound():
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 10
    filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 10 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


# Play recorded Audio via Simpleaudio
import simpleaudio as sa


def play():
    filename = 'output.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()


# coverting Recorded sound in Sign Language
from os import path
from pydub import AudioSegment


def text():
    r = sr.Recognizer()
    gif = ['hello tuesday', 'welcome to',' hello friend will you assist me to her home please','he didnt feel good', 'he didnt go home', 'he didnt love you', 'he doesnt feel good', 'he doesnt go home', 'he doesnt love you' , 'he feels good', 'he felt good', 'he goes home',
           'he is feeling good', 'he is going home','he is meeting my friend', 'he is nice to me', 'he loved you', 'he loves you', 'he meets my friend', 'he met my friend', 'he was nice to me', 'he went home',
           'he will be nice to me', 'he will go home', 'he will love you', 'he will feel good', 'he will meet my friend', 'he wont feel good', 'he wont go home',
           'he wont love you', 'how are you', 'i am feeling good', 'i am going home', 'i am meeting my friend', 'i didnt feel good' , 'i didnt go home','i didnt love you', 'i dont feel good', 'i dont go home', 'i dont love you',
           'i feel good', 'i felt good', 'i go home', 'i love you', 'i loved you', 'i meet my friend', 'i met my friend','i went home', 'i will feel good', 'i will go home', 'i will love you',
           'i will meet my friend', 'i wont feel good', 'i wont go home', 'i wont love you', 'she didnt feel good', 'she didnt go home', 'she didnt love you', 'she doesnt feel good', 'she doesnt go home', 'she doesnt love you', 'she feels good',
           'she felt good', 'she goes home', 'she is feeling good', 'she is going home', 'she is meeting my friend', 'she is nice to me', 'she loved you','she loves you', 'she meets my friend', 'she met my friend', 'she was nice to me',
           'she went home', 'she will be nice to me', 'she will feel good', 'she will go home', 'she will love you', 'she will meet my friend' , 'she wont feel good' ,'she wont go home' , 'she wont love you', 'welcome to my home', 'where is he',
           'where is my friend', 'where is my home', 'where is she', 'where is the bathroom', 'you will be nice to me','will you please help me', 'ac', 'air conditioner', 'alarm clock', 'alcohol', 'animals', 'animal', 'appetizer', 'april fools day', 'are you alright', 'assist', 'avocado', 'awesome', 'baby sitter', 'bad', 'balloon', 'bathroom', 'beautiful', 'bed', 'big', 'bird', 'birthday', 'black hair', 'both of them', 'bowling',
           'boxing day', 'breakup', 'bright light', 'broken hearted', 'bull', 'cabbage', 'cake', 'can', 'can i borrow that', 'cap','carnival', 'cartoon', 'caterpillar', 'chair', 'childish', 'chop', 'circle', 'coconut', 'collapse', 'confused','cool', 'could', 'could you pour some more drink for me', 'cousin','coustume', 'crackers',
           'cube', 'cute', 'dancing', 'day', 'dead', 'deaf', 'delete', 'dentist', 'diabetes', 'directions', 'disconnect', 'disrespect', 'do', 'do not', 'dont', 'earthquake', 'eating','engagement party', 'engineer', 'enlarge', 'entertainment','equal', 'escape','evacuate','evening', 'event coordinator', 'every week', 'everyday', 'everything',
           'excuse', 'exhausted', 'expand', 'extra large','facebook', 'family', 'fashion show', 'fast', 'fast food', 'fat', 'feel', 'field', 'fish', 'flag day', 'flirt', 'forgive', 'foul', 'fox', 'friday', 'friend', 'frustrated', 'fun','game', 'garlic', 'generator', 'giant', 'go', 'go away and leave me alone', 'golf', 'good', 'good bye', 'good luck',
           'good night', 'goodbye', 'gossip', 'governor', 'great', 'grow up', 'happy', 'happy fathers day', 'happy valentines day', 'he', 'hearing aid', 'heater', 'height', 'hello', 'help', 'help your self', 'helpless', 'her', 'hi', 'him', 'hiv', 'home', 'how', 'how are you', 'how much does it cost', 'how are you', 'huge', 'hurt', 'husband', 'i', 'i am fine',
           'i am lost', 'i cant focus', 'i dont care', 'i dont know','i dont like this', 'i dont understand', 'i hate you', 'i love you','i will help you','ice cream','internet', 'is it close', 'is it far', 'isolated', 'it', 'it is clear', 'jealous', 'joy', 'just a moment', 'hold on','keep calm and stay home', 'kiss', 'large bowl', 'late', 'later', 'laugh', 'lawyer',
           'lazy', 'learning disability', 'length', 'live', 'lonely', 'love', 'mad', 'magic', 'many', 'may', 'may you feel at ease', 'may you fel safe', 'may you feel strong', 'maybe', 'me', 'medium', 'meet', 'mental illness', 'menu', 'merry christmas', 'mine', 'miscommunication', 'money', 'morning', 'mother', 'mother in law', 'movie', 'murderer', 'music', 'my', 'near',
           'need', 'nervous', 'next day', 'next week', 'nice', 'nice to meet you', 'night', 'no', 'no one', 'none', 'noon', 'nothing', 'november', 'nurse', 'nursing home', 'oh god', 'oh shit', 'old', 'olympics', 'open minded', 'overweight', 'owl', 'pain', 'pants', 'paralyzed', 'party', 'penalty', 'phone', 'phone charger', 'plate', 'please', 'please clean up', 'please close the door',
           'please enjoy', 'please repeat', 'please stop', 'please turn on the lights', 'please turn the lights off', 'popcorn', 'potato chips', 'practice', 'presidents day', 'rabbit', 'recording', 'red cross', 'releived', 'repeat', 'ride', 'sad', 'safe', 'saturday', 'school bus', 'seafood', 'seal', 'seatbelt', 'seriously', 'shapes', 'share', 'shark', 'she', 'shocked', 'short', 'shrink',
           'shut up', 'shy', 'siblings', 'sick', 'sky', 'slap you', 'sleep', 'small', 'small chair', 'small table', 'so angry', 'social media', 'some', 'sore throat', 'sorry', 'sound', 'speech therapy', 'sphere', 'squirrel', 'steal', 'step sister', 'stomach ache', 'stroke', 'sunday', 'sunscreen', 'sunset', 'super', 'supper bowl', 'sweet potato', 'take your time', 'tall', 'tease', 'tennis',
           'thank you', 'thankyou', 'thanks', 'them', 'they','thirsty', 'ticket', 'time change', 'tired', 'to', 'travel guide book', 'treat', 'tree', 'truth or dare', 'tuesday', 'turn around', 'u turn', 'understand', 'us', 'very small', 'vest', 'vice president', 'volleyball', 'vomit', 'wait a moment', 'want', 'was', 'water', 'we are out of gas', 'wednesday', 'weekend', 'welcome', 'went', 'what happened',
           'what is for lunch', 'where', 'where is a hotel', 'where is a phone', 'where is the classroom', 'where is the next class', 'which', 'wide', 'will', 'will you help me', 'win', 'wine', 'wonderful', 'work', 'world series', 'wow', 'write', 'yes', 'you', 'you are cherished', 'you are doing great', 'you got this', 'yourself', 'address', 'all', 'any questions', 'are you angry', 'are you hungry', 'banana',
           'be careful', 'bridge', 'cat', 'christmas', 'church', 'clinic', 'did you finish homework', 'do you have money', 'do you want something to drink', 'dont worry', 'flower is beautiful', 'good question', 'grapes', 'hindu','i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i go to a theatre', 'i had to say something but i forget', 'job', 'lets go for lunch', 'mango', 'nice to meet you', 'open the door',
           'please call me later', 'police station', 'post office', 'shall i help you', 'shall we go together tomorrow', 'shop', 'sign language iterpreter', 'sit down', 'stand up', 'take care','temple', 'there was traffic jam', 'toilet', 'tomato', 'village', 'what is the problem', 'what is todays date', 'what is your father do', 'what is your name', 'whatsup', 'where is the bathroom', 'you are wrong']

    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # transcribe audio file
    AUDIO_FILE = "output.wav"

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)
        a = r.recognize_google(audio)
        print(a)
        i = 0
        while True:
            try:

                for c in string.punctuation:
                    a = a.replace(c, "")

                if (a.lower() in gif):
                    path = 'GIF/{}.gif'.format(a.lower())
                    for img in ImageSequence.Iterator(Image.open(path)):
                        ImageNumpyFormat = np.asarray(img)
                        plt.imshow(ImageNumpyFormat)
                        plt.draw()
                        plt.pause(0.0001)
                    break
                else:
                    for i in range(len(a)):
                        if (a[i] in arr):
                            ImageAddress = 'Alphabat/' + a[i] + '.jpg'
                            ImageItself = Image.open(ImageAddress)
                            ImageNumpyFormat = np.asarray(ImageItself)
                            plt.imshow(ImageNumpyFormat)
                            plt.draw()
                            plt.pause(0.8)

                        else:
                            continue
                break
            except:
                print("Recorded Data not found")
                break
                plt.close()

def website():
    r1 = sr.Recognizer()
    r2 = sr.Recognizer()
    r3 = sr.Recognizer()

    with sr.Microphone() as source:
        print('[search SLTC: search youtube')
        print('speak now')
        audio = r3.listen(source)

        if 'website' in r2.recognize_google(audio):
            r2 = sr.Recognizer()
            url = 'https://www.degree.lk/agencies/sltc-2/'
            with sr.Microphone() as source:
                print('search your query')
                audio = r2.listen(source)

                try:
                    get = r2.recognize_google(audio)
                    print(get)
                    wb.get().open_new(url + get)
                except sr.UnknownValueError:
                    print('error')
                except sr.RequestError as e:
                    print('failed'.format(e))


# func()
while 1:
  image="GUI.png"
  msg="VOICE TO SIGN LANGUAGE TRANSLATOR _ 1169 - M.Vythursh & 1089 - S.Sukatheesh"
  choices = ["LIVE VOICE","RECORD AUDIO","PLAY AUDIO","REVEAL","WEBSITE", "FREQUENCY", "Exit"]
  reply   = buttonbox(msg,image=image,choices=choices)
  if reply ==choices[0]:
      func()

  if reply == choices[1]:
        sound()
  if reply == choices[2]:
      play()

  if reply == choices[3]:
      text()


  if reply == choices[4]:
      website()

  if reply == choices[5]:
      frequency()

  if reply == choices[6]:
      quit()