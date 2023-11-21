import python_weather
import spacy
from speak import speak
def recognize_city(query):
    city = None
    nlp = spacy.load('en_core_web_sm')
    processed_query = nlp(query)
    for ent in processed_query.ents:
        if ent.label_ == 'GPE':
            city = ent.text
    return city

async def weather_report(city):
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get(city)

        speak(f'Its currently {weather.current.temperature} degrees in {city}.')