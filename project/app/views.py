from django.shortcuts import render
from django.http import request
import speech_recognition as sr


def index(request):
    return render(request, 'index.html')


def record(request):
    data = request.POST.get('audio_data')

    print(data)
    with open('audio.wav', 'wb') as f:
        f.write(data)
    # get audio from the microphone
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Speak:")
    #     audio = r.listen(source)

    # try:
    #     output = " " + r.recognize_google(audio, language='ja-JP')
    # except sr.UnknownValueError:
    #     output = "Could not understand audio"
    # except sr.RequestError as e:
    #     output = "Could not request results; {0}".format(e)

    return render(request, 'index.html', {'data': data})
