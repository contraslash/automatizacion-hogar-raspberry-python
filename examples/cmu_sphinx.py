import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    # Model not included on repo, please follow creating_model.md or adapting_model.md
    print(
        "Sphinx thinks you said " +
        r.recognize_sphinx(
            audio,
            (
                "adapting_model/isolated_words.ci_semi.adapt",
                "adapting_model/simplified/simplified.lm.DMP",
                "adapting_model/etc/isolated_words.dic",
            )
        ))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
