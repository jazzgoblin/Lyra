import configparser
import os
is_file = os.path.isfile('config.ini')
config = configparser.ConfigParser()

if is_file is False:
    ai_key = input("Enter your AI Key: ")
    config['DEFAULT'] = {'OpenAI_API_Key': ai_key,
                         'Expectations': "Lyra is an innovative, voice-activated assistant device, designed to provide comprehensive and interactive assistance to users in their daily lives. Integrated with OpenAI's powerful GPT-3.5 language model, Lyra offers a unique blend of conversational AI capabilities, making it an indispensable tool for information access, task management, learning, and entertainment.",
                         'DeleteRecordings': 'True'
                         }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

config.read('config.ini')

api_key = config['DEFAULT']['openai_api_key']
expectations = config['DEFAULT']['expectations']
delete_recordings = config['DEFAULT']['deleterecordings']