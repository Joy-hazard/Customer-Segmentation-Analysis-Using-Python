import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("marketing_campaign.csv", sep="\t")

# -----------------------------
# Feature Engineering
# -----------------------------

# Create Age column
current_year = 2026
df["Age"] = current_year - df["Year_Birth"]

# Total amount spent
df["TotalAmountSpent"] = (
    df["MntFishProducts"]
    + df["MntFruits"]
    + df["MntGoldProds"]
    + df["MntSweetProducts"]
    + df["MntMeatProducts"]
    + df["MntWines"]
)

# Handle missing income
df["Income"].fillna(df["Income"].median(), inplace=True)

# Remove zero spenders
df = df[df["TotalAmountSpent"] > 0]

# -----------------------------
# Univariate Analysis
# -----------------------------
plt.figure()
plt.hist(df["Age"], bins=range(10, 100, 5))
plt.title("Distribution of Customer Age")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.show()

# -----------------------------
# Bivariate Analysis
# -----------------------------
plt.figure()
plt.scatter(df["Income"], df["TotalAmountSpent"])
plt.title("Income vs Total Spending")
plt.xlabel("Income")
plt.ylabel("Total Amount Spent")
plt.show()

# -----------------------------
# Multivariate Analysis (3D)
# -----------------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.scatter(
    df["Income"],
    df["TotalAmountSpent"],
    df["Age"]
)

ax.set_xlabel("Income")
ax.set_ylabel("Total Amount Spent")
ax.set_zlabel("Age")
ax.set_title("Customer Distribution (3D View)")
plt.show()

# -----------------------------
# Clustering Preparation
# -----------------------------
cluster_data = df[["Income", "TotalAmountSpent"]]

# Log transform (safe for zero values)
cluster_data_log = np.log1p(cluster_data)

# Scaling
scaler = StandardScaler()
cluster_scaled = scaler.fit_transform(cluster_data_log)

# -----------------------------
# Elbow Method
# -----------------------------
inertia = []

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(cluster_scaled)
    inertia.append(kmeans.inertia_)

plt.figure()
plt.plot(range(1, 11), inertia, marker="o")
plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.show()

# -----------------------------
# Final KMeans Model
# -----------------------------
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(cluster_scaled)

# -----------------------------
# Cluster Visualization
# -----------------------------
plt.figure()
for cluster in df["Cluster"].unique():
    cluster_df = df[df["Cluster"] == cluster]
    plt.scatter(
        cluster_df["Income"],
        cluster_df["TotalAmountSpent"],
        label=f"Cluster {cluster}"
    )

plt.title("Customer Segmentation using KMeans")
plt.xlabel("Income")
plt.ylabel("Total Amount Spent")
plt.legend()
plt.show()
