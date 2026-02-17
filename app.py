# ----------------------------------------
# Social Media AI Suite - DARK AI VERSION
# ----------------------------------------

import streamlit as st
import pytesseract
from PIL import Image
import PyPDF2
from textblob import TextBlob
import re
import matplotlib.pyplot as plt
import random

# ----------------------------------------
# PAGE CONFIG
# ----------------------------------------

st.set_page_config(
    page_title="Social Media AI Suite",
    page_icon="🚀",
    layout="wide"
)

# ----------------------------------------
# DARK THEME CUSTOM STYLE
# ----------------------------------------

st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #0E1117;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #161B22;
}

/* Buttons */
div.stButton > button {
    background-color: #6C63FF;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
}

div.stButton > button:hover {
    background-color: #5a54e6;
}

/* Text Input */
input, textarea {
    background-color: #161B22 !important;
    color: white !important;
    border-radius: 8px !important;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background-color: #161B22;
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------
# SESSION STATE
# ----------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ----------------------------------------
# LANDING PAGE
# ----------------------------------------

def landing_page():
    st.markdown("""
    <div style='text-align:center; padding:100px 0;'>
        <h1 style='font-size:60px;'>🚀 Social Media AI Suite</h1>
        <p style='font-size:22px; color:gray;'>
        Analyze • Optimize • Rewrite • Grow
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Enter Dashboard"):
        st.session_state.logged_in = True
        st.rerun()

# ----------------------------------------
# PDF TEXT EXTRACTION
# ----------------------------------------

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

# ----------------------------------------
# ENGAGEMENT ANALYSIS
# ----------------------------------------

def analyze_content(text):
    word_count = len(text.split())
    hashtags = re.findall(r"#\w+", text)
    hashtag_count = len(hashtags)
    sentiment = TextBlob(text).sentiment.polarity

    score = 40

    if 50 <= word_count <= 150:
        score += 20
    elif word_count > 200:
        score -= 10

    if hashtag_count >= 3:
        score += 15

    if sentiment > 0:
        score += 10

    if any(cta in text.lower() for cta in ["follow", "comment", "share", "like"]):
        score += 15

    score = max(0, min(score, 100))

    return word_count, hashtag_count, sentiment, score

# ----------------------------------------
# HASHTAG GENERATOR
# ----------------------------------------

def generate_context_hashtags(text):
    text_lower = text.lower()

    hashtag_map = {
        "course": "#LearningJourney",
        "certificate": "#Certification",
        "completed": "#AchievementUnlocked",
        "microsoft": "#Microsoft",
        "sap": "#SAP",
        "technology": "#IR4.0",
        "digital": "#DigitalTransformation",
    }

    detected = []

    for keyword, hashtag in hashtag_map.items():
        if keyword in text_lower:
            detected.append(hashtag)

    defaults = ["#CareerGrowth", "#FutureReady", "#LinkedInLearning"]

    while len(detected) < 4:
        tag = random.choice(defaults)
        if tag not in detected:
            detected.append(tag)

    return " ".join(detected[:5])

# ----------------------------------------
# REWRITER
# ----------------------------------------

def rewrite_caption(text):

    hooks = [
        "🚀 Big update!",
        "🌟 Excited to share!",
        "🔥 Something powerful:",
        "✨ Proud moment!"
    ]

    ctas = [
        "👉 Follow for more!",
        "💬 Drop your thoughts below!",
        "❤️ Appreciate your support!"
    ]

    hook = random.choice(hooks)
    cta = random.choice(ctas)
    hashtags = generate_context_hashtags(text)

    return f"""
{hook}

{text}

{cta}

{hashtags}
"""

# ----------------------------------------
# DASHBOARD
# ----------------------------------------

def dashboard():

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Analyzer", "AI Rewriter", "Logout"])

    if page == "Logout":
        st.session_state.logged_in = False
        st.rerun()

    if page == "Analyzer":

        st.title("📊 Content Analyzer")

        uploaded_file = st.file_uploader(
            "Upload PDF or Image",
            type=["pdf", "jpg", "png", "jpeg"]
        )

        if uploaded_file:

            with st.spinner("Analyzing..."):

                if uploaded_file.type == "application/pdf":
                    text = extract_text_from_pdf(uploaded_file)
                else:
                    image = Image.open(uploaded_file)
                    st.image(image, use_column_width=True)
                    text = pytesseract.image_to_string(image)

                if text.strip():

                    st.subheader("📝 Extracted Text")
                    st.write(text)

                    wc, hc, sent, score = analyze_content(text)

                    st.markdown("---")
                    st.subheader("📊 Performance Metrics")

                    col1, col2, col3 = st.columns(3)
                    col1.metric("Words", wc)
                    col2.metric("Hashtags", hc)
                    col3.metric("Sentiment", round(sent, 2))

                    st.progress(score / 100)
                    st.markdown(f"### 🔥 Engagement Score: {score}/100")

                    st.subheader("📈 Analytics Overview")

                    labels = ["Words", "Hashtags", "Sentiment x100"]
                    values = [wc, hc, sent * 100]

                    fig, ax = plt.subplots()
                    ax.bar(labels, values)
                    ax.set_facecolor("#0E1117")
                    fig.patch.set_facecolor("#0E1117")
                    ax.tick_params(colors='white')
                    st.pyplot(fig)

                else:
                    st.warning("No readable text found.")

    if page == "AI Rewriter":

        st.title("🤖 AI Caption Optimizer")

        user_text = st.text_area("Enter your caption")

        if st.button("Optimize Caption"):

            if user_text.strip():

                improved = rewrite_caption(user_text)

                st.subheader("✨ Optimized Version")
                st.success(improved)

            else:
                st.warning("Please enter some text.")

# ----------------------------------------
# MAIN FLOW
# ----------------------------------------

if not st.session_state.logged_in:
    landing_page()
else:
    dashboard()

# ----------------------------------------
# FOOTER
# ----------------------------------------

st.markdown("---")
st.markdown(
    "<center style='color: gray;'>Built by Navreet | 2026 | AI SaaS Portfolio Project</center>",
    unsafe_allow_html=True
)
