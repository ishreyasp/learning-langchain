from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a 10 words linkedin post on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Write a 10 words instagram post on {topic}',
    input_variables=['topic']
)

chain = RunnableParallel({
    'linkedin': prompt1 | model | parser,
    'instagram': prompt2 | model | parser
})

result = chain.invoke({'topic': 'AI technology'})

print(result['linkedin'])
print(result['instagram'])