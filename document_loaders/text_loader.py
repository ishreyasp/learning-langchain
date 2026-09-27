from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf-8')

documents = loader.load()

print(type(documents))
print(len(documents))
print(documents[0])
print(documents[0].page_content)
print(documents[0].metadata)

model = ChatOpenAI()

parser = StrOutputParser()

prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text:\n {text}"
)

chain = prompt | model | parser

result = chain.invoke({"text": documents[0].page_content})
print(result)