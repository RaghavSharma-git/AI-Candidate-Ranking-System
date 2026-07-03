# 🤖 AI Candidate Ranking System

An AI-powered recruitment platform that intelligently ranks candidates based on a Job Description using Semantic AI, Skill Matching, Experience Analysis, Behavior Signals, and Career Intent Scoring.

Unlike traditional Applicant Tracking Systems (ATS) that rely on keyword matching, this system understands the semantic meaning of resumes and job descriptions to identify the most relevant candidates.

---

# 🚀 Features

- 🧠 Semantic Resume Ranking using Sentence Transformers
- 🎯 Skill Matching
- 💼 Experience Matching
- 📊 Recruiter Behavior Scoring
- 🚀 Career Intent Detection
- 💡 Explainable AI Ranking
- 📄 Job Description Upload (.docx/.txt)
- 📂 Candidate Dataset Upload (.json/.jsonl)
- 📈 Interactive Streamlit Dashboard
- 📥 Export Top Candidates as CSV
- ⚡ Batch Embedding Generation
- 🗄️ Embedding Cache Support
- 🔍 FAISS-based Vector Search (Scalable Architecture)

---

# 🏗️ System Architecture

```
                 Job Description
                        │
                        ▼
                JD Parser
                        │
                        ▼
        Sentence Transformer Encoder
                        │
                        ▼
                JD Embedding
                        │
                        ▼
             FAISS Vector Search
                        │
               Top-K Candidates
                        │
                        ▼
             Skill Matching Engine
                        │
                        ▼
          Experience Evaluation
                        │
                        ▼
          Recruiter Behavior Score
                        │
                        ▼
             Career Intent Score
                        │
                        ▼
            Explainable AI Module
                        │
                        ▼
             Final Candidate Ranking
                        │
                        ▼
        Streamlit Dashboard + CSV Export
```

---

# 🧠 Ranking Methodology

Each candidate is evaluated using multiple signals.

| Signal | Weight |
|---------|--------|
| Semantic Similarity | 40% |
| Skill Match | 30% |
| Experience | 15% |
| Behavior Score | 10% |
| Intent Score | 5% |

Final Score

```
Final Score =
0.40 × Semantic +
0.30 × Skill +
0.15 × Experience +
0.10 × Behavior +
0.05 × Intent
```

Candidates are sorted based on the Final Score and the Top-N candidates are recommended.

---

# ⚙️ Tech Stack

### AI / Machine Learning

- Sentence Transformers
- all-MiniLM-L6-v2
- Scikit-learn
- FAISS

### Backend

- Python

### Frontend

- Streamlit

### Data Processing

- Pandas
- NumPy
- JSON
- JSONL

---

# 📂 Project Structure

```
AI-Candidate-Ranking-System
│
├── data/
│   ├── sample_candidates.json
│   ├── candidates.jsonl
│   ├── job_description.docx
│   ├── candidate_embeddings.pkl
│   └── candidate_index.faiss
│
├── models/
│   ├── semantic_ranker.py
│   ├── skill_matcher.py
│   ├── experience_matcher.py
│   ├── signal_scorer.py
│   ├── intent_scorer.py
│   ├── final_ranker.py
│   ├── explainer.py
│   └── ranker.py
│
├── utils/
│   ├── document_builder.py
│   ├── jd_loader.py
│   ├── jsonl_loader.py
│   └── cache_embeddings.py
│
├── output/
│   └── submission.csv
│
├── streamlit_app.py
├── app.py
├── build_index.py
├── requirements.txt
└── README.md
```

---

# 📊 Dashboard

The Streamlit dashboard provides:

- Candidate Ranking
- Ranking Statistics
- Top Candidates
- Candidate Details
- Semantic Score
- Skill Score
- Experience Score
- Behavior Score
- Intent Score
- Matched Skills
- Missing Skills
- AI Explanation
- CSV Download

---

# 📈 Scalability

The system is designed for large-scale candidate datasets.

Current optimizations include:

- Batch Embedding Generation
- Embedding Cache
- FAISS Vector Index
- Top-K Candidate Retrieval

This architecture enables efficient semantic search across large resume collections.

---

# 💡 Explainable AI

For every ranked candidate, the system generates:

- Semantic relevance
- Skill match summary
- Missing skills
- Experience evaluation
- Behavior insights
- Career intent analysis

This improves transparency and recruiter trust.

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Candidate-Ranking-System.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run streamlit_app.py
```

---

# 📥 Input Formats

## Job Description

- DOCX
- TXT

## Candidate Dataset

- JSON
- JSONL

---

# 📤 Output

- Ranked Candidate List
- AI Explanation
- Top 100 CSV
- Recruiter Dashboard

---

# 🔮 Future Enhancements

- PDF Resume Parsing
- Resume Upload (ZIP)
- OCR Support
- Hybrid Search (Semantic + Keyword)
- LLM-powered Resume Summarization
- ATS Integration
- Cloud Deployment
- Multi-language Resume Support

---

# 👨‍💻 Author

**Raghav Sharma**

BCA Student | AI & Software Development Enthusiast

---

# ⭐ If you found this project useful, don't forget to star the repository!
