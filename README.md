# IBM Telco Customer Churn Prediction

## 📌 Project Overview

This is an end-to-end Customer Churn Analytics and Prediction project based on the IBM Telco Customer Churn dataset.

The project analyzes customer behavior and predicts whether a customer is likely to churn or stay using Machine Learning.

The project includes data analysis, SQL analysis, Power BI dashboarding, Machine Learning, and Streamlit deployment.

---

## 🎯 Business Objective

The main objective of this project is to identify customers who are at risk of leaving the telecom company.

By predicting customer churn, businesses can:

- Identify high-risk customers
- Understand factors affecting customer churn
- Take proactive customer retention actions
- Improve customer satisfaction
- Reduce customer loss

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SQL
- Excel
- Power BI
- Streamlit
- Joblib

---

## 📊 Data Analysis

The dataset was analyzed using Python, Excel, SQL, and Power BI.

The analysis focused on:

- Customer demographics
- Tenure
- Contract type
- Internet service
- Payment method
- Monthly charges
- Total charges
- Customer churn

---

## 🤖 Machine Learning

A Machine Learning classification model was trained to predict customer churn.

The trained Machine Learning pipeline is saved using Joblib.

Model file:

`customer_churn_pipeline.pkl`

The model predicts:

- `0` → Customer is likely to Stay
- `1` → Customer is likely to Churn

The Streamlit application also displays the estimated churn probability.

---

## 🚀 Streamlit Application

A Streamlit web application was developed to make the Machine Learning model interactive.

Users can enter customer information such as:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

The application provides:

- Churn Prediction
- Churn Probability
- Risk Level

Risk levels are categorized as:

- Low Risk 🟢
- Medium Risk 🟡
- High Risk 🔴

---

## 📁 Project Structure

```text
IBM_TELCO_CHURN/
│
├── app.py
├── customer_churn_pipeline.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Application

### Step 1: Install Required Libraries

Open the terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

### Step 2: Run the Streamlit Application

Run the following command:

```bash
streamlit run app.py
```

### Step 3: Open the Application

After running the command, open the Streamlit application in your web browser.

---

## 💡 Business Insights

The analysis provided the following key insights:

- Customers with month-to-month contracts have a higher risk of churn.
- Customers with long-term contracts generally show better customer retention.
- Customers with higher monthly charges may have a higher risk of churn.
- Customers with shorter tenure may have a higher likelihood of leaving.
- Payment method and service-related factors can also influence customer churn.

---

## 📈 Business Impact

The churn prediction model can help telecom companies identify customers who may be at risk of leaving.

The company can use these predictions to:

- Offer personalized retention plans
- Provide discounts or special offers
- Improve customer support
- Encourage long-term contracts
- Develop targeted customer engagement strategies

---

## 👩‍💻 Author

Mounika Kasturi