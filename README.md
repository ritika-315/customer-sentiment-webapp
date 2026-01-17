# 🧠 Customer Feedback Sentiment Analyzer & Dashboard

An web application that analyzes customer feedback and predicts sentiment (Positive/Negative) using Machine Learning & NLP.  
The system also logs user feedback and provides a dashboard with analytics.

---

## 🚀 Features

✔ Sentiment Prediction using Logistic Regression  
✔ NLP Text Cleaning & Preprocessing  
✔ Live Web Interface (Flask)  
✔ Feedback Logging System  
✔ Analytics Dashboard  
✔ Sentiment Percentage Tracking    
✔ Ready for Public Deployment  

---

## Screenshots
<img width="1914" height="873" alt="image" src="https://github.com/user-attachments/assets/f068cfb4-c54b-4d37-a84f-cedb84471d75" />
<img width="1919" height="868" alt="image" src="https://github.com/user-attachments/assets/ad981f14-4836-4736-95a3-8182c2f078b8" />

---

## 🛠 Tech Stack

- Python  
- Flask  
- Scikit-learn  
- Pandas  
- NLTK  
- Matplotlib  
- HTML & CSS  

---

## 📂 Dataset Used
Dataset Link: https://www.kaggle.com/datasets/vishweshsalodkar/customer-feedback-dataset

Customer Feedback Dataset from Kaggle containing:
- Feedback Text  
- Sentiment Labels  
- Source, Date, User ID, Location  
- Confidence Score  

---

## 📊 How it Works

1. Dataset is cleaned & structured  
2. NLP preprocessing removes noise while keeping negations  
3. ML model is trained on labeled feedback  
4. Flask backend loads trained model  
5. User submits feedback via website  
6. Sentiment is predicted & stored  
7. Dashboard shows analytics  

---

## 💻 Run Locally

bash

pip install -r requirements.txt

python app.py

Open in browser: http://127.0.0.1:5000

Dashboard: http://127.0.0.1:5000/dashboard

---

## 🌍 Live Deployment

This project is publicly deployed on Render and accessible to everyone:

🔗 **Live Web App:**  
https://customer-sentiment-webapp.onrender.com/

Users can submit feedback and view real-time sentiment predictions along with dashboard analytics.

---

## 📌 Real-World Use Case

This system can be used by companies and organizations to:

- Monitor customer satisfaction automatically  
- Detect and analyze major complaints  
- Track sentiment trends for products and services  
- Understand customer experience using NLP insights  
- Support business decisions based on feedback analytics  
- Improve service quality and product reliability  

It simulates how businesses leverage AI to process large volumes of customer feedback efficiently.
