import threading
import time
from datetime import datetime
from pygame import mixer
import keyboard
import re
from speak import speak


def parse_time_from_text(text):
    match = re.search(r'(\d{1,2}):(\d{2})\s*([ap]\.?\s*m\.?)', text, re.I)
    if match:
        hour, minute, period = match.groups()
        hour = int(hour)
        minute = int(minute)

        # Normalize period to lower case and remove spaces and periods
        period = period.lower().replace('.', '').replace(' ', '')

        if period == 'pm' and hour != 12:
            hour += 12
        elif period == 'am' and hour == 12:
            hour = 0

        return f"{hour:02}:{minute:02}"
    else:
        return None

class Alarm:
    def __init__(self, alarm_time, sound):
        self.alarm_time = alarm_time
        self.sound = sound
        self.thread = threading.Thread(target=self.run)
        self.is_active = True

    def run(self):
        alarm_info = f'Okay, Ive set an alarm for {self.alarm_time}'
        speak(alarm_info)
        while self.is_active:

            current_time = datetime.now().strftime("%H:%M")
            print(f'Alarm running for {self.alarm_time}')
            if current_time == self.alarm_time:
                self.ring()
                break
            time.sleep(60)

    def ring(self):
        snooze = True
        while snooze is True:
            mixer.init()
            mixer.music.load('audio/angelic_voices.mp3')
            mixer.music.play()
            print("Ring Ring!")
            pressed_key = keyboard.read_key()
            if pressed_key == 'space':
                print(pressed_key)
                mixer.music.stop()
                mixer.quit()
                snooze = False
                self.stop()

            else:
                #Snooze
                mixer.music.stop()
                time.sleep(540)
    def start(self):
        self.thread.start()

    def stop(self):
        self.is_active = False

active_alarms = []