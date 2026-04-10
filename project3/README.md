# 🛍️ Customer Behavior & Shopping Trends Dashboard

## 📌 Overview

This project analyzes customer shopping behavior using a structured dataset and presents insights through an interactive dashboard. It demonstrates end-to-end **Data Analytics workflow** including data cleaning, SQL analysis, and visualization.

---

## 🎯 Objectives

* Analyze customer purchase patterns
* Identify top product categories
* Understand impact of discounts, shipping & payment methods
* Segment customers based on behavior

---

## 🧰 Tech Stack

* **Python (Pandas, NumPy)** – Data Cleaning & EDA
* **MySQL** – Data Analysis
* **Power BI / Excel** – Dashboard

---

## 📊 Dataset
- [Download Dataset](./cleaned_data.csv)


---

## 🗄️ SQL Setup

```sql
USE shopping_db;
SHOW TABLES;
SELECT * FROM customers LIMIT 20;
```

---

## 🔍 Key SQL Queries

```sql
-- Category Distribution
SELECT Category, COUNT(*) AS total
FROM customers
GROUP BY Category
ORDER BY total DESC;

-- Gender vs Spending
SELECT Gender, AVG(Purchase_Amount) AS avg_spending
FROM customers
GROUP BY Gender;

-- Top Customers
SELECT Customer_ID, SUM(Purchase_Amount) AS total_spent
FROM customers
GROUP BY Customer_ID
ORDER BY total_spent DESC
LIMIT 5;

-- Payment Methods
SELECT Payment_Method, COUNT(*) 
FROM customers
GROUP BY Payment_Method;
```

---

## 📊 Dashboard Highlights

* Customer Segmentation
* Top Products by Rating
* Gender vs Spending
* Sales by Season
* Payment & Shipping Analysis
* Discount Impact

---

## 🔥 Key Insights

* Clothing category drives highest sales
* Male customers have higher average spending
* Discounts significantly boost purchases
* Express/Free shipping increases order value
* Majority users are returning/loyal customers

---

## 💼 Business Value

Helps businesses improve **marketing strategy, pricing decisions, and customer targeting** using data-driven insights.

---

## 📸 Dashboard
<img width="1086" height="603" alt="image" src="https://github.com/user-attachments/assets/e986ed7b-fd43-48b2-aee2-41257f8d3636" />

