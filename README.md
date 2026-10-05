# Healthcare Appointment No-Show Analysis

## 📌 Project Overview

Healthcare organizations face challenges when patients miss scheduled appointments, leading to inefficient resource utilization and scheduling difficulties.

This project analyzes healthcare appointment data to identify patterns associated with appointment no-shows and builds a machine learning model to support better scheduling and patient management.

The project combines **Python, Machine Learning, and Power BI** to transform appointment data into actionable insights.

---

## 🎯 Objectives

- Analyze appointment attendance and no-show behaviour.
- Identify factors associated with missed appointments.
- Examine the relationship between SMS reminders and attendance.
- Analyze no-show patterns across age groups and weekdays.
- Study the impact of waiting periods on appointment attendance.
- Build a machine learning model to predict appointment no-shows.
- Develop an interactive Power BI dashboard for healthcare insights.
- Provide recommendations to improve appointment management.

---

## 🛠️ Tools & Technologies

- **Python**
- **Pandas**
- **Scikit-learn**
- **Matplotlib**
- **Seaborn**
- **Power BI**
- **DAX**
- **Decision Tree Classification**

---

## 📂 Dataset

The project uses a healthcare appointment dataset containing information related to:

- Patient demographics
- Appointment dates
- Waiting periods
- SMS reminders
- Scholarship status
- Hypertension
- Diabetes
- Alcoholism
- Handicap status
- Appointment attendance

The dataset was cleaned and transformed before analysis and modelling.

---

## 🔄 Project Workflow

### 1. Data Preparation

The dataset was loaded and inspected using Python.

Data preparation included:

- Checking dataset dimensions
- Checking missing values
- Removing duplicate records
- Converting date fields
- Creating appointment weekdays
- Calculating waiting days
- Encoding the appointment outcome

### 2. Exploratory Data Analysis

The analysis examined:

- Overall appointment attendance
- No-show rate
- No-show behaviour by weekday
- No-show behaviour by age group
- SMS reminder patterns
- Waiting-period patterns
- Patient-related factors

### 3. Machine Learning

A **Decision Tree Classifier** was developed to predict appointment no-shows.

Features used included:

- Age
- Scholarship
- Hypertension
- Diabetes
- Alcoholism
- Handicap
- SMS received
- Waiting days

The dataset was divided into training and testing sets using an 80/20 split.

### 4. Power BI Dashboard

An interactive Power BI dashboard was created to communicate the analysis.

The dashboard includes:

- Total appointments
- No-show appointments
- Attended appointments
- No-show rate
- Average waiting days
- No-show rate by weekday
- Appointment attendance
- No-show rate by age group
- SMS reminder analysis
- Waiting-period analysis
- Patient-factor analysis
- Key recommendations

---

## 📊 Key Insights

The analysis highlights several patterns in appointment attendance:

- Appointment no-show behaviour varies across weekdays.
- No-show behaviour differs across age groups.
- SMS reminder status can be examined as an important appointment-management factor.
- Waiting periods show differences in appointment attendance behaviour.
- Patient characteristics can help identify segments that may require closer monitoring.

---

## 💡 Recommendations

Based on the analysis, healthcare organizations can consider:

- Strengthening reminder communication for scheduled appointments.
- Monitoring appointments with longer waiting periods.
- Identifying higher-risk patient segments.
- Using historical attendance patterns to support scheduling decisions.
- Using data-driven appointment management to improve resource utilization.

---

## 📁 Project Files

| File | Description |
|------|-------------|
| `medical_appointment_noshows.py` | Python data cleaning, analysis and machine learning code |
| `medical_appointment_cleaned.csv` | Cleaned dataset used for analysis |
| `power bi (elevate).pbix` | Power BI interactive dashboard |

---

## 📈 Dashboard

The Power BI dashboard provides an analyst-style overview of healthcare appointment attendance, no-show behaviour, reminder effectiveness and scheduling patterns.

---

## 🚀 Skills Demonstrated

**Data Analytics:**  
Data Cleaning • Exploratory Data Analysis • KPI Analysis • Pattern Identification

**Machine Learning:**  
Decision Tree Classification • Train/Test Split • Classification Evaluation • Feature Importance

**Visualization:**  
Power BI • DAX • Dashboard Design • Data Storytelling

**Programming:**  
Python • Pandas • Scikit-learn • Matplotlib • Seaborn

---

## 👩‍💻 Author

**Rathika Priyanka**

B.Com FinTech | Data & Financial Analytics

Interested in Data Analytics, Business Analytics and Financial Analytics.
