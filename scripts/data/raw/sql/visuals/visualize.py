import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/sales_data_clean.csv")

# Revenue by product
product_revenue = df.groupby("product")["revenue"].sum().sort_values(ascending=False).head(10)
product_revenue.plot(kind="bar", figsize=(10, 6), title="Top 10 Products by Revenue")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("visuals/top_products.png")
plt.close()

# Revenue trend over time
daily_revenue = df.groupby("date")["revenue"].sum()
daily_revenue.plot(figsize=(10, 6), title="Daily Revenue Trend")
plt.ylabel("Revenue ($)")
plt.xlabel("Date")
plt.tight_layout()
plt.savefig("visuals/daily_revenue.png")
plt.close()

print("Visualizations saved in the 'visuals' folder.")
