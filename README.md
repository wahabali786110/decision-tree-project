
# Customer Churn Prediction Using Decision Tree 🌳

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to leave a company using a **Decision Tree Classifier**.

The project covers the complete ML workflow, from data exploration and preprocessing to model training, evaluation, and deployment using **Streamlit**.

## 📌 Project Overview

Customer churn occurs when customers stop using a company's services. Predicting churn can help telecom companies identify customers at risk of leaving and plan customer retention strategies.

This project uses a Decision Tree Classifier to predict customer churn based on customer information such as tenure, monthly charges, contract type, and internet services.

## ✨ Features

- Interactive web application built with Streamlit
- Customer churn prediction (Churn / No Churn)
- Estimated churn probability
- User-friendly input form
- Input validation
- Automated preprocessing using a Scikit-learn Pipeline
- One-Hot Encoding for categorical features
- Model caching for efficient predictions

## 📊 Dataset

**Dataset:** IBM Telco Customer Churn

**Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

The model uses the following seven features:

| Feature | Description |
|---------|-------------|
| tenure | Number of months the customer has stayed |
| MonthlyCharges | Customer's monthly bill |
| Contract | Customer's contract type |
| InternetService | Type of internet service |
| PaymentMethod | Customer's payment method |
| TechSupport | Whether technical support is available |
| OnlineSecurity | Whether online security is available |

**Target Variable:** Churn (Yes / No)

## 🛠️ Technologies Used

- **Python** — Programming language
- **Pandas** — Data manipulation
- **Matplotlib & Seaborn** — Data visualization
- **Scikit-learn** — Machine Learning
- **Decision Tree Classifier** — Prediction algorithm
- **OneHotEncoder** — Categorical encoding
- **ColumnTransformer & Pipeline** — Preprocessing
- **Joblib** — Model serialization
- **Streamlit** — Web application

## 🔄 Machine Learning Workflow

### 1. Exploratory Data Analysis (EDA)
- Understanding the dataset
- Checking data types and missing values
- Univariate and bivariate analysis
- Visualizing feature distributions
- Analyzing customer churn patterns

### 2. Data Preprocessing
- Selecting relevant features
- Separating features and target variable
- Splitting training and testing data
- Encoding categorical features using OneHotEncoder
- Building a preprocessing pipeline

### 3. Model Training
- Training a Decision Tree Classifier
- Experimenting with different maximum depths
- Using validation data for hyperparameter selection
- Selecting the model using F1-score

### 4. Model Evaluation
The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

### 5. Model Deployment
- Saving the trained Pipeline using Joblib
- Creating an interactive Streamlit application
- Loading the trained model
- Predicting customer churn from user inputs

## 📈 Model Information

| Parameter | Value |
|-----------|-------|
| Algorithm | Decision Tree Classifier |
| Max Depth | 2 |
| Minimum Samples per Leaf | 10 |
| Feature Encoding | One-Hot Encoding |
| Model Selection Metric | F1-score |
| Train-Test Split | 80% / 20% |

The model was developed as a beginner-friendly implementation of an end-to-end Machine Learning workflow.

## 📂 Project Structure

```text
decision-tree-project/
│
├── app.py
├── churn.ipynb
├── Customer_Churn.csv
├── customer_churn_model.pkl
├── requirements.txt
└── README.md
```

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/wahabali786110/decision-tree-project.git
```

### 2. Navigate to the Project Directory

```bash
cd decision-tree-project
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💻 How to Use

1. Open the Streamlit application.
2. Enter the customer's tenure and monthly charges.
3. Select the contract type, internet service, payment method, technical support, and online security options.
4. Click **Predict Churn**.
5. View the predicted churn status and estimated churn probability.

## ⚠️ Limitations

- The model uses only seven customer features.
- The Decision Tree has a maximum depth of 2, limiting the complexity of its predictions.
- Customers reaching the same leaf node receive the same estimated probability.
- Predictions are based on historical data and may not generalize to every telecom company.
- The predicted probabilities have not been calibrated.

## 🔮 Future Improvements

- Experiment with additional features.
- Implement cross-validation and GridSearchCV.
- Compare Decision Trees with Random Forest and other algorithms.
- Improve model performance through hyperparameter tuning.
- Add feature importance visualizations.
- Improve the Streamlit dashboard.
- Deploy the application publicly.

## 👨‍💻 Author

**Abdul Wahab**

Software Engineering Student | Machine Learning Enthusiast

GitHub: [wahabali786110](https://github.com/wahabali786110)

---

⭐ If you find this project useful, consider giving the repository a star!
