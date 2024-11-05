# Library Load Model
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model

# Library Pre-Processing
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from nltk.stem import WordNetLemmatizer

# Download necessary resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Load Model
model = load_model('model')

additionalStopwords = [
    'the', 'I', 'and', 'to', 'is', 'a', 'it', 'this', 'but',
    'of', 'for', 'you', 'my', 'in', 'like', 'so', 'good', 'i', 'are',
    'have', 'not', 'that', 'on', "'s"
]
    
stopWords = list(set(stopwords.words('english')))

stopWords.extend(additionalStopwords)
lemmatizer = WordNetLemmatizer()


# Create A Function for Text Preprocessing

def text_preprocessing(text):
  # Case folding
  text = text.lower()

  # Newline removal (\n)
  text = re.sub(r"\\n", " ",text)

  # Whitespace removal
  text = text.strip()

  # Non-letter removal (such as emoticon, symbol (like μ, $, 兀), etc
  text = re.sub("[^A-Za-z\s']", " ", text)

  # Tokenization
  tokens = word_tokenize(text)

  # Stopwords removal
  tokens = [word for word in tokens if word not in stopWords]

  # Stemming
  tokens = [lemmatizer.lemmatize(word) for word in tokens]

  # Combining Tokens
  text = ' '.join(tokens)

  return text


def run():
    # membuat title
    st.title('Genshin Reviews Sentiment Prediction')
    st.subheader('Sentiment Prediction for Hoyoverse')
    st.markdown('---')
    # Buat form
    with st.form(key='genshin_review_detect'):
        st.write("## Review text")
        # URL input
        text = st.text_input("Enter the review:")
        submitted = st.form_submit_button('Predict')
        # Perform prediction
        if submitted:
                data_inf = {'text': text}
                data_inf = pd.DataFrame([data_inf])
                # Preprocess the text (apply the same preprocessing steps as used during training)
                data_inf['text'] = data_inf['text'].apply(lambda x: text_preprocessing(x))
                # Make the prediction using the loaded model
                y_pred_inf = model.predict(data_inf)
                y_pred_inf = np.argmax(y_pred_inf)

                # Display the prediction result
                if y_pred_inf == 2:
                    st.subheader("Prediction: Super Positive Review")
                    st.success("Prediction: Super Positive Review")
                    st.balloons()
                elif y_pred_inf == 1:
                    st.subheader("Prediction: Positive Review")
                    st.success("Prediction: Positive Review")
                elif y_pred_inf == 0:
                    st.subheader("Prediction: Neutral Review")
                else:
                    st.subheader("Prediction: Negative Review")
                
                # Display the extracted text
                st.subheader("Extracted Text:")
                st.write(text)

if __name__ == '__main__':
    run()