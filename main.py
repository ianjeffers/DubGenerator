from gtts import gTTS
from googletrans import Translator

import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()
translator = Translator()


# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak

language = input("Please enter a language: \n")

while (1):
    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using google to recognize audio
            recorded_text = r.recognize_google(audio2)
            recorded_text = recorded_text.lower()
            print("Recorded text:\n",recorded_text)
            translated_text = translator.translate(recorded_text, src='en', dest=language).text
            print("Translated text:\n", translated_text)

            myobj = gTTS(text=translated_text, lang='de', slow=False)
            myobj.save("Test" + language + ".mp3")

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("No Audio")