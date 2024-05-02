import os
from openai import AzureOpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import langchain

llm = OpenAI(temperature=0.9)
output = llm.predict("日本の総理大臣は誰ですか？")

print(output)

client = AzureOpenAI(
  azure_endpoint = "https://zuu-pdev-us2.openai.azure.com/", 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2024-02-15-preview"
)


message_text = [{"role":"system","content":"You are an AI assistant that helps people find information."}]

completion = client.chat.completions.create(
  model="gpt4-turbo-20k", # model = "deployment_name"
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)
print(completion.choices[0].message.content)
