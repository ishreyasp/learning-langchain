from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

def word_count(text: str):
    return len(text.split())

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

joke_gen_chain = prompt1 | model | parser

parallel_chain = RunnableParallel({
    'passthru': RunnablePassthrough(),
    'counter': RunnableLambda(word_count)
})

chain = joke_gen_chain | parallel_chain

result = chain.invoke({"topic": "cats"})

print(result)