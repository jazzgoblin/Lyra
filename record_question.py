import speech_recognition as sr
from openai_processing import query_ai
from lyra_commands import command_logic

recognizer = sr.Recognizer()
def record_question():
    with sr.Microphone() as source:
        print("Ask Question: ")
        audio = recognizer.listen(source)

    try:
        question = recognizer.recognize_google(audio).lower()
        # Start listening for question.
        print(question)
        if not command_logic(question):
            query_ai(question)

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))