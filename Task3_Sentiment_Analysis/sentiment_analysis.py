import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# ---------------------------------------
# 1. Load Dataset
# ---------------------------------------

data = pd.read_csv("reviews.csv")

print("Dataset loaded successfully!")
print("\nDataset:")
print(data)


# ---------------------------------------
# 2. Prepare the Data
# ---------------------------------------

X = data["Review"]
y = data["Sentiment"]


# ---------------------------------------
# 3. Split Dataset
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ---------------------------------------
# 4. Convert Text to TF-IDF Features
# ---------------------------------------

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


# ---------------------------------------
# 5. Train the Classifier
# ---------------------------------------

model = LogisticRegression()

model.fit(X_train_tfidf, y_train)


# ---------------------------------------
# 6. Evaluate the Model
# ---------------------------------------

y_pred = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)

print("\n===================================")
print("       MODEL EVALUATION")
print("===================================")

print(f"\nAccuracy: {accuracy:.2f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# ---------------------------------------
# 7. Interactive Sentiment Prediction
# ---------------------------------------

print("\n===================================")
print("      SENTIMENT ANALYSIS TOOL")
print("===================================")

print("Type 'exit' to stop.")

while True:

    user_input = input("\nEnter a review: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    user_tfidf = vectorizer.transform([user_input])

    prediction = model.predict(user_tfidf)[0]

    print("Predicted Sentiment:", prediction.upper())