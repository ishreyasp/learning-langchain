from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.4)

chat_template = ChatPromptTemplate([
    ('system', 'You are a helful {domain} assistant'),
    ('human', 'Explain in simple terms what is {topic}'),
])

prompt = chat_template.format(domain="programming", topic="Python")

print(prompt)