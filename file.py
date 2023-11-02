import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

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

# Evaluate the model on the test set
y_pred = clf.predict(X_test)
accuracy = np.mean(y_pred == y_test)
print("Accuracy:", accuracy)

# Deploy the model
# ...