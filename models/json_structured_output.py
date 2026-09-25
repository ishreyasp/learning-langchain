from langchain import ChatOpenAI
import json
from dotenv import load_dotenv

load_dotenv()

json_schema = {
    "title": "Movie",
    "description": "A movie with details",
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "description": "The title of the movie"
        },
        "year": {
            "type": "integer",
            "description": "The year the movie was released"
        },
        "director": {
            "type": "string",
            "description": "The director of the movie"
        },
        "rating": {
            "type": "number",
            "description": "The movie's rating out of 10"
        }
    },
    "required": ["title", "year", "director", "rating"]
} 

model = ChatOpenAI(model="gpt-4", temperature=0.4)

result = model.with_structured_output(json_schema)

structured_result = result.invoke("""
This is a review of the new iPhone. The key themes include camera quality, battery life, and design. The summary is that it's a great phone with minor drawbacks. The sentiment is positive. Pros include excellent camera and sleek design. Cons are the high price and average battery life. The reviewer is John Doe.
""")

print(structured_result)