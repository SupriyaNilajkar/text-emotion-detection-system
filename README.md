# 🎭 Emotion Detection System

Final Year Computer Science Engineering Project

A web-based Emotion Detection application built using **Streamlit** and a pretrained **Transformer (DistilRoBERTa) model** from HuggingFace.  
The system analyzes user-input text and predicts the underlying human emotion along with confidence scores.


## 🚀 Project Overview

This project demonstrates the practical implementation of **Natural Language Processing (NLP)** using a deep learning Transformer model.  
The application provides real-time emotion classification through an interactive web interface.


## 🧠 Model Used

- Model: j-hartmann/emotion-english-distilroberta-base
- Framework: HuggingFace Transformers
- Task: Text Classification

### Supported Emotions:
- Joy 😊  
- Sadness 😢  
- Anger 😡  
- Fear 😨  
- Surprise 😲  
- Disgust 🤢  
- Neutral 😐  


## 🛠️ Technologies Used

- Python  
- Streamlit  
- HuggingFace Transformers  
- PyTorch  
- Pandas  


## ✨ Features

- Real-time emotion detection from text  
- Displays predicted emotion with emoji  
- Shows confidence scores using bar chart  
- User-friendly and interactive interface  
- Lightweight and fast performance  

---

## 📂 Project Structure
emotion_detection/
│── app.py
│── requirements.txt
│── README.md


## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/emotion-detection-streamlit.git

### 2️⃣ Navigate to Project Folder

cd emotion-detection-streamlit

### 3️⃣ Create Virtual Environment

python -m venv .venv

### 4️⃣ Activate Virtual Environment (Windows)

.venv\Scripts\activate

### 5️⃣ Install Dependencies

pip install -r requirements.txt

### 6️⃣ Run the Application

streamlit run app.py

The application will open in your browser at:
http://localhost:8501  

## 📊 Example

**Input:**
I am very happy today!

**Output:**
🎯 Predicted Emotion: Joy 😊
