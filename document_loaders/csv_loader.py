from langchain_community.document_loaders import CSVLoader

loader = CSVLoader('file.csv')

documents = loader.load()

for document in documents:
    print(document.page_content)
    print(document.metadata)