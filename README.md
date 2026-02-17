Social Media AI Suite

This project was built as part of a Software Engineering technical assessment. The objective was to create a working application that can extract text from PDFs or images and analyze social media content to suggest engagement improvements.

The application allows users to upload PDF files or scanned images. For PDFs, text is extracted using PyPDF2. For images, OCR is performed using Tesseract to retrieve readable text. Once the content is extracted, it is analyzed based on word count, hashtag usage, sentiment, and the presence of call-to-action phrases.

An engagement score (0–100) is generated using a simple rule-based scoring logic. The goal of the scoring system is to simulate how content quality and structure impact visibility and engagement on social media platforms.

The project also includes a caption optimization feature. Based on detected context (achievement, growth, announcement, etc.), the system rewrites the caption by adding structured hooks, CTAs, and relevant hashtags.

The application is built using Streamlit for both frontend and backend. TextBlob is used for sentiment analysis, Matplotlib for visualizations, Pillow for image handling, and PyTesseract for OCR.

The focus of this project was:

Clean and readable code structure

Modular function design

Basic error handling

Loading states for better user experience

Delivering a working solution within an 8-hour constraint

This project demonstrates practical problem-solving, working with real-world file inputs, integrating third-party libraries, and building an end-to-end functional application.

Built by Navreet 
