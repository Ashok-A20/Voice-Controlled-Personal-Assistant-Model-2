# Voice-Controlled Personal Assistant

A voice-controlled desktop assistant built with Python and PyQt5. This assistant can perform various tasks such as opening applications, searching the web, controlling media, and more, all via voice commands.

## Features

- **Voice Command Recognition**: Uses the `speech_recognition` library to recognize voice commands and `pyttsx3` for text-to-speech conversion.
- **Task Automation**: Automates tasks like opening applications (Notepad, Paint, Browser), controlling media (YouTube, etc.), and taking screenshots.
- **Interactive GUI**: A sleek graphical interface built using PyQt5 with animated elements like GIFs and images.
- **Wikipedia Search**: Can perform searches on Wikipedia and read out the results.
- **Time and Date**: Tells the current time and date on request.
- **Jokes**: Responds with a random joke using the `pyjokes` library.

## How It Works

The assistant listens for voice commands and performs actions based on the recognized commands. Some of the available commands include:

- **"Open Browser"**: Opens the default web browser.
- **"Play [song name]"**: Plays a video on YouTube using `pywhatkit`.
- **"Tell me a joke"**: Responds with a random joke.
- **"Open Notepad"**: Opens Notepad and allows typing and saving content.
- **"Search Wikipedia for [topic]"**: Searches Wikipedia and reads the first result.
- **"Time"**: Tells the current time.
- **"Take a screenshot"**: Takes a screenshot and saves it to the default location.
- **"Exit program"**: Closes the assistant.

### Example Interaction

1. The assistant greets you based on the time of day: "Good Morning Master."
2. You give a command like "Open YouTube," and the assistant opens YouTube in the web browser.
3. The assistant can also perform additional tasks like playing media, searching Wikipedia, or opening other applications.

## Customization

- You can customize the assistant's voice by changing the `voices` property in the `pyttsx3` engine initialization.
- Modify the paths for images and gifs used in the PyQt5 interface for a personalized look.

## Troubleshooting

- Ensure that your microphone is connected and configured properly for the `speech_recognition` library to work.
- If you experience issues with `PyQt5`, verify that the required version is installed and compatible with your system.


