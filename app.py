import streamlit as st
import os
import uuid
from extractor import extract_pdf_content
from llm_handler import query_pdf_with_llm

# --- Page setup ---
st.set_page_config(page_title=" AI PDF Assistant", layout="centered")
st.title(" AI PDF Assistant")

# --- Sidebar ---
with st.sidebar:
    st.markdown("###  Instructions")
    st.markdown("1. Upload a PDF\n2. Ask questions\n3. Download answers")
    theme = st.radio(" Theme", ["Light", "Dark"])
    st.markdown("---")
    st.caption("Made with love  using Streamlit & Transformers")

# --- Theme toggle ---
if theme == "Dark":
    st.markdown("""
        <style>
        .stApp {
            background-color: #0e1117;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

# --- File Upload ---
uploaded_file = st.file_uploader(" Upload a PDF file", type="pdf")
session_id = st.session_state.get("session_id", str(uuid.uuid4()))
st.session_state.session_id = session_id

pdf_folder = "uploaded_pdfs"
os.makedirs(pdf_folder, exist_ok=True)

if uploaded_file:
    pdf_path = os.path.join(pdf_folder, uploaded_file.name)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner(" Extracting text from PDF..."):
        extracted = extract_pdf_content(pdf_path)
        all_text = "\n\n".join([f"[Page {e['page']}]: {e['text']}" for e in extracted])

    st.success(f" Extracted '{uploaded_file.name}' successfully.")

    # --- Tabs UI ---
    tab1, tab2 = st.tabs([" Extracted Text", "❓ Ask Questions"])

    with tab1:
        st.text_area(" Full Extracted Text", all_text, height=300)

    with tab2:
        st.markdown("### ❓ Ask questions about the PDF")
        if "qa_history" not in st.session_state:
            st.session_state.qa_history = []

        user_query = st.text_input(" Your question:")

        if user_query:
            with st.spinner(" Generating answer..."):
                response = query_pdf_with_llm(all_text, user_query)

            st.session_state.qa_history.append((user_query, response))

        if st.session_state.qa_history:
            st.markdown("###  Question History")
            for idx, (q, a) in enumerate(reversed(st.session_state.qa_history), 1):
                st.markdown(f"**{idx}. Q:** {q}")
                st.markdown(f"**A:** {a}")
                st.markdown("---")

            last_q, last_a = st.session_state.qa_history[-1]
            st.download_button("⬇️ Download Last Answer", last_a, file_name="answer.txt", mime="text/plain")

else:
    st.info("Upload a PDF to get started.")
