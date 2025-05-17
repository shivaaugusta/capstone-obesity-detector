# Obesity Prediction App

This is a Streamlit web application for predicting obesity levels based on personal and lifestyle inputs. It is built as part of a Data Science Capstone Project at Universitas Dian Nuswantoro.

## 📌 Features
- Predicts obesity level using a trained Random Forest model.
- Input features include age, gender, weight, height, and daily habits.
- Built with Streamlit, deployed via Streamlit Cloud.

## 🧠 Model
The model was trained using the [Obesity Dataset](https://drive.google.com/file/d/16mZS56ed1SQyimDxRGGKvihvIMri2exM/view?usp=sharing) with preprocessing steps such as:
- Handling missing values
- Encoding categorical data
- Feature scaling
- SMOTE for class balancing
- Hyperparameter tuning using GridSearchCV

## 🚀 How to Run Locally
1. Clone this repo:
git clone https://github.com/shivaaugusta/capstone-obesity-detector
.git
cd capstone-obesity-detector

2. Install requirements:
pip install -r requirements.txt

3. Run the app:
streamlit run app.py

