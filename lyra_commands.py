import sys
from alarm_clock import parse_time_from_text, Alarm, active_alarms
from speak import speak
from lyra_locale import weather_report, recognize_city
import asyncio

#Command Functions
def exit():
    speak("See you later!")
    sys.exit()




#Command Logic
def command_logic(query):
    #Quit Lyra
    if 'exit' in query:
        exit()
        return True

    #Set Alarm
    elif 'set' in query and 'alarm' in query:
        time = parse_time_from_text(query)
        new_alarm = Alarm(alarm_time=time, sound='path_to_your_alarm_sound.mp3')
        new_alarm.start()  # Start the alarm thread
        active_alarms.append(new_alarm)
        return True

    #Get Weather
    elif 'temperature' in query or 'weather' in query:

        asyncio.run(weather_report(city=recognize_city(query)))
        return True

    else:
        return False
