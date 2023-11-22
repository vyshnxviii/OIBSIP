"""PROJECT 1 - VOICE ASSISTANT"""

import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to capture user command through microphone
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you repeat?")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error with the request.")
        return ""

# Function to perform web search using the provided query
def web_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    
# Function to handle user commands and execute corresponding actions
def assistant(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            speak(f"Searching Google for {query}")
            web_search(query)
        else:
            speak("What do you want me to search for?")
    else:
        speak("I'm not sure how to help with that.")

# Main function to initiate the voice assistant
def main():
    speak("Welcome! How can I assist you today?")
    while True:
        command = take_command()
        assistant(command)

# Entry point to the program
if __name__ == "__main__":
    main()
