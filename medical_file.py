print("PYTHON PROGRAM STARTED")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

file_path = r"C:\Users\S.A Rathika Priyanka\Downloads\medical_appointment_noshows.csv"

df = pd.read_csv(file_path)

print("\nDataset loaded successfully")
print(df.shape)
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace("-", "_")
    .str.replace(" ", "_")
)

df = df.drop_duplicates()

df["scheduledday"] = pd.to_datetime(
    df["scheduledday"],
    errors="coerce"
)

df["appointmentday"] = pd.to_datetime(
    df["appointmentday"],
    errors="coerce"
)

df["appointment_weekday"] = df["appointmentday"].dt.day_name()

df["scheduled_date_only"] = df["scheduledday"].dt.normalize()
df["appointment_date_only"] = df["appointmentday"].dt.normalize()

df["waiting_days"] = (
    df["appointment_date_only"] -
    df["scheduled_date_only"]
).dt.days

df["waiting_days"] = df["waiting_days"].clip(lower=0)

df["no_show_target"] = df["no_show"].map({
    "No": 0,
    "Yes": 1
})

df = df.dropna(subset=["no_show_target"])

df["no_show_target"] = df["no_show_target"].astype(int)

print("\nNo-Show Counts")
print(df["no_show"].value_counts())

print("\nNo-Show Percentage")
print((df["no_show"].value_counts(normalize=True) * 100).round(2))

print("\nAverage Age")
print(round(df["age"].mean(), 2))

print("\nAverage Age by Status")
print(df.groupby("no_show")["age"].mean().round(2))

print("\nWeekday Analysis")
weekday_analysis = pd.crosstab(
    df["appointment_weekday"],
    df["no_show"],
    normalize="index"
) * 100
print(weekday_analysis.round(2))

print("\nSMS Analysis")
sms_analysis = pd.crosstab(
    df["sms_received"],
    df["no_show"],
    normalize="index"
) * 100
print(sms_analysis.round(2))

features = [
    "age",
    "scholarship",
    "hipertension",
    "diabetes",
    "alcoholism",
    "handcap",
    "sms_received",
    "waiting_days"
]

X = df[features]
y = df["no_show_target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model = DecisionTreeClassifier(
    random_state=42,
    max_depth=5
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy")
print(round(accuracy * 100, 2), "%")

print("\nConfusion Matrix")
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("\nClassification Report")
print(classification_report(y_test, y_pred))

feature_importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance")
print(feature_importance)

test_results = X_test.copy()
test_results["actual_no_show"] = y_test.values
test_results["predicted_no_show"] = y_pred

output_path = (
    r"C:\Users\S.A Rathika Priyanka\Downloads"
    r"\medical_appointment_cleaned.csv"
)

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved")
print(output_path)

plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="no_show")
plt.title("Appointment Attendance vs No-Show")
plt.xlabel("Appointment Status")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 5))
sns.countplot(
    data=df,
    x="sms_received",
    hue="no_show"
)
plt.title("SMS Reminder vs Appointment Status")
plt.xlabel("SMS Received")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

weekday_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

sns.countplot(
    data=df,
    x="appointment_weekday",
    hue="no_show",
    order=weekday_order
)

plt.title("Appointment Status by Weekday")
plt.xlabel("Appointment Weekday")
plt.ylabel("Number of Patients")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))

sns.barplot(
    data=feature_importance,
    x="Importance",
    y="Feature"
)

plt.title("Decision Tree Feature Importance")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.tight_layout()
plt.show()

print("\nFINAL DATA CHECK")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Minimum waiting days:", df["waiting_days"].min())
print("Maximum waiting days:", df["waiting_days"].max())
print("No-show rate:", round(df["no_show_target"].mean() * 100, 2), "%")

print("\nHEALTHCARE NO-SHOW PROJECT COMPLETED")