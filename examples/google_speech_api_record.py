import speech_recognition as sr

# obtain audio from the audio
# File not included on repo, record your own, use a single channel wav file recorded at 16KHz
AUDIO_FILE = "adapting_model/ad001.wav"
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# Add your own credential, remember the r to the beginning and now put spaces or blanklines at the beginning or at the
# end
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": ""
}"""
try:
    print(
        "Google Cloud Speech thinks you said " + r.recognize_google_cloud(
            audio,
            credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS
        )
    )
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
