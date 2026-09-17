# Task 3 - Sentiment Analysis Tool

## Overview

This project is a machine learning-based sentiment analysis tool developed as part of the InfozaTech Artificial Intelligence Internship.

The application analyzes text reviews and predicts whether the sentiment is **positive** or **negative**.

## Objectives

The main objectives of this project are:

* Prepare a labeled text dataset.
* Preprocess text data.
* Convert text into numerical features using TF-IDF.
* Train a machine learning classifier.
* Evaluate the trained model.
* Allow users to enter text and receive a sentiment prediction.

## Dataset

The project uses a labeled review dataset containing two sentiment classes:

* Positive
* Negative

The dataset is stored in:

```text
reviews.csv
```

Each record contains:

| Column    | Description                |
| --------- | -------------------------- |
| Review    | Text entered as a review   |
| Sentiment | Positive or negative label |

## Technologies Used

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorization
* Logistic Regression

## Methodology

### 1. Data Loading

The dataset is loaded using Pandas.

```python
data = pd.read_csv("reviews.csv")
```

### 2. Train-Test Split

The dataset is divided into training and testing sets.

The model is trained using the training data and evaluated using unseen test data.

### 3. TF-IDF Feature Extraction

TF-IDF (Term Frequency-Inverse Document Frequency) is used to convert text into numerical features that can be processed by the machine learning model.

```python
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)
```

### 4. Model Training

A Logistic Regression classifier is trained using the TF-IDF features.

```python
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)
```

### 5. Model Evaluation

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

### 6. Sentiment Prediction

The application allows users to enter their own text.

Example:

```text
Enter a review: I really enjoyed this product!

Predicted Sentiment: POSITIVE
```

Another example:

```text
Enter a review: This product was terrible.

Predicted Sentiment: NEGATIVE
```

## How to Run

### 1. Install Python

Make sure Python 3 is installed.

### 2. Install dependencies

Run:

```bash
pip install -r requirements.txt
```

### 3. Run the application

Run:

```bash
python sentiment_analysis.py
```

### 4. Enter a review

Type a review when prompted.

Type:

```text
exit
```

to close the application.

## Project Structure

```text
Task3_Sentiment_Analysis/
│
├── sentiment_analysis.py
├── reviews.csv
├── requirements.txt
└── README.md
```

## Limitations

This project uses a relatively small dataset, so its performance may not represent performance on large real-world datasets.

The model may also struggle with:

* Sarcasm
* Slang
* Mixed sentiments
* Negation
* Unusual wording
* Context-dependent statements

For example, a sarcastic statement may contain positive words while actually expressing a negative opinion.

## Future Improvements

Possible improvements include:

* Using a larger real-world dataset.
* Adding more sentiment categories such as neutral.
* Using word embeddings.
* Experimenting with advanced models.
* Adding a graphical or web-based interface.
* Improving text preprocessing.
