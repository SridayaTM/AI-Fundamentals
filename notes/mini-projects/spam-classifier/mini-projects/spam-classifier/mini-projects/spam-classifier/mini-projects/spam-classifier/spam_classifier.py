import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("dataset.csv")

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['text'])

# Labels
y = data['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Test prediction
sample = ["Free entry in a contest"]
sample_vector = vectorizer.transform(sample)
prediction = model.predict(sample_vector)

print("Prediction:", prediction[0])
