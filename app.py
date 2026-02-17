# ----------------------------------------
# Social Media Content Analyzer
# Premium Dark Version
# ----------------------------------------

import streamlit as st
import pytesseract
from PIL import Image
import PyPDF2
from textblob import TextBlob
import re

# ----------------------------------------
# Page Configuration
# ----------------------------------------

st.set_page_config(
    page_title="Social Media Analyzer",
    page_icon="📊",
    layout="wide"
)

# ----------------------------------------
# Custom Dark Styling
# ----------------------------------------

st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

h1, h2, h3 {
    color: #FFFFFF;
}

.stMetric {
    background-color: #1C1F26;
    padding: 15px;
    border-radius: 12px;
}

.stProgress > div > div > div > div {
    background-color: #00F5D4;
}

.stButton button {
    border-radius: 10px;
    background-color: #00F5D4;
    color: black;
    font-weight: bold;
}

.stDownloadButton button {
    border-radius: 10px;
    background-color: #00F5D4;
    color: black;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------
# Tesseract Path (EDIT if different)
# ----------------------------------------

pytesseract.pytesseract.tesseract_cmd = r"D:\navreet\tesseract.exe"

# ----------------------------------------
# Sidebar
# ----------------------------------------

st.sidebar.title("⚙️ Navigation")
st.sidebar.info("Upload your social media content to analyze engagement.")

st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.write(
    "AI-powered tool that analyzes posts and provides engagement insights."
)

# ----------------------------------------
# Header
# ----------------------------------------

st.title("📊 Social Media Content Analyzer")
st.markdown("### Turn your content into high-engagement posts 🚀")
st.markdown("---")

uploaded_file = st.file_uploader(
    "Upload PDF or Image",
    type=["pdf", "jpg", "png", "jpeg"]
)

# ----------------------------------------
# Functions
# ----------------------------------------

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


def analyze_content(text):
    word_count = len(text.split())
    hashtags = re.findall(r"#\w+", text)
    hashtag_count = len(hashtags)
    sentiment = TextBlob(text).sentiment.polarity

    engagement_score = 50

    if 50 <= word_count <= 150:
        engagement_score += 15
    if hashtag_count >= 3:
        engagement_score += 15
    if sentiment > 0:
        engagement_score += 10

    engagement_score = min(engagement_score, 100)

    if engagement_score >= 80:
        rating = "🔥 Excellent"
    elif engagement_score >= 60:
        rating = "👍 Good"
    else:
        rating = "⚠ Needs Improvement"

    suggestions = []

    if word_count > 200:
        suggestions.append("Reduce content length for better engagement.")
    if hashtag_count < 3:
        suggestions.append("Add at least 3 relevant hashtags.")
    if not any(cta in text.lower() for cta in ["call now", "buy now", "learn more"]):
        suggestions.append("Add a strong Call-To-Action (CTA).")
    if sentiment < 0:
        suggestions.append("Use a more positive tone.")

    return word_count, hashtag_count, sentiment, engagement_score, rating, suggestions


# ----------------------------------------
# Main App Logic
# ----------------------------------------

if uploaded_file is not None:

    with st.spinner("🔍 Analyzing your content..."):

        try:
            if uploaded_file.type == "application/pdf":
                text = extract_text_from_pdf(uploaded_file)
            else:
                image = Image.open(uploaded_file)
                st.image(image, width="stretch")
                text = pytesseract.image_to_string(image)

            if not text.strip():
                st.error("No readable text detected.")
            else:

                st.markdown("## 📝 Extracted Content")
                st.write(text)

                word_count, hashtag_count, sentiment, engagement_score, rating, suggestions = analyze_content(text)

                st.markdown("---")
                st.markdown("## 📊 Performance Dashboard")

                col1, col2, col3 = st.columns(3)

                col1.metric("Word Count", word_count)
                col2.metric("Hashtags", hashtag_count)
                col3.metric("Sentiment Score", round(sentiment, 2))

                st.markdown("### Engagement Score")
                st.progress(engagement_score / 100)
                st.markdown(f"## {engagement_score}/100 — {rating}")

                st.markdown("---")
                st.markdown("## 💡 Optimization Suggestions")

                if suggestions:
                    for suggestion in suggestions:
                        st.warning(suggestion)
                else:
                    st.success("Your content is highly optimized for engagement!")

                report = f"""
SOCIAL MEDIA CONTENT REPORT

Word Count: {word_count}
Hashtags: {hashtag_count}
Sentiment Score: {round(sentiment, 2)}
Engagement Score: {engagement_score}/100
Rating: {rating}

Suggestions:
{chr(10).join(suggestions) if suggestions else "No major improvements needed."}
"""

                st.download_button(
                    label="📥 Download Analysis Report",
                    data=report,
                    file_name="content_analysis_report.txt",
                    mime="text/plain"
                )

        except Exception as e:
            st.error(f"An error occurred: {e}")
