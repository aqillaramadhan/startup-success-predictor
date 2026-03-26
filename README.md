# 🚀 Startup Success Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://startup-success-predictor-3dappaj7fgdm3z9zbtm7ien.streamlit.app/)

## 🌐 Live Web Application
**[👉 Click here to try the Startup Success Predictor 👈](https://startup-success-predictor-3dappaj7fgdm3z9zbtm7ien.streamlit.app/)**

*(Note: You can add a screenshot of the web app here later by uploading an image and linking it)*

## 📖 Project Overview
This is an End-to-End Machine Learning project aimed at predicting the operational status of a startup (Operating, Acquired, or Closed) based on historical funding data from Crunchbase. 

The project covers the entire data science lifecycle, including:
* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model Training (Random Forest Classifier)
* Interactive Web App Deployment (Streamlit)

## 🧠 Data Scientist Notes & Critical Insights
While building this predictive model, several real-world data science challenges were identified:
1. **Imbalanced Dataset:** The historical Crunchbase dataset is heavily skewed, with over 85% of startups categorized as 'Operating'. This majority class bias inherently makes the model lean towards predicting ongoing operations, highlighting the reality of working with raw historical data.
2. **Feature Starvation:** The model relies on quantitative features (Total Funding, Funding Rounds, and Startup Age). In a real-world business context, startup success is heavily influenced by qualitative factors (e.g., founder competence, business model viability, macroeconomic conditions) that are not captured in this dataset.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Manipulation & Processing:** Pandas
* **Machine Learning:** Scikit-Learn
* **Deployment & UI:** Streamlit

---
*Developed by Muhammad Aqilla Ramadhan* *Student of Artificial Intelligence, IPB University | Data Analyst*