import os
from openai import AzureOpenAI

#変数を与えた場合のAzureのプロンプティング
assistant_name = "helpful assistant"
user_question1 = "Does Azure OpenAI support customer managed keys?"
assistant_response1 = "Yes, customer managed keys are supported by Azure OpenAI."
user_question2 = "Do other Azure AI services support this too?"

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version="2024-02-01"
)

response = client.chat.completions.create(
    model="gpt4-turbo-20k", # model = "deployment_name".
        messages = [
        {"role": "system", "content": f"You are a {assistant_name}."},
        {"role": "user", "content": user_question1},
        {"role": "assistant", "content": assistant_response1},
        {"role": "user", "content": user_question2}
    ]
  )

print(response.choices[0].message.content)
