from langchain_community.document_loaders import WebBaseLoader

url = "https://example.com"

loader = WebBaseLoader(url)

documents = loader.load()

for document in documents:
    print(document.page_content)
    print(document.metadata)