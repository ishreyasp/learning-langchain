from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
    input_variables=["paper_input", "length_input"],
    validate_template=True,
    template="""
    Summarize the paper titled '{paper_input}' with the following specifications:
    Explanation Length: {length_input}

    1. Mathematical Details:
        - Include relevant mathematical equations if present in the papaer.
        - Include relevenat mathematical concepts using simple and inituitive explanations.
    2. Key Contributions:
        - Highlight the main contributions of the paper.
    3. Conclusion:
        - Provide a concise summary of the paper's findings and their implications.
    If certain information is not available in the paper , respond with: "Information not available." instead of guessing.
    Ensure the summary is clear, accurate, and aligned with the provided length specification.
    """
)

prompt_template.save("prompt_template.json")
