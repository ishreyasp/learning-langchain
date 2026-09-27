from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='path-to-folder',
    glob='*.pdf',
    loader_cls=PyPDFLoader,
)

doc = loader.load()

documents = loader.lazy_load()

for document in documents:
    print(document.page_content)
    print(document.metadata)