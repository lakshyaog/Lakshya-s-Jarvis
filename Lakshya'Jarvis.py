import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Replace with your OpenWeatherMap API key
API_KEY = 'your_api_key'
CITY = 'your_city'  # e.g., 'London'

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        return temperature, weather_description
    else:
        return None

def execute_command(command):
    if 'jarvis what is current time' in command:
        
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f" boss The current time is {current_time}.")
    elif 'jarvis tell me todays date' in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f" boss Today's date is {current_date}.")
    elif 'temperature' in command:
        weather = get_weather()
        if weather:
            temperature, description = weather
            speak(f"The current temperature in {CITY} is {temperature} degrees Celsius with {description}.")
        else:
            speak("Sorry, I couldn't fetch the weather information.")
    elif ' jarvis open youtube' in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube boss.")
    elif 'how are you' in command:
        speak("i am fine boss what about you boss")
    elif 'i am also fine jarvis' in command:
        speak(" good to hear that boss")
    
    elif 'jarvis shutdown' in command:
        speak("shuting down gooodbyee boss!")
        return False
    else:
        speak("i don't understand that boss give me the brief detail about that topic.")
    
    return True

def main():
    speak("Hello, I am  Jarvis . I am designed by lakshya solanki?")
    speak("i am here to provide u details about your queries, how can i help u boss")
    while True:
        command = listen()
        if not execute_command(command):
            break

if __name__ == "__main__":
    main()





