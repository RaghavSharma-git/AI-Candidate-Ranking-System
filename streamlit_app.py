import streamlit as st
import json
import pandas as pd
import pdfplumber
import docx

from models.ranker import rank_candidates

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Candidate Ranking System",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Candidate Ranking System")

st.caption("Upload a Job Description and Candidate Dataset to identify the best matching candidates using AI-powered ranking.")

st.markdown("""
### AI Powered Candidate Ranking Dashboard

Rank candidates using

- Semantic AI
- Skill Matching
- Experience Analysis
- Behavior Analysis
- Intent Detection
""")

# ==========================================
# SESSION STATE
# ==========================================

if "ranking" not in st.session_state:
    st.session_state.ranking = None

# ==========================================
# FUNCTIONS
# ==========================================

def read_docx(uploaded_file):

    document = docx.Document(uploaded_file)

    text = []

    for para in document.paragraphs:
        text.append(para.text)

    return "\n".join(text)


def read_pdf(uploaded_file):

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

    return text


def extract_jd(uploaded_file):

    if uploaded_file.name.endswith(".pdf"):

        return read_pdf(uploaded_file)

    elif uploaded_file.name.endswith(".docx"):

        return read_docx(uploaded_file)

    elif uploaded_file.name.endswith(".txt"):

        return uploaded_file.read().decode("utf-8")

    return ""


# ==========================================
# JOB DESCRIPTION
# ==========================================

st.header("📄 Job Description")

uploaded_jd = st.file_uploader(

    "Upload Job Description",

    type=["pdf", "docx", "txt"]

)

jd = st.text_area(

    "OR Paste Job Description",

    height=220,

    placeholder="Paste Job Description here..."

)

if uploaded_jd is not None:

    jd = extract_jd(uploaded_jd)

    st.success("Job Description Loaded Successfully")

# ==========================================
# RESUME UPLOAD
# ==========================================

st.header("📂 Candidate Dataset")

uploaded_resume_file = st.file_uploader(

    "Upload Candidate Dataset (.json / .jsonl)",

    type=["json", "jsonl"]

)

st.info(
"""
Supported Candidate Dataset Formats

✅ JSON

✅ JSONL

✔ Upload any valid candidate dataset

✔ Supports small, medium and large datasets

✔ Automatically ranks all uploaded candidates
"""
)

# ==========================================
# BUTTON
# ==========================================

if st.button("🚀 Rank Candidates"):

    if jd.strip() == "":

        st.warning("Please provide a Job Description.")

        st.stop()

    if uploaded_resume_file is None:

        st.warning("Please upload candidate dataset.")

        st.stop()

    with st.spinner("Ranking Candidates..."):

        # JSON
        if uploaded_resume_file.name.endswith(".json"):

            candidates = json.load(uploaded_resume_file)

        # JSONL
        else:

            candidates = []

            for line in uploaded_resume_file:

                candidates.append(
                    json.loads(line)
                )

        ranking = rank_candidates(

            jd,

            candidates

        )

        st.session_state.ranking = ranking

        st.success(
            f"Successfully Ranked {len(ranking):,} Candidates"
        )

        # ============================================================
# SHOW RESULTS
# ============================================================

if st.session_state.ranking is not None:

    ranking = st.session_state.ranking

    st.divider()

    st.header("📊 Ranking Statistics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Candidates",
        len(ranking)
    )

    col2.metric(
        "Best Score",
        f"{ranking[0]['final_score']:.2f}"
    )

    avg = sum(
        c["final_score"]
        for c in ranking
    ) / len(ranking)

    col3.metric(
        "Average Score",
        f"{avg:.2f}"
    )

    col4.metric(
        "Highest Ranked Candidate",
        ranking[0]["name"]
    )

    st.success(
        f"🏆 Best Candidate : {ranking[0]['name']} ({ranking[0]['final_score']:.2f})"
    )

    st.divider()

    # ============================================================
    # TOP 10 TABLE
    # ============================================================

    st.header("🏆 Top Ranked Candidates")

    table = []

    for rank, candidate in enumerate(
        ranking[:10],
        start=1
    ):

        table.append({

            "Rank": rank,

            "Candidate ID":
            candidate["candidate_id"],

            "Name":
            candidate["name"],

            "Final Score":
            round(candidate["final_score"],2),

            "Semantic":
            round(candidate["semantic_score"],2),

            "Skill":
            round(candidate["skill_score"],2),

            "Experience":
            round(candidate["experience_score"],2),

            "Behavior":
            round(candidate["behavior_score"],2),

            "Intent":
            round(candidate["intent_score"],2)

        })

    df = pd.DataFrame(table)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ============================================================
    # SELECT CANDIDATE
    # ============================================================

    candidate_names = [
        c["name"]
        for c in ranking[:10]
    ]

    selected = st.selectbox(

        "👤 Candidate Details",

        candidate_names

    )

    selected_candidate = next(

        c

        for c in ranking

        if c["name"] == selected

    )

    st.divider()

    st.header(f"👤 {selected_candidate['name']}")

    left, right = st.columns(2)

    with left:

        st.metric(

            "Final Score",

            f"{selected_candidate['final_score']:.2f}"

        )

        st.write("Semantic Score")

        st.progress(
            float(selected_candidate["semantic_score"])
        )

        st.caption(
            f"{selected_candidate['semantic_score']:.2f}"
        )

        st.write("Skill Score")

        st.progress(
            float(selected_candidate["skill_score"])
        )

        st.caption(
            f"{selected_candidate['skill_score']:.2f}"
        )

    with right:

        st.write("Experience Score")

        st.progress(
            float(selected_candidate["experience_score"])
        )

        st.caption(
            f"{selected_candidate['experience_score']:.2f}"
        )

        st.write("Behavior Score")

        st.progress(
            float(selected_candidate["behavior_score"])
        )

        st.caption(
            f"{selected_candidate['behavior_score']:.2f}"
        )

        st.write("Intent Score")

        st.progress(
            float(selected_candidate["intent_score"])
        )

        st.caption(
            f"{selected_candidate['intent_score']:.2f}"
        )

    st.divider()

    # ============================================================
    # SKILLS
    # ============================================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matched Skills")

        if selected_candidate["matched_skills"]:

            for skill in selected_candidate["matched_skills"]:

                st.success(skill)

        else:

            st.info("No matched skills.")

    with col2:

        st.subheader("❌ Missing Skills")

        if selected_candidate["missing_skills"]:

            for skill in selected_candidate["missing_skills"]:

                st.error(skill)

        else:

            st.success("No missing skills.")

    st.divider()

    # ============================================================
    # AI EXPLANATION
    # ============================================================

    st.subheader("🧠 AI Explanation")

    st.info(
        selected_candidate["reason"]
    )

    st.divider()

    # ============================================================
    # DOWNLOAD CSV
    # ============================================================

    submission = []

    for rank, candidate in enumerate(
        ranking,
        start=1
    ):

        submission.append({

            "rank": rank,

            "candidate_id": candidate["candidate_id"],

            "candidate_name": candidate["name"],

            "final_score": candidate["final_score"]

        })

    csv = pd.DataFrame(
        submission
    ).to_csv(index=False)

    st.download_button(

        "⬇ Download Ranked Candidates",

        csv,

        file_name="candidate_ranking.csv",

        mime="text/csv"

    )
    

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🤖 AI Candidate Ranking")
st.sidebar.success("AI Engine Ready")
st.sidebar.markdown("---")
st.sidebar.write("### Features")
st.sidebar.write("✅ Semantic Ranking")
st.sidebar.write("✅ Skill Matching")
st.sidebar.write("✅ Experience Analysis")
st.sidebar.write("✅ Behavior Analysis")
st.sidebar.write("✅ Intent Detection")
st.sidebar.write("✅ Explainable AI")
st.sidebar.write("✅ JSON / JSONL Upload")
st.sidebar.write("✅ Large Dataset Support")
st.sidebar.write("✅ CSV Export")

st.sidebar.markdown("---")
st.sidebar.write("### Developed By")
st.sidebar.info("""Raghav Sharma

Puneet Singh

Saksham

Prakash Kumar""")
