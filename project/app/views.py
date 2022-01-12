from django.shortcuts import render
from django.http import request
from django.views.decorators.csrf import csrf_exempt
import speech_recognition as sr


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def record(request):
    audio_wav = request.body

    with open('audio/audio.wav', 'wb') as f:
        f.write(audio_wav)
    r = sr.Recognizer()
    with sr.AudioFile('audio/audio.wav') as source:
        audio_data = r.record(source)
    try:
        output = " " + r.recognize_google(audio_data, language='ja-JP')
        print(output)
    except sr.UnknownValueError:
        output = "Could not understand audio"
    except sr.RequestError as e:
        output = "Could not request results; {0}".format(e)

    return render(request, 'index.html', {'data': output})
