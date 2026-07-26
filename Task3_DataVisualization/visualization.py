import os
import pandas as pd
import matplotlib.pyplot as plt

# Create graphs folder
os.makedirs("graphs", exist_ok=True)

# Load dataset
df = pd.read_csv("Iris.csv")

print(df.head())

# ---------------- Scatter Plot ----------------
plt.figure(figsize=(8,6))

for species in df["Species"].unique():
    subset = df[df["Species"] == species]
    plt.scatter(
        subset["SepalLengthCm"],
        subset["PetalLengthCm"],
        label=species
    )

plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.grid(True)
plt.savefig("graphs/scatter_plot.png")
plt.close()

# ---------------- Histogram ----------------
plt.figure(figsize=(8,6))
plt.hist(df["SepalLengthCm"], bins=10)

plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.grid(True)

plt.savefig("graphs/histogram.png")
plt.show()

print("Graphs saved successfully.")