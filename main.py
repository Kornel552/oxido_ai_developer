from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv("API_KEY")
model ='gpt-3.5-turbo'

response = openai.ChatCompletion.create(
    model=model,
    messages=[
        {
            'role': 'system',
            'content': 'Return full sentence'
        },
        {
            'role': 'user',
            'content': 'say hello'
        }
    ],
    temperature=1,
    max_tokens=256,
)

resp = response.choices[0].message.content
print(resp)
