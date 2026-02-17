# ----------------------------------------
# Social Media AI Suite - FINAL Portfolio Version
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
# SESSION STATE
# ----------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ----------------------------------------
# LOGIN PAGE
# ----------------------------------------

def login_page():
    st.markdown("<h1 style='text-align:center;'>🔐 Login</h1>", unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login Successful!")
            st.rerun()
        else:
            st.error("Invalid Credentials")

# ----------------------------------------
# LANDING PAGE
# ----------------------------------------

def landing_page():
    st.markdown("""
    <div style='text-align:center; padding:80px 0;'>
        <h1 style='font-size:55px;'>🚀 Social Media AI Suite</h1>
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
# CONTEXT-AWARE HASHTAG GENERATOR
# ----------------------------------------

def generate_context_hashtags(text):
    text_lower = text.lower()

    hashtag_map = {
        "course": "#LearningJourney",
        "certificate": "#Certification",
        "completed": "#AchievementUnlocked",
        "microsoft": "#Microsoft",
        "sap": "#SAP",
        "aicte": "#AICTE",
        "technology": "#IR4.0",
        "ir4.0": "#Industry40",
        "digital": "#DigitalTransformation",
        "foundation": "#SkillDevelopment",
        "program": "#TechSaksham",
        "mentor": "#Grateful",
        "institute": "#HigherEducation"
    }

    detected_hashtags = []

    for keyword, hashtag in hashtag_map.items():
        if keyword in text_lower:
            detected_hashtags.append(hashtag)

    default_tags = [
        "#CareerGrowth",
        "#ProfessionalDevelopment",
        "#FutureReady",
        "#LinkedInLearning"
    ]

    while len(detected_hashtags) < 4:
        tag = random.choice(default_tags)
        if tag not in detected_hashtags:
            detected_hashtags.append(tag)

    return " ".join(detected_hashtags[:5])

# ----------------------------------------
# SMART CONTEXT-AWARE REWRITER
# ----------------------------------------

def rewrite_caption(text):
    text = text.strip()
    lower_text = text.lower()

    achievement_hooks = [
        "🎉 Proud to share this milestone!",
        "🌟 Another step forward!",
        "🚀 Excited to announce this achievement!",
        "🏆 Grateful for this accomplishment!",
        "✨ Celebrating progress and growth!"
    ]

    growth_hooks = [
        "🔥 Stop scrolling!",
        "🚀 Want to grow faster?",
        "📈 Ready to level up?",
        "💡 Here's something powerful:",
        "✨ This changes everything:"
    ]

    ctas = [
        "👉 Follow for more updates!",
        "💬 Would love to hear your thoughts!",
        "❤️ Appreciate your support!",
        "🔔 Stay tuned for more insights!"
    ]

    # Detect context
    if any(word in lower_text for word in 
           ["completed", "certificate", "grateful", "excited", "achievement", "course"]):
        hook = random.choice(achievement_hooks)
    else:
        hook = random.choice(growth_hooks)

    cta = random.choice(ctas)

    hashtags = generate_context_hashtags(text)

    improved_caption = f"""
{hook}

{text}

{cta}

{hashtags}
"""

    return improved_caption

# ----------------------------------------
# DASHBOARD
# ----------------------------------------

def dashboard():

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Analyzer", "AI Rewriter", "Logout"])

    if page == "Logout":
        st.session_state.logged_in = False
        st.rerun()

    # ---------------- ANALYZER ----------------

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
                    st.image(image, width="stretch")
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

                    # Chart
                    st.subheader("📈 Analytics Overview")

                    labels = ["Words", "Hashtags", "Sentiment x100"]
                    values = [wc, hc, sent * 100]

                    fig, ax = plt.subplots()
                    ax.bar(labels, values)
                    st.pyplot(fig)

                else:
                    st.warning("No readable text found.")

    # ---------------- AI REWRITER ----------------

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
