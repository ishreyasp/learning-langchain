from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.4)

st.header("LangChain Prompt UI")

paper_input = st.selectbox(
    "Select a paper:",
    ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"]
)

length_input = st.selectbox(
    "Select the length of the summary:",
    ["Short", "Medium", "Long"]
)

prompt_template = load_prompt('prompt_template.json')

formatted_prompt = prompt_template.format(
            paper_input=paper_input, 
            length_input=length_input
        )

if st.button("Generate Summary"):
    result = model.invoke(formatted_prompt)
    st.write(result.content)