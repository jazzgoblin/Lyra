from openai import OpenAI
from config import api_key, expectations
from speak import speak

client = OpenAI(api_key=api_key)
def query_ai(question):
  print('Good question. Let me think about that.')
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": expectations},
      {"role": "user", "content": question}
    ]
  )
  answer = completion.choices[0].message.content
  print(answer)

  speak(answer)
