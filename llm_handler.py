from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load QA model
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def chunk_text(text, chunk_size=400):
    """
    Splits text into chunks of approx `chunk_size` words.
    """
    words = text.split()
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

def find_best_context(chunks, question):
    """
    Use TF-IDF + cosine similarity to get the most relevant chunk to the question.
    """
    vectorizer = TfidfVectorizer().fit([question] + chunks)
    vectors = vectorizer.transform([question] + chunks)
    sims = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    best_idx = sims.argmax()
    return chunks[best_idx]

def query_pdf_with_llm(extracted_text, question):
    chunks = chunk_text(extracted_text)
    best_context = find_best_context(chunks, question)

    result = qa_pipeline(question=question, context=best_context)
    return result["answer"]

