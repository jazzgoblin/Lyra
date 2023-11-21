import speech_recognition as sr
from record_question import record_question
from speak import speak
from openai_processing import query_ai
from lyra_commands import command_logic
recognizer = sr.Recognizer()
keyword = "stevie"
def listen_for_keyword():
    with sr.Microphone() as source:
        print("Speak: ")
        audio = recognizer.listen(source)
    try:
        word = recognizer.recognize_google(audio).lower()
        if word == keyword.lower():
            speak('Go ahead!')
            # Start listening for question.
            print('heard stevie')
            question = record_question()
        elif keyword.lower() in word:
            print(word)
            if command_logic(word) is False:
                query_ai(word)



    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))