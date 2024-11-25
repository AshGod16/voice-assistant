import speech_recognition as sr
from transformers import pipeline
import pyttsx3
import json
import datetime
import webbrowser
import os
from tqdm import tqdm
from transformers.utils import logging
import sys
from pathlib import Path

class VoiceAssistant:
    def __init__(self):
        # Configure progress bar for downloads
        cache_dir = Path.home() / '.voice_assistant_cache'
        cache_dir.mkdir(exist_ok=True)
        os.environ['TRANSFORMERS_CACHE'] = str(cache_dir)
        
        logging.set_verbosity_warning()
        print("Initializing voice assistant...")
        
        self.nlp = pipeline("text-classification", 
                          model="facebook/bart-large-mnli",
                          device=-1)
        
        self.recognizer = sr.Recognizer()
        self.speaker = pyttsx3.init()
        
        self.intents = {
            "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
            "weather": ["weather", "temperature", "forecast"],
            "time": ["time", "current time", "what time"],
            "web_search": ["search for", "look up", "find"],
            "music": ["play music", "play song", "start music"]
        }
        print("Initialization complete!")

    def download_progress(self, current, total):
        if self.progress_bar is None:
            self.progress_bar = tqdm(total=total, unit='iB', unit_scale=True)
        self.progress_bar.update(current - self.progress_bar.n)
        if current >= total:
            self.progress_bar.close()
            self.progress_bar = None

    def listen(self):
        with sr.Microphone() as source:
            print("\nListening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            
        try:
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError:
            print("Could not request results")
            return None

    def classify_intent(self, text):
        if not text:
            return None
        candidate_labels = list(self.intents.keys())
        result = self.nlp(text, candidate_labels, multi_label=False)
        return result['labels'][0]

    def speak(self, text):
        print(f"Assistant: {text}")
        self.speaker.say(text)
        self.speaker.runAndWait()

    def handle_intent(self, intent, text):
        if intent == "greeting":
            current_hour = datetime.datetime.now().hour
            if 5 <= current_hour < 12:
                response = "Good morning!"
            elif 12 <= current_hour < 17:
                response = "Good afternoon!"
            else:
                response = "Good evening!"
                
        elif intent == "time":
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            response = f"The current time is {current_time}"
            
        elif intent == "weather":
            response = "I'm sorry, weather functionality is not implemented yet"
            
        elif intent == "web_search":
            search_query = text.split("search for")[-1].strip()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            response = f"Searching for {search_query}"
            
        elif intent == "music":
            response = "I'm sorry, music functionality is not implemented yet"
            
        else:
            response = "I'm not sure how to help with that"
            
        return response

    def run(self):
        self.speak("Hello! How can I help you today?")
        while True:
            text = self.listen()
            if text:
                intent = self.classify_intent(text)
                response = self.handle_intent(intent, text)
                self.speak(response)

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()