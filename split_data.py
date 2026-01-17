import pandas as pd

rows = []

with open("customer_feedback.csv", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(", ")

        if len(parts) == 7:
            rows.append(parts)

df = pd.DataFrame(rows, columns=[
    "Text","Sentiment","Source","DateTime","UserID","Location","Confidence"
])

df.to_csv("cleaned_feedback.csv", index=False)

print("Dataset cleaned and structured successfully!")
