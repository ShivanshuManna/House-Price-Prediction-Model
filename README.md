🏠 House Price Prediction Web App
Machine Learning Model using Linear Regression & Flask
📌 Project Overview

This project is a House Price Prediction Web Application built using Machine Learning (Linear Regression) and deployed with Flask.

The application allows users to enter house features (such as area, number of bedrooms, etc.) and get an instant predicted house price through a simple web interface.

🧠 Machine Learning Model

Algorithm Used: Linear Regression

Built using Scikit-learn

Trained on historical housing dataset

Model saved using Joblib for deployment

📊 Evaluation Metrics

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

R² Score

🛠️ Technologies & Libraries Used

Python

Flask

NumPy

Pandas

Matplotlib

Seaborn

Scikit-learn

Joblib

📊 Project Workflow

Data Collection

Data Cleaning & Preprocessing

Exploratory Data Analysis (EDA)

Feature Selection

Model Training using Linear Regression

Model Evaluation

Model Saving using Joblib

Deployment using Flask

📂 Project Structure
House-Price-Prediction/
│
├── app.py
├── model.pkl
├── templates/
│   └── index.html
├── static/
├── dataset.csv
├── requirements.txt
└── README.md
▶️ How to Run the Project
1. Clone the Repository

git clone https://github.com/your-username/house-price-prediction.git

cd house-price-prediction

2. Install Dependencies

pip install -r requirements.txt

Or manually install:

pip install flask numpy pandas matplotlib seaborn scikit-learn joblib

3. Run the Application

python app.py

4. Open in Browser

http://127.0.0.1:5000/

🌐 Web Application Features

User-friendly input form

Real-time house price prediction

Backend ML integration with Flask

Lightweight and easy to deploy

📈 Future Improvements

Compare with other regression models

Improve UI/UX design

Deploy on cloud platforms (AWS / Render / Heroku)

Add input validation and error handling

🎯 Learning Outcomes

Implementation of Linear Regression

Model evaluation techniques

Model saving and loading using Joblib

Flask integration with ML models

End-to-end ML project development

📜 License

This project is open-source and available under the MIT License.
