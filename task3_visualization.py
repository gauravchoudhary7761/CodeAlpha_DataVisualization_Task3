import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales_data.csv")

# Set style
sns.set_theme(style="whitegrid")

# -------- Line Chart: Sales Trend --------
plt.figure(figsize=(10, 5))
sns.lineplot(x="Month", y="Sales", data=df, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_trend.png")
plt.show()

# -------- Bar Chart: Profit --------
plt.figure(figsize=(10, 5))
sns.barplot(x="Month", y="Profit", data=df)
plt.title("Monthly Profit Analysis")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("profit_chart.png")
plt.show()

# -------- Pie Chart: Sales Distribution --------
plt.figure(figsize=(8, 8))
plt.pie(df["Sales"], labels=df["Month"], autopct="%1.1f%%", startangle=140)
plt.title("Sales Contribution by Month")
plt.tight_layout()
plt.savefig("sales_distribution.png")
plt.show()

print("✅ TASK 3: Data Visualization Completed Successfully!")
