# 🎓 Placement Prediction & Skill Gap Analyzer

## 📌 Overview

This project predicts whether a student will get placed or not using **Machine Learning** and provides insights through a dashboard. It covers the complete pipeline from **data preprocessing to deployment**.

---

## 🎯 Objective

* Predict student placement status
* Identify key factors affecting placement
* Help students understand skill gaps
* Provide data-driven insights

---

## 🧰 Tech Stack

* **Python (Pandas, NumPy)** – Data Cleaning & EDA
* **Scikit-learn** – Machine Learning Model
* **Pickle (.pkl)** – Model Saving
* **Streamlit** – Web App Deployment
* **Power BI** – Dashboard Visualization

---

## 📊 Dataset

The dataset contains student academic and skill-related information:

* StudentID
* CGPA
* Internships
* Projects
* Workshops/Certifications
* AptitudeTestScore
* SoftSkillsRating
* ExtracurricularActivities
* PlacementTraining
* SSC Marks, HSC Marks
* PlacementStatus

👉 [View Dataset](./placedata v2.0 synthetic.csv)

---

## ⚙️ Project Workflow

1. **Data Cleaning**

   * Handled missing values
   * Converted categorical data (Yes/No → 1/0)
   * Checked duplicates

2. **EDA (Exploratory Data Analysis)**

   * Analyzed CGPA vs Placement
   * Compared skills vs placement rate
   * Identified important features

3. **Model Building**

   * Used classification algorithm (Logistic Regression / etc.)
   * Trained model on cleaned dataset
   * Evaluated accuracy

4. **Model Saving**

   * Saved trained model using `.pkl` file

5. **Deployment**

   * Built interactive UI using Streamlit
   * User inputs data → model predicts placement

6. **Dashboard**

   * Created Power BI dashboard for insights

---

## 📊 Dashboard Features

* Placement Rate Analysis
* CGPA vs Placement
* Skills Impact (Internship, Projects, Training)
* Academic Performance Analysis
* Key Factors Affecting Placement

---

## 🔥 Key Insights

* 📈 Higher **CGPA** increases placement chances
* 🧠 **Aptitude score & soft skills** play a major role
* 💼 Students with **internships & projects** are more likely to be placed
* 🎯 **Placement training** significantly improves success rate
* 📊 Academic scores (SSC/HSC) have moderate impact

---

## 🤖 Model Output

* Predicts: **Placed / Not Placed**
* Can be extended to show **probability (%)**

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 💼 Business / Student Value

* Helps students improve required skills
* Assists institutions in training decisions
* Provides data-driven career guidance

---

## 📸 Dashboard & App
<img width="1109" height="602" alt="image" src="https://github.com/user-attachments/assets/bab04180-8e89-47bb-bcc2-5499d152322e" />

