from google.cloud import bigquery
import os
from openai import AzureOpenAI

# クライアントの初期化
client = bigquery.Client()

# クエリの設定
query = """
SELECT title, category
FROM `zuu-infra.prd_to_articles.to_article_urls`
ORDER BY title DESC
LIMIT 5;
"""



# クエリの実行と結果の取得
query_job = client.query(query)  # APIリクエストを実行

results_list = []
# 結果をイテレート

for row in query_job:
    # Row values can be accessed by field name or index
    results_list.append({
        "title": row['title'],
        "category": row['category']
    })




print(results_list)


# Azure OpenAI クライアントの初期化
client = AzureOpenAI(
    azure_endpoint="https://zuu-pdev-us2.openai.azure.com/",
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-15-preview"
)

# OpenAIに送るシステムメッセージで、リスト内のtitleだけを取り出すように指示
message_text = [
    {"role": "system", "content": "Given the following data, extract only the titles and return them as an array."},
    {"role": "user", "content": str(results_list)}
]

# OpenAI APIを呼び出し
completion = client.chat.completions.create(
    model="gpt4-turbo-saino01",  # モデル名はデプロイメント名に置き換え
    messages=message_text,
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
)


print(completion.result)

api_answer = completion.result

""" 
client = AzureOpenAI(
  azure_endpoint = "https://zuu-pdev-us2.openai.azure.com/", 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2024-02-15-preview"
)


message_text = [{"role":"system","content":answer}]

completion = client.chat.completions.create(
  model="gpt4-turbo-saino01", # model = "deployment_name"
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
) 
"""




# データセットの設定
dataset_id = "{}.your_new_dataset".format(client.project)
dataset = bigquery.Dataset(dataset_id)
dataset.location = "US"

# データセットの作成
dataset = client.create_dataset(dataset, timeout=30)
print("Created dataset {}.{}".format(client.project, dataset.dataset_id))

# テーブルの設定
table_id = "{}.{}.your_new_table".format(client.project, dataset.dataset_id)
schema = [
    bigquery.SchemaField("title", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("category", "STRING", mode="REQUIRED"),  # データ型をSTRINGに修正
]

table = bigquery.Table(table_id, schema=schema)

# テーブルの作成
table = client.create_table(table)
print("Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id))

rows_to_insert = api_ansewer

# データの挿入
errors = client.insert_rows_json(table, rows_to_insert)
if errors == []:
    print("New rows have been added.")
else:
    print("Encountered errors while inserting rows: {}".format(errors))

