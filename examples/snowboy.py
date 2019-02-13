import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    # Files are not included on repo, please create your own at https://snowboy.kitt.ai/
    print(
        "Sphinx thinks you said " +
        r.snowboy_wait_for_hot_word(
            "snowboy/swig/Python3",
            "Hola.pmdl",
            audio
        ))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))