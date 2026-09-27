from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke: {joke}',
    input_variables=['joke']
)

joke_gen_chain = prompt1 | model | parser

parallel_chain = RunnableParallel({
    'passthru': RunnablePassthrough(),
    'explaination': prompt2 | model | parser
})

chain = joke_gen_chain | parallel_chain

result = chain.invoke({"topic": "cats"})

print(result)