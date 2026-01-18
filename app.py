from flask import Flask, render_template, request
import csv
from datetime import datetime
import pandas as pd
from transformers import pipeline
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer
from flask import jsonify

app = Flask(__name__)

model_id = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = ORTModelForSequenceClassification.from_pretrained(model_id)

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model=model,
    tokenizer=tokenizer
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    feedback = request.form["feedback"]
    result = sentiment_pipeline(feedback)[0]
    label = "Positive" if result["label"] == "POSITIVE" else "Negative"
    # 🔹 Save to CSV log
    with open("feedback_log.csv", "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([feedback, result, datetime.now()])
    return render_template("index.html", prediction=result)

@app.route("/api/predict", methods=["POST"])
def api_predict():
    text = request.json["feedback"]
    result = sentiment_pipeline(text)[0]
    label = "Positive" if result["label"] == "POSITIVE" else "Negative"
    return jsonify({"sentiment": label})

# 🔷 DASHBOARD ROUTE
@app.route("/dashboard")
def dashboard():
    df = pd.read_csv("feedback_log.csv")

    total = len(df)
    counts = df["Predicted_Sentiment"].value_counts()

    positive = counts.get("Positive",0)
    negative = counts.get("Negative",0)

    pos_percent = round((positive/total)*100,2) if total>0 else 0
    neg_percent = round((negative/total)*100,2) if total>0 else 0

    recent = df.tail(5).iloc[::-1]

    return render_template("dashboard.html",
                           total=total,
                           pos_percent=pos_percent,
                           neg_percent=neg_percent,
                           recent=recent.values)

if __name__ == "__main__":
    app.run(debug=True)
