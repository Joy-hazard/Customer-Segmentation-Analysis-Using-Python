📊 Customer Segmentation Analysis

A Python-based data analysis project that segments customers based on demographics and purchasing behavior using K-Means clustering. & An **interactive Excel dashboard** built using Pivot Tables and Pivot Charts to analyze customer behavior, spending patterns, and marketing campaign effectiveness. This project demonstrates **end-to-end data analysis** — from raw data preparation to actionable business insights.

## 🔍 Key Features

- Data cleaning & feature engineering

- Exploratory Data Analysis (EDA)

- Customer segmentation using K-Means

- Data visualization with Matplotlib

## 🛠 Tools & Tech Stack

- Python
- Pandas, NumPy
- Matplotlib
- Scikit-learn
- Microsoft Excel
- Pivot Tables & Pivot Charts
- Conditional Formatting
- Slicers
- Excel Formulas


▶️ How to Run
pip install pandas numpy matplotlib scikit-learn
python segmentation_analysis.py

## 🧮 Data Preparation & Calculated Columns

The following calculated fields were created in Excel:

- **Age**  
  `=YEAR(TODAY()) - Year_Birth`

- **Total Amount Spent**  
  `=MntWines + MntMeatProducts + MntFishProducts + MntFruits + MntSweetProducts + MntGoldProds`

- **Total Children**  
  `=Kidhome + Teenhome`

- **Age Group**  
  `<30, 30–45, 46–60, 60+`

- **Income Group**  
  `Low, Medium, High`

- **Customer Segment**  
  `High Value / Low Value`

## 📊 Key Analyses Performed

### 🔹 Demographic Analysis
- Customer count by education level
- Average income by marital status

### 🔹 Sales & Spending Analysis
- Total spending by product category
- Age group vs total spending
- Income group vs average spending

### 🔹 Customer Behavior Analysis
- Purchase channel preference (Web / Store / Catalog)
- Campaign acceptance analysis

### 🔹 Segmentation Analysis
- High-value vs low-value customers
- Family size vs spending behavior

### ✅ Interactive Elements
- Slicers for:
  - Age Group
  - Education
  - Marital Status
- Dynamic Pivot Charts:
  - Spending by Product
  - Spending by Age Group
  - Campaign Effectiveness
  - Customer Segmentation

📈 Outcome

Customers are grouped into meaningful segments to support targeted marketing and business decision-making.

## 🧠 How to Explain This Project in an Interview

> “I built an interactive Excel dashboard using Pivot Tables to analyze customer demographics, spending behavior, and campaign performance.  
I segmented customers based on age, income, and purchase behavior to identify high-value customers and provided insights that can support targeted marketing strategies.”

---

## 📌 Project Use Case

This project is suitable for:
- Data Analyst / Business Analyst portfolios
- Excel dashboard demonstrations
- Interview case discussions
- Marketing & customer analytics practice

👤 Author

Joy Pal
🔗 https://github.com/Joy-hazard
