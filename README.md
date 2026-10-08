# 🎙️ AI Voice Assistant – Jarvis

An AI-powered voice assistant built with Python that can understand voice commands, process them using AI, provide spoken responses, fetch information, play music, open websites, and perform various computer-assisted tasks.

## ✨ Features

- 🎤 Voice command recognition
- 🧠 AI-powered question answering
- 🔊 Text-to-speech responses
- 🤖 OpenAI integration
- ⚡ Groq integration for speech transcription
- 📰 Latest news retrieval
- 🎵 Music playback
- 🌐 Web browsing and website opening
- 💬 Natural language interaction
- 🖥️ Computer-assisted tasks
- 🔐 API keys managed securely using environment variables

## 🛠️ Technologies Used

- **Python**
- **OpenAI API**
- **Groq API**
- **Whisper**
- **SpeechRecognition**
- **Edge TTS**
- **Pygame**
- **Requests**
- **python-dotenv**
- **Git & GitHub**

## 📂 Project Structure

```text
voice-assistant-python/
│
├── main.py
├── client.py
├── musicLibrary.py
├── voice_test.py
├── .gitignore
└── README.md
```

## File Description

| File               |               Description                                  |
|--------------------|------------------------------------------------------------|
| `main.py`          |  Main voice assistant program                              |
| `client.py`        | AI client and OpenAI-related functionality                 |
| `musicLibrary.py`  | Music library and playback-related functions               |
| `voice_test.py`    | Voice recognition/testing functionality                    |
| `.gitignore`       | Prevents sensitive and temporary files from being uploaded |


## 🔄 How It Works

```text
Voice Command
      ↓
Speech Recognition
      ↓
Speech-to-Text
      ↓
AI Processing
      ↓
Task / Response Generation
      ↓
Text-to-Speech
      ↓
Spoken Response
```

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/jSrishti8002/voice-assistant-python.git
```
### 2. Open the project folder
``` bash
cd voice-assistant-python
```
### 3. Create a virtual environment
```bash
python -m venv .venv
```
### 4. Activate the virtual environment
```bash
On Windows:
.venv\Scripts\activate
```
### 5. Install the required packages
```bash
pip install -r requirements.txt
```
If requirements.txt is not included yet, install the required Python packages used by the project manually.

## 🔑 API Configuration

This project uses API keys for external services.
Create a .env file in the project folder:
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
NEWS_API_KEY=your_news_api_key

Never upload your .env file or API keys to GitHub.
The project uses environment variables to keep API credentials separate from the source code.

## ▶️ Running the Assistant

After configuring the environment and API keys, run:
```bash
python main.py
```
The assistant will start listening for voice commands.
Example commands:
"Who was Newton?"

"Tell me some latest news."

"Open YouTube."

"Play <song_name>."

## 🔒 Security

Sensitive information is intentionally excluded from this repository.
The following files and temporary files are ignored using .gitignore:
```text
.env
__pycache__/
*.pyc
command.wav
jarvis_output.mp3
```
API keys should always be stored in environment variables rather than directly inside the source code.

## 🚀 Future Improvements

- Add more voice commands
- Improve conversational memory
- Add more computer automation features
- Add a graphical user interface
- Improve error handling
- Add more AI-powered capabilities
- Improve multilingual voice interaction
  
## 📌 Project Status

Active Development
This project is being developed as a Python-based AI voice assistant and is continuously being improved with new features and integrations.

## 👩‍💻 Author
Srishti Jaiswal
GitHub: [@jSrishti8002](https://github.com/jSrishti8002)


