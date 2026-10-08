import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

for voice in speaker.GetVoices():
    print(voice.GetDescription())