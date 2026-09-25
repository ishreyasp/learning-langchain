from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

document = [
    "Virat Kohli is a cricket player",
    "Tom Cruise is an actor",
    "Elon Musk is an entrepreneur",
    "Bill Gates is a software entrepreneur",
]

query = "Who is a cricket player?"

document_embedding = embeddings.embed_documents(document)
query_embedding = embeddings.embed_query(query)

scores = cosine_similarity([query_embedding], document_embedding)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(document[index])
print("Similarity score:", score)