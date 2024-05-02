from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain import OpenAI

# OpenAIのAPIキーを設定
api_key = "YOUR_OPENAI_API_KEY"

# OpenAIクライアントを作成
openai_client = OpenAI(api_key=api_key)

# チャットモデルを作成
chat_model = ChatOpenAI(openai_client)

# 対話を生成する関数
def generate_dialogue():
    # システムメッセージを作成
    system_message = SystemMessage(content="You are a helpful assistant.")

    # ユーザーメッセージを作成
    user_message_1 = HumanMessage(content="Does Azure OpenAI support customer managed keys?")
    user_message_2 = HumanMessage(content="Do other Azure AI services support this too?")

    # 対話を生成
    response_1 = chat_model.generate_response(system_message, user_message_1)
    response_2 = chat_model.generate_response(response_1, user_message_2)

    # 応答を出力
    print("Response 1:", response_1.content)
    print("Response 2:", response_2.content)

# 対話を生成
generate_dialogue()
