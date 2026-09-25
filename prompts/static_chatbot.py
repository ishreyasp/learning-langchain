from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.4)

chat_history = [
    SystemMessage(content="You are a helpful AI assistant."),
]

while True:
    usr_ip = input("You: ")
    if usr_ip == 'exit':
        break
    chat_history.append(HumanMessage(content=usr_ip))
    response = model.invoke(chat_history)
    print("AI:", response.content)
    chat_history.append(AIMessage(content=response.content))

print(chat_history)