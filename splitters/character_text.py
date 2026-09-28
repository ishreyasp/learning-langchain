from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    chunk_size=9,
    chunk_overlap=0,
    separator=" ",
)

text = "This is a sample text that will be split into chunks based on the character text splitter configuration."

chunks = splitter.split_text(text)

for chunk in chunks:
    print(chunk)