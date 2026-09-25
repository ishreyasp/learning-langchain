from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description='Give the sentiment of the feedback')

pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)

model = ChatOpenAI(model="gpt-4", temperature=0.4)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': pydantic_parser.get_format_instruction()}
)

classifier_chain = prompt1 | model | pydantic_parser

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback: \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback: \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "positive", prompt2 | model | StrOutputParser()),
    (lambda x:x.sentiment == "negative", prompt3 | model | StrOutputParser()),
    RunnableLambda(lambda x: "Unknown sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({"feedback": "I love this product!"}))

chain.get_graph().print_ascii()