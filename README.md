# Social Media Content Analyzer

## Project Overview
The Social Media Content Analyzer is a web application built using Streamlit that helps analyze social media content in a simple and interactive way. The goal of this project was to create a working application that can process uploaded text or images and generate meaningful insights from the content.

## Features
- Upload text files or images
- Extract text from PDFs and images
- Analyze content based on word usage, hashtags, sentiment, and engagement factors
- Display results in a clean and user-friendly interface

## Technologies Used
- Python
- Streamlit
- PyPDF2
- PyTesseract (OCR)
- TextBlob (Sentiment Analysis)
- Matplotlib
- GitHub for version control and deployment

## Live Application
https://social-media-content-analyzer-ebtezbpfawbgej8bqzuzhd.streamlit.app/

## Brief Write-up 

This project was developed as part of a technical assessment to demonstrate practical problem-solving and full-stack application development using Python. The main idea was to build a tool that can analyze social media content and provide useful feedback to improve engagement.

The application allows users to upload PDF files or images. For PDFs, text is extracted using PyPDF2, and for images, OCR is performed using Tesseract to retrieve readable text. Once the text is extracted, it is analyzed based on word count, hashtag usage, sentiment, and the presence of call-to-action phrases. A simple rule-based scoring system generates an engagement score between 0 and 100.

Streamlit was used to design both the frontend and backend because it enables quick development and deployment of data-driven applications. The project structure was organized clearly to ensure smooth deployment on Streamlit Community Cloud.

Overall, this project demonstrates integration of file handling, text processing, sentiment analysis, and web deployment into a complete working solution.
