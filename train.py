import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from preprocess import clean_text

df = pd.read_csv("cleaned_feedback.csv")

df["Text"] = df["Text"].astype(str).apply(clean_text)

X = df["Text"]
y = df["Sentiment"]

vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=5000)
X_vect = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vect, y)

pickle.dump(model, open("model.pkl","wb"))
pickle.dump(vectorizer, open("vectorizer.pkl","wb"))

print("Model trained and saved successfully!")
