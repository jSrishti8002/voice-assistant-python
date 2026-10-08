import speech_recognition as sr
import webbrowser
import edge_tts
import asyncio
import os
from dotenv import load_dotenv
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import musicLibrary
import requests
from groq import Groq 

load_dotenv()

groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

recognizer = sr.Recognizer()

pygame.mixer.init()

newsapi = os.getenv("NEWS_API_KEY")
def speak(text):
    # Set your preferred Indian English Neural Voice (e.g., Neerja or Prabhat)
    VOICE = "en-IN-neerjaNeural"

    OUTPUT_FILE = "jarvis_output.mp3"

    async def generate_speech():
        communicate = edge_tts.Communicate(text, VOICE, volume="+0%")
        await communicate.save(OUTPUT_FILE)

    # Run the asynchronous speech generator
    asyncio.run(generate_speech())

    # Play back the saved MP3 file via pygame
    pygame.mixer.music.load(OUTPUT_FILE)
    pygame.mixer.music.play()

    # Block script execution until Jarvis finishes speaking the current line
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    # Unload and clean up the temporary file so it can be overwritten next time
    pygame.mixer.music.unload()
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
def transcribe_with_groq(audio):
    temp_file = "command.wav"

    with open(temp_file, "wb") as f:
        f.write(audio.get_wav_data())

    with open(temp_file, "rb") as file:
        transcription = groq_client.audio.transcriptions.create(
            file=file,
            model="whisper-large-v3"
        )
    os.remove(temp_file)
    return transcription.text

def aiProcess(command):
    client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
    )
    completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses"},
        {"role": "user", "content": command}
    ]
    )

    return(completion.choices[0].message.content)

def process_command(c):
    c = c.strip()
    print("PROCESSING:", repr(c))

    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")

    elif c.lower().startswith("play"):
       
        song = c.lower().replace("play ", "").strip().rstrip(".!?")
        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
        else:
            speak(f"I could not find {song} in the music library")
    elif "headlines" in c.lower():

        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:

            # Parse the json response
            data = r.json()

            # extract the articles
            articles = data.get('articles',[])

            # get the headlines
            for article in articles[:5]:
                speak(article['title'])
        else:
            speak("Sorry, I could not fetch the news.")
    else:
        # let openAI handle the request
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__" :
    speak("Initialising Jarvis.... Hello Srishti")
    while True:
        #Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        r = sr.Recognizer()
        r.energy_threshold = 300
        r.dynamic_energy_threshold = True
        r.pause_threshold = 1
        # recognize speech using google
        
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                audio = r.listen(source , timeout = 3, phrase_time_limit= 2)

            word = transcribe_with_groq(audio)
            if "hello" in word.lower():
                speak("Yes?")
              
                #listen for command    
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(
                    source,
                    timeout=8,
                    phrase_time_limit=20
                    )
                    command = transcribe_with_groq(audio)
                    print("command:" , command)
                    process_command(command)
        
        except sr.WaitTimeoutError:
            pass
            
        except Exception as e:
            print("ERROR:", repr(e))
        