
# ============================================================
# IBM TELCO CUSTOMER CHURN PREDICTION APP
# ============================================================

# Import Libraries
import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS - PROFESSIONAL UI
# ============================================================

st.markdown(
    """
    <style>

    /* Main App Background */
    .stApp {
        background-color: grey;
    }

    /* Main Title */
    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    /* Section Header */
    .section-header {
        font-size: 25px;
        font-weight: 600;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    /* Footer */
    .footer {
        text-align: center;
        margin-top: 40px;
        padding: 20px;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD TRAINED MODEL
# ============================================================

model = joblib.load("customer_churn_pipeline.pkl")


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("📊 About This App")

    st.write(
        """
        This Machine Learning application predicts whether a
        Telco customer is likely to churn based on customer
        demographics, services, contract details and billing information.
        """
    )

    st.divider()

    st.subheader("🤖 Machine Learning Model")

    st.write("**Model:** Logistic Regression")

    st.write("**Dataset:** IBM Telco Customer Churn")

    st.write("**Application:** Customer Churn Prediction")

    st.divider()

    st.info(
        "💡 Business Goal: Identify customers at high risk of churn "
        "and support customer retention strategies."
    )


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📊 IBM Telco Customer Churn Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict customer churn risk using Machine Learning'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# CUSTOMER INFORMATION
# ============================================================

st.markdown(
    '<div class="section-header">👤 Customer Information</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter the customer's information below to predict the likelihood of churn."
)


# ============================================================
# INPUT FEATURES
# ============================================================

col1, col2 = st.columns(2)


# ============================================================
# COLUMN 1 - PERSONAL & SERVICE INFORMATION
# ============================================================

with col1:

    st.subheader("👤 Personal & Service Information")

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=100,
        value=1
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No phone service", "No", "Yes"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["No internet service", "No", "Yes"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["No internet service", "No", "Yes"]
    )


# ============================================================
# COLUMN 2 - SERVICES & BILLING INFORMATION
# ============================================================

with col2:

    st.subheader("🛠️ Services & Billing Information")

    device_protection = st.selectbox(
        "Device Protection",
        ["No internet service", "No", "Yes"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No internet service", "No", "Yes"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No internet service", "No", "Yes"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No internet service", "No", "Yes"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=50.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=100.0
    )


# ============================================================
# CREATE NEW DATA
# ============================================================

new_data = pd.DataFrame({

    "gender": [gender],

    "SeniorCitizen": [
        1 if senior_citizen == "Yes" else 0
    ],

    "Partner": [partner],

    "Dependents": [dependents],

    "tenure": [tenure],

    "PhoneService": [phone_service],

    "MultipleLines": [multiple_lines],

    "InternetService": [internet_service],

    "OnlineSecurity": [online_security],

    "OnlineBackup": [online_backup],

    "DeviceProtection": [device_protection],

    "TechSupport": [tech_support],

    "StreamingTV": [streaming_tv],

    "StreamingMovies": [streaming_movies],

    "Contract": [contract],

    "PaperlessBilling": [paperless_billing],

    "PaymentMethod": [payment_method],

    "MonthlyCharges": [monthly_charges],

    "TotalCharges": [total_charges]

})


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.divider()

predict_button = st.button(
    "🔮 Predict Customer Churn",
    use_container_width=True
)


# ============================================================
# PREDICTION LOGIC
# ============================================================

if predict_button:

    # --------------------------------------------------------
    # MODEL PREDICTION
    # --------------------------------------------------------

    prediction = model.predict(new_data)[0]

    # --------------------------------------------------------
    # CHURN PROBABILITY
    # --------------------------------------------------------

    probability = model.predict_proba(new_data)[0][1]

    churn_percentage = round(
        probability * 100,
        2
    )


    # --------------------------------------------------------
    # RISK LEVEL & BUSINESS RECOMMENDATION
    # --------------------------------------------------------

    if churn_percentage < 30:

        risk_level = "Low 🟢"

        recommendation = (
            "Customer has a low churn risk. "
            "Continue providing good service and maintain customer engagement."
        )

    elif churn_percentage < 60:

        risk_level = "Medium 🟡"

        recommendation = (
            "Customer has a moderate churn risk. "
            "Consider offering personalized support or service benefits "
            "to improve customer satisfaction."
        )

    else:

        risk_level = "High 🔴"

        recommendation = (
            "Customer has a high churn risk. "
            "Consider proactive retention offers, discounts, "
            "or personalized customer support."
        )


    # --------------------------------------------------------
    # PREDICTION RESULT
    # --------------------------------------------------------

    if prediction == 1:

        prediction_result = "Likely to Churn ❌"

    else:

        prediction_result = "Likely to Stay ✅"


    # ========================================================
    # DISPLAY PREDICTION RESULTS
    # ========================================================

    st.divider()

    st.markdown(
        '<div class="section-header">📈 Prediction Result</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # RESULT METRICS
    # --------------------------------------------------------

    result_col1, result_col2, result_col3 = st.columns(3)


    with result_col1:

        st.metric(
            "Prediction",
            prediction_result
        )


    with result_col2:

        st.metric(
            "Churn Probability",
            f"{churn_percentage}%"
        )


    with result_col3:

        st.metric(
            "Risk Level",
            risk_level
        )


    # ========================================================
    # BUSINESS RECOMMENDATION BOX
    # ========================================================

    st.write("")

    with st.container(border=True):

        st.subheader("💡 Business Recommendation")

        st.write(recommendation)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    '<div class="footer">'
    'Built with Python • Pandas • Scikit-learn • Streamlit • Machine Learning'
    '</div>',
    unsafe_allow_html=True
)

