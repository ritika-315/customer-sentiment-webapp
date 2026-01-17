import nltk
import string
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

# REMOVE negation words from stopwords so they stay
negation_words = {"not", "no", "never", "n't"}
stop_words = stop_words - negation_words

def clean_text(text):
    text = text.lower()
    text = "".join([c for c in text if c not in string.punctuation])
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)
