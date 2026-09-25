from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Literal, Optional
from dotenv import load_dotenv

load_dotenv()

class Review(TypedDict):
    key_themes: Annotated[list[str], "Key themes in the review"]
    summary: Annotated[str, "Summary in brief of the review"]
    sentiment: Annotated[Literal["positive", "negative", "neutral"], "Sentiment of the review"]
    pros: Annotated[Optional[str], "Pros of the review"]
    cons: Annotated[Optional[str], "Cons of the review"]
    reviewer: Annotated[Optional[str], "Name of the reviewer"]

model = ChatOpenAI(model="gpt-4", temperature=0.4)

result = model.with_structured_output(Review)

structured_result = result.invoke("""
This is a review of the new iPhone. The key themes include camera quality, battery life, and design. The summary is that it's a great phone with minor drawbacks. The sentiment is positive. Pros include excellent camera and sleek design. Cons are the high price and average battery life. The reviewer is John Doe.
""")

print(structured_result)