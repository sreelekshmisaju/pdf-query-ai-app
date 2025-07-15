# 📄 AI PDF Content Query App

A robust, offline-capable application for extracting and querying content from PDF documents using AI. Built with Streamlit and Hugging Face Transformers (DistilBERT), this tool allows users to upload academic or technical PDFs and ask contextual questions in natural language. No OpenAI or external API key required.

---

## 🎯 Project Objectives

- Extract structured text from academic or scanned PDFs.
- Enable users to ask multiple questions about the content.
- Maintain per-session Q&A history and downloadable responses.
- Provide an intuitive, theme-enabled, responsive UI.
- Ensure offline/local operation using Hugging Face models.

---

## ⚙️ Methodology

This app uses:
- `PyMuPDF (fitz)` to extract per-page text from PDFs.
- Hugging Face Transformers (`distilbert-base-cased-distilled-squad`) to answer user queries.
- Streamlit for an interactive web interface.
- Optional logging for tracking all LLM interactions.

The input PDF is processed on upload, and extracted text is passed to the QA model. User questions are run against this context and answers are displayed with a download option and session history.

---

## 🚀 Key Features

- 🤖 Powered by Hugging Face QA model (DistilBERT)
- 📄 Upload any academic PDF (persistent)
- 💬 Ask multiple questions with real-time answers
- 📜 View complete session Q&A history
- ⬇️ Download last answer as `.txt`
- 🎨 Custom theme + dark/light toggle
- 📱 Responsive UI using Streamlit
- 🧾 Logs stored locally for audit/debug

---

## 📁 Directory Structure

```

pdf-query-ai-app/
├── app.py                # Main Streamlit frontend logic
├── extractor.py          # PDF parsing and text extraction
├── llm\_handler.py        # LLM-based QA logic (Hugging Face)
├── uploaded\_pdfs/        # Stores uploaded PDF files
├── logs/
│   └── llm\_logs.txt      # Logs of user questions & responses
├── .streamlit/
│   └── config.toml       # Theme configuration
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

````

---

## 🧰 Dependencies

Install using:

```bash
pip install -r requirements.txt
````

Required libraries:

* `streamlit`
* `PyMuPDF` (`fitz`)
* `transformers`
* `torch`
* `sentencepiece`

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sreelekshmisaju/pdf-query-ai-app.git
cd pdf-query-ai-app
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate
venv\Scripts\activate        # Windows
# OR
source venv/bin/activate     # macOS/Linux
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Open the provided local URL in your browser (e.g. [http://localhost:8501](http://localhost:8501))

---

## 📦 Deployment (Streamlit Cloud)

1. Push the project to your GitHub repository.
2. Visit [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your GitHub repo and click **Deploy**.
4. No API keys needed.
5. You can persist files via session state or optionally connect to cloud storage.

---

## 📜 LLM Interaction Logging

All user questions and generated answers are saved in:

```
logs/llm_logs.txt
```

Example:

```
Q: What is the main objective of the document?
A: To analyze the impact of digital finance in Indian villages.

Q: Who authored this document?
A: Ministry of Rural Development.
```

---

## 🧪 Example Usage

**Step-by-step**:

1. Upload a report or thesis PDF
2. Ask: "What is the summary of this paper?"
3. Ask follow-ups like:

   * "Who are the authors?"
   * "What are the conclusions?"
4. Download the latest answer

---

## 💡 Troubleshooting

| Issue                                | Solution                                                |
| ------------------------------------ | ------------------------------------------------------- |
| `No module named 'fitz'`             | Run `pip install PyMuPDF`                               |
| Hugging Face model not loading       | Check your internet connection for model download       |
| Streamlit crashes with long PDF text | Limit `all_text[:3000]` or split content using chunks   |
| App UI broken on mobile              | Use full-screen view or increase layout width in config |

---

## 🎨 Theme Customization

Edit `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#4B8BBE"
backgroundColor = "#ffffff"
textColor = "#262730"
font = "sans serif"
```

Or toggle Dark Mode within the sidebar.

---

## 🔮 Future Roadmap

* 🔎 Semantic search with vector embeddings
* 🧠 Upgrade to multilingual QA models
* 🧾 Export full Q\&A sessions to PDF
* 🗃️ Multi-document Q\&A with ranking
* 🌐 Option to run model via API if needed

---

## 🛡 License

Licensed under the **MIT License**.

---

## 🤝 Acknowledgements

* [Streamlit](https://streamlit.io/)
* [Hugging Face Transformers](https://huggingface.co/transformers/)
* [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)

---


