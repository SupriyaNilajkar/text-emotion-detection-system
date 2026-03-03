import streamlit as st
from transformers import pipeline
import pandas as pd

# ---------------- Page Config ---------------- #
st.set_page_config(
    page_title="Emotion Detection System",
    page_icon="🎭",
    layout="centered"
)

# ---------------- Title ---------------- #
st.title("🎭 Emotion Detection System")
st.write("Detect human emotions from text using a pretrained Transformer model.")

# ---------------- Load Model (Cached) ---------------- #
@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        return_all_scores=True
    )

classifier = load_model()

# ---------------- Emotion Emojis ---------------- #
emotion_emojis = {
    "joy": "😊",
    "sadness": "😢",
    "anger": "😡",
    "fear": "😨",
    "surprise": "😲",
    "disgust": "🤢",
    "neutral": "😐"
}

# ---------------- User Input ---------------- #
user_input = st.text_area("Enter your text here:")

# ---------------- Detect Emotion ---------------- #
if st.button("Detect Emotion"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        results = classifier(user_input)

        # Handle different output formats safely
        if isinstance(results, list):
            if isinstance(results[0], list):
                emotion_scores = results[0]
            else:
                emotion_scores = results
        else:
            emotion_scores = [results]

        # Convert to DataFrame
        df = pd.DataFrame(emotion_scores)
        df = df.sort_values(by="score", ascending=False)

        # Get Top Emotion
        top_emotion = df.iloc[0]
        emotion_label = top_emotion["label"]
        emoji = emotion_emojis.get(emotion_label, "🙂")

        # Display Result
        st.markdown(f"## 🎯 Predicted Emotion: {emotion_label} {emoji}")

        # Show Confidence Scores
        st.subheader("📊 Emotion Confidence Scores")
        st.bar_chart(df.set_index("label")["score"])