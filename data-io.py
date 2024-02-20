import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import streamlit as st

# Load the fake and real news dataset
df = pd.read_csv("news.csv")

# Preprocess the data
X = df["text"]
y = df["label"]

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.25, random_state=42)

# Train a logistic regression model
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Define the Streamlit app
def main():
    st.title("Fake News Detector")

    # User input for news text
    user_input = st.text_area("Enter the news text to check if it's fake or real:")

    if st.button("Check"):
        # Preprocess the user input
        user_input_vec = vectorizer.transform([user_input])

        # Predict the label
        prediction = clf.predict(user_input_vec)[0]

        # Display the prediction
        if prediction == 1:
            st.error("Fake News")
        else:
            st.success("Real News")

if __name__ == "__main__":
    main()
