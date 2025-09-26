import speech_recognition as sr
import pyttsx3
import webbrowser

# Dummy reply function to replace OpenAI call
def Reply(question):
    # Just echo the question or give canned responses for testing
    question = question.lower()
    if "hello" in question:
        return "Hello! How can I help you today?"
    elif "open youtube" in question:
        return "Opening YouTube."
    elif "open google" in question:
        return "Opening Google."
    elif "bye" in question:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I don't know how to respond to that."

# Text to speech 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print('Listening .......')
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print('Recognizing ....')
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        print("Say that again .....")
        return "None"
    return query

if __name__ == '__main__':
    speak("Hello! How are you?")
    while True: 
        query = takeCommand().lower()
        if query == 'none':
            continue
        
        ans = Reply(query)
        print(ans)
        speak(ans)
        
        # Browser commands
        if "open youtube" in query: 
            webbrowser.open('https://www.youtube.com')
        elif "open google" in query: 
            webbrowser.open('https://www.google.com')
        elif "bye" in query:
            break
