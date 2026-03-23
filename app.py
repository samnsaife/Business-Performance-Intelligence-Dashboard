import streamlit as st
import pandas as pd

st.set_page_config(page_title="Business Intelligence Dashboard", layout="wide")

st.title("📊 Business Performance Intelligence Dashboard")
st.write("Executive KPI Reporting | Retail Growth & Profit Analytics")

# Load cleaned dataset
df = pd.read_csv("data/cleaned_superstore.csv")

# --- KPI Section ---
st.subheader("Executive KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"₹{df['sales'].sum():,.0f}")
col2.metric("Total Profit", f"₹{df['profit'].sum():,.0f}")
col3.metric("Profit Margin %", f"{df['profit_margin'].mean():.2f}%")
col4.metric("Total Orders", len(df))

# --- Monthly Trend ---
st.subheader("📈 Monthly Sales Trend")
monthly_sales = df.groupby("month")["sales"].sum()
st.line_chart(monthly_sales)

# --- Regional Profit Leakage ---
st.subheader("🌍 Profit Leakage by Region")
region_profit = df.groupby("region")["profit"].sum().sort_values()
st.bar_chart(region_profit)

# --- Top Products ---
st.subheader("🏆 Top 10 Products by Revenue")
top_products = (
    df.groupby("product_name")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
st.bar_chart(top_products)

# --- Consulting Insights ---
st.subheader("💡 Consulting Insights & Recommendations")

st.write("""
- Regions with negative profit indicate **pricing or logistics inefficiencies**  
- Certain categories consistently underperform → **portfolio optimization needed**  
- Monthly sales spikes suggest opportunities for **seasonal growth strategy**  
- Focus on high-value customers to maximize retention and profitability  
""")
