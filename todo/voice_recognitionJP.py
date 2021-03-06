import speech_recognition as sr
import webbrowser as wb
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import vlc
from django.shortcuts import render
import environ

env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')


def listenJP(request):

    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("speak now")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="ja-JP")
        # text = r.recognize_google(audio, language="en-US").lower()
        print(text)
        # resultUS = r.recognize_google(audio, language="en-US").lower()
        resultJP = r.recognize_google(audio, language="ja-JP")
        print(resultJP)

        if "ダメ" in resultJP:
            print("イジメ、ダメ、絶対")
            p = vlc.MediaPlayer(
                "https://p.scdn.co/mp3-preview/ba0658edbc00e0a47e0ef21a490429ae2b592ffc?cid=774b29d4f13844c495f206cafdad9c86"
            )
            p.play()
            return render(request, "result.html", {'resultText': resultJP})
        elif "女々しい" in resultJP:
            print("livin on player!")
            p = vlc.MediaPlayer(
                "https://p.scdn.co/mp3-preview/7bfbeb604573ba7fddb1699db55dcec53afc17af?cid=774b29d4f13844c495f206cafdad9c86"
            )
            p.play()
            return render(request, "result.html", {'resultText': resultJP})
        elif "可愛い" in resultJP:
            print("yui!")
            p = vlc.MediaPlayer(
                "https://p.scdn.co/mp3-preview/4880ce6ec2acbd37dcb309fa904467db97091df0?cid=774b29d4f13844c495f206cafdad9c86"
            )
            p.play()
            return render(request, "result.html", {'resultText': resultJP})
        elif "これも人生か" in resultJP:
            print("it's my life!")
            p = vlc.MediaPlayer(
                "https://p.scdn.co/mp3-preview/95970ac30265466027a6a9cb4ca18dbbfddab3d7?cid=774b29d4f13844c495f206cafdad9c86"
            )
            p.play()
            return render(request, "result.html", {'resultText': resultJP})
        else:
            return render(request, "error.html", {'resultText': resultJP})
