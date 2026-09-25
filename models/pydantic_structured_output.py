from langchain import ChatOpenAI
from pydantic import BaseModel, Field
from typing import Literal, Optional
from dotenv import load_dotenv

load_dotenv()

class Review(BaseModel):
    key_themes: list[str] = Field(description="Key themes in the review")
    summary: str = Field(description="Summary in brief of the review")
    sentiment: Literal["positive", "negative", "neutral"] = Field(description="Sentiment of the review")
    pros: Optional[str] = Field(description="Pros of the review", default=None)
    cons: Optional[str] = Field(description="Cons of the review", default=None)
    reviewer: Optional[str] = Field(description="Name of the reviewer", default=None) 

model = ChatOpenAI(model="gpt-4", temperature=0.4)

result = model.with_structured_output(Review)

structured_result = result.invoke("""
This is a review of the new iPhone. The key themes include camera quality, battery life, and design. The summary is that it's a great phone with minor drawbacks. The sentiment is positive. Pros include excellent camera and sleek design. Cons are the high price and average battery life. The reviewer is John Doe.
""")

print(structured_result)