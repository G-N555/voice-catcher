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

lz_uri = "spotify:artist:58lV9VcRSjABbAbfWS6skp"

client_id = env('CLIENT_ID')
client_secret = env('CLIENT_SECRET')
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(
    client_id, client_secret
)

spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager)
results = spotify.artist_top_tracks(lz_uri)
print(results)
# # for track in results["tracks"][:3]:
# #     print("track    : " + track["name"])
# #     print("audio    : " + track["preview_url"])
# #     print("cover art: " + track["album"]["images"][0]["url"])
# p = vlc.MediaPlayer(
#     "https://p.scdn.co/mp3-preview/95970ac30265466027a6a9cb4ca18dbbfddab3d7?cid=774b29d4f13844c495f206cafdad9c86"
# )
# p.play()


def validError(request):
    return render("error.html", {'resultText': resultUS})


def listenEN(request):

    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("speak now")
        audio = r.listen(source)
        # text = r.recognize_google(audio, language="ja-JP")
        text = r.recognize_google(audio, language="en-US").lower()
        # print(text)
        resultUS = r.recognize_google(audio, language="en-US").lower()
        # resultJP = r.recognize_google(audio, language="ja-JP")
        print(resultUS)

        if "life" in resultUS:
            print("it's my life!")
            p = vlc.MediaPlayer(
                "https://p.scdn.co/mp3-preview/95970ac30265466027a6a9cb4ca18dbbfddab3d7?cid=774b29d4f13844c495f206cafdad9c86"
            )
            p.play()
            return render(request, "result.html", {'resultText': resultUS})
        elif "let's take the stairs" in resultUS:
            print("stair way to the heaven!")
            p = vlc.MediaPlayer(
                "https://p.scdn.co/mp3-preview/c2586acd4b782e0c06d2170f4c36caf6f5387de1?cid=774b29d4f13844c495f206cafdad9c86"
            )
            p.play()
            return render(request, "result.html", {'resultText': resultUS})
        elif "I'm super lazy today" in resultUS:
            print("the lazy song!")
            p = vlc.MediaPlayer(
                "https://p.scdn.co/mp3-preview/6dda0f582db7db112f377d36df313cf04e706f27?cid=774b29d4f13844c495f206cafdad9c86"
            )
            p.play()
            return render(request, "result.html", {'resultText': resultUS})
        elif "numb" in resultUS:
            print("Numb!")
            p = vlc.MediaPlayer(
                "https://p.scdn.co/mp3-preview/e6ccf7717f8a167bfea4afc1bf7da1a0cd707fbb?cid=774b29d4f13844c495f206cafdad9c86"
            )
            p.play()
            return render(request, "result.html", {'resultText': resultUS})
        elif "feel" in resultUS:
            print("cum on feel the noize!")
            p = vlc.MediaPlayer(
                "https://p.scdn.co/mp3-preview/9954d51864d538a47cd2eb9c3367b0c429d54ee7?cid=774b29d4f13844c495f206cafdad9c86"
            )
            p.play()
            return render(request, "result.html", {'resultText': resultUS})
        elif "anger" in resultUS:
            print("don't look back in anger!")
            p = vlc.MediaPlayer(
                "https://p.scdn.co/mp3-preview/80224af0151f8f6f14f615d954ca41a9db0eee75?cid=774b29d4f13844c495f206cafdad9c86"
            )
            p.play()
            return render(request, "result.html", {'resultText': resultUS})
        elif "I give five stars" in resultUS:
            print("yellow!")
            p = vlc.MediaPlayer(
                "https://p.scdn.co/mp3-preview/c119ca773ef844108da21c4679dc54c007cf0926?cid=774b29d4f13844c495f206cafdad9c86"
            )
            p.play()
            return render(request, "result.html", {'resultText': resultUS})
        else:
            return render(request, "error.html", {'resultText': resultUS})
