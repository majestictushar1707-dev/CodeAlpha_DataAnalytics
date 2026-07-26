import pandas as pd
import os

# Load the dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Display first 5 rows
print("========== First 5 Rows ==========")
print(df.head())

print("\n========== Dataset Shape ==========")
print(df.shape)

print("\n========== Column Names ==========")
print(df.columns)
print("\n========== Dataset Information ==========")
df.info()

print("\n========== Missing Values ==========")
print(df.isnull().sum())

print("\n========== Statistical Summary ==========")
print(df.describe())

import matplotlib.pyplot as plt
import seaborn as sns

# Set graph style
sns.set_style("whitegrid")

# Create graphs folder if it doesn't exist
# os.makedirs("graphs", exist_ok=True)

# Survival Count Plot
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Survived")

plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")

plt.savefig("graphs/survival_count.png")
plt.close()

# Survival by Gender
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Sex", hue="Survived")

plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")

plt.savefig("graphs/survival_by_gender.png")
plt.close()

# Age Distribution
plt.figure(figsize=(8,5))

sns.histplot(df["Age"], bins=30, kde=True)

plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")

plt.savefig("graphs/age_distribution.png")
plt.close()

# Passenger Class Distribution
plt.figure(figsize=(6,4))

sns.countplot(data=df, x="Pclass")

plt.title("Passenger Class Distribution")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")

plt.savefig("graphs/passenger_class_distribution.png")
plt.close()

# Fare Distribution
plt.figure(figsize=(8,5))

sns.histplot(df["Fare"], bins=40, kde=True)

plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")

plt.savefig("graphs/fare_distribution.png")
plt.close()

# Correlation Heatmap
plt.figure(figsize=(10, 6))

numeric_df = df.select_dtypes(include=["number"])

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.savefig("graphs/correlation_heatmap.png")
plt.close()

print("\n" + "=" * 50)
print("FINAL INSIGHTS")
print("=" * 50)

print("1. The Titanic dataset contains 891 passengers and 12 columns.")
print("2. Age, Cabin, and Embarked columns contain missing values.")
print("3. Female passengers had a much higher survival rate than male passengers.")
print("4. Most passengers belonged to the 3rd passenger class.")
print("5. Most passengers were between 20 and 40 years old.")
print("6. Ticket fares were highly uneven, with a few very expensive tickets.")
print("7. Passenger class had a noticeable relationship with survival.")
print("8. The dataset provides valuable insights into survival patterns on the Titanic.")