import openai
import os

print(openai.__version__)

openai.api_key = os.environ["OPENAI_KEY"]

openai.api_key = 'your-api-key'

response = openai.ChatCompletion.create(
    model="text-davinci-003",  # ChatGPT 4.0のモデルを指定します
    messages=[
        {"role": "user", "content": "FXについて教えて"},
    ],
)

print(response.choices[0].text.strip())
