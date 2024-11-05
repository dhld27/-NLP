# streamlit
import streamlit as st
# pandas
import pandas as pd
# Visualisation
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud
# Image
from PIL import Image

def run():
    # Create Title
    st.title('Graded Challenge 7 Phase 2')
    # Create Introduction
    st.subheader('Introduction')
    # Create Preliminary 
    st.write("Daffa Darwin Batch 5 BSD Hacktiv8.")
    # Add an image from URL
    st.image('https://i.ytimg.com/vi/n9krPErdsBE/maxresdefault.jpg')
    # Create caption
    st.caption("source: Genshin Impact Google Play(https://play.google.com/store/apps/details?id=com.miHoYo.GenshinImpact&hl=en_US&pli=1)")

    # Description
    st.write('## Objective')
    st.write('''
            to predict the sentiment based on the review of Genshin Impact in Google Play if there are a new user that play the game, then leave a review. 
             This task will predict whether the last review are into three sentiment: Positive, Neutral, or Negative. 
             Then, for the continuous improvement to the company since the dataset is considered as a real-time review 
             and it can be an aspiration for the company that create Genshin Impact, "Hoyoverse" to improve their product to gain more profit.
    ''')
    st.write('## Problem Statement')
    st.write('''
        Genshin Impact is an open-world game developed by Hoyoverse, where the game obtain so much feedback
             from the customers (in this case the customer considered as a Genshin Impact player) variative from positive feedback,
             neutral feedback, and negative feedback. the the user wants to create this app to predict whether there are a new
             feedback, it can predict which feedback that will be affect the company, if it is positive feedback, the company can 
             gain more profit from the product ("Genshin impact"), if the feedback neutral, the company can ignore it.
             but when the feedback is negative, the company can considered it as their improvement for better business  
    ''')

    st.divider()
    # Display the DataFrame
    st.write('## Data')
    df = pd.read_csv('genshin_review.csv')
    st.dataframe(df)
    st.write('Dataset Description')
    st.write('''
        The dataset obtained from Kaggle for fulfill the
        requirements of Graded Challenge 7 Phase 2
    ''')

    st.divider()
    # Visualisation
    st.write('## Exploratory Data Analysis')

    # Combine all the text in the 'review' column into a single string
    text = " ".join(df['review'].astype(str))

    # Generate the word cloud
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="black").generate(text)

    # Streamlit app
    st.title("Word Cloud from Reviews")

    # Display the word cloud
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)

if __name__ == '__main__':
    run()
