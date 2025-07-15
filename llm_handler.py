from transformers import pipeline

# Load question-answering pipeline (lightweight and fast)
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def query_pdf_with_llm(extracted_text, question):
    # Limit context length (Hugging Face models can't handle too much text)
    context = extracted_text[:3000]  # truncate long PDFs

    result = qa_pipeline(question=question, context=context)
    return result["answer"]

