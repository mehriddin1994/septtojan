# 📊 Project Assignment: 2025 Sales Analysis for the "BozorUz" Online Store

**Course:** Python Programming — NumPy, Pandas, Matplotlib
**Submission format:** Jupyter Notebook (`.ipynb`) + PNG charts + short report
**Data file:** `sales_2025.csv`

---

## 1. Scenario (Introduction)

You have just been hired as a **Data Analyst** at **"BozorUz"**, an online store that sells products through 7 branches across Uzbekistan.

The company director hands you a file containing every order placed during 2025 and says:

> *"Our data is a mess: some rows are duplicated, some values are missing, and some are just plain wrong. Clean it up and prepare an analysis that will help me make decisions for next year. Show me with numbers and charts."*

Your task is to answer the director's questions using **numbers and charts**.

---

## 2. Data Description

The file `sales_2025.csv` contains **just over 5,000** orders. Columns:

| Column | Description | Type |
|---|---|---|
| `order_id` | Unique order number | integer |
| `date` | Order date (`YYYY-MM-DD`) | text → date |
| `branch` | Branch that received the order | text |
| `category` | Product category | text |
| `price` | Price of one item (in UZS) | number |
| `quantity` | Number of items purchased | number |
| `discount_pct` | Discount (0, 5, 10, 15, 20 %) | number |
| `payment_type` | Cash, Uzcard, Humo, Click, Payme | text |
| `customer_age` | Customer's age | number |
| `customer_gender` | Male / Female | text |
| `rating` | Customer rating (1–5) | number |

> ⚠️ **Note:** The file intentionally contains errors. Finding them is part of the assignment.

---

## 3. Tasks

### 🔹 Stage 1. Exploring the Data (10 points)

1. Load the file using `pandas`.
2. Print the shape of the table (number of rows and columns).
3. Display the first 10 rows and the last 5 rows.
4. Identify the data type (`dtype`) of each column.
5. Count the missing (`NaN`) values in each column and also show them as a **percentage**.
6. Print the basic descriptive statistics for the numeric columns.
7. Write a conclusion: based on the statistics, which columns appear to contain **suspicious** values?

---

### 🔹 Stage 2. Data Cleaning (20 points)

Print the number of rows **before and after** each step.

1. Find the **duplicate rows**, report how many there are, and remove them.
2. Standardize the values in the `branch` column (letter case, extra spaces). After cleaning, exactly **7** unique branches should remain.
3. Convert the `date` column to the `datetime` type.
4. Identify **negative** values in the `quantity` column. Explain how you handled them and **why** you chose that approach.
5. Find unrealistic values in the `customer_age` column (e.g., greater than 100). Replace them with `NaN`.
6. Fill in missing values:
   - `price` — with the **median of that category**;
   - `customer_age` — with the median of the whole column;
   - drop rows where `quantity` or `payment_type` is missing;
   - `rating` — leave missing, but take this into account in your analysis.
7. Save the cleaned data as `sales_2025_clean.csv`.

---

### 🔹 Stage 3. Creating New Columns — NumPy (15 points)

Create the following columns using **NumPy functions** (`np.where`, `np.select`, `np.round`, etc.):

1. `total_amount` = `price × quantity`
2. `discount_amount` = `total_amount × discount_pct / 100`
3. `paid_amount` = `total_amount − discount_amount`
4. `month` — month number from the date; `month_name` — month name; `weekday` — day of the week
5. `age_group` — using `np.select`:
   - 16–24 → `"Young"`
   - 25–39 → `"Adult"`
   - 40–54 → `"Middle-aged"`
   - 55+ → `"Senior"`
6. `payment_method` — using `np.where`: `"Cash"` if the payment type is Cash, otherwise `"Electronic"`.
7. Convert the `paid_amount` column to a NumPy array and compute the following **using NumPy only**: mean, median, standard deviation, maximum, minimum, and the 25th and 75th percentiles.

---

### 🔹 Stage 4. Analytical Questions — Pandas (25 points)

For each question, provide **code + a result table + a 1–2 sentence conclusion**.

1. What was the total revenue (`paid_amount`) for the year? Show the result in **millions of UZS**, rounded.
2. For each **branch**: number of orders, total revenue, and average order value. Sort by revenue in descending order.
3. Which **category** generated the most revenue? Which one sold the most **units**? Are they the same? Why or why not?
4. Calculate revenue by **month**. Identify the best and worst months.
5. Using `pivot_table`, build a **branch × category** table (values: total revenue in millions of UZS).
6. Which **payment type** is the most popular? Show the share of electronic vs. cash payments as percentages.
7. Which category does each **age group** spend the most money on?
8. Does the average **quantity** increase as the discount percentage increases? Check using `groupby`.
9. Calculate the average **rating** for each category. Which category has the lowest rating?
10. Count the number of orders by **day of the week**. On which day is sales activity highest?
11. Display the **TOP 10** orders with the highest `paid_amount`.
12. Is there a difference in average order value between male and female customers?

---

### 🔹 Stage 5. Visualization — Matplotlib (20 points)

Every chart must have a **title, axis labels**, and a **legend** where needed. Save each chart as a `.png` file (`plt.savefig`).

| # | Chart | Type |
|---|---|---|
| 1 | Monthly revenue trend | Line chart (`plot`) with markers |
| 2 | Total revenue by branch | Horizontal bar chart (`barh`), sorted |
| 3 | Share of revenue by category | Pie chart (`pie`) with percentages |
| 4 | Distribution of customer ages | Histogram (`hist`) with 20 bins |
| 5 | Relationship between price and quantity | Scatter plot (`scatter`), colored by category |
| 6 | Distribution of `paid_amount` by category | Box plot (`boxplot`) |
| 7 | Electronic vs. cash payments by month | Grouped or stacked bar chart (`bar`) |
| 8 | **Dashboard:** 4 charts in one figure, 2×2 layout | `plt.subplots(2, 2)` |

For the dashboard, choose the 4 charts you consider most important for the director and add an overall title (`suptitle`).

---

### 🔹 Stage 6. Report and Recommendations (10 points)

At the end of the notebook, write a **"Summary for the Director"** section (in a Markdown cell, 150–250 words):

1. The **5 most important findings** (with numbers).
2. At least **3 practical recommendations** for the company. For example: which branch needs attention, when to run promotions, which category to develop.
3. **Limitations** of the analysis: what shortcomings in the data could affect the results?

---

## 4. ⭐ Bonus Tasks (+10 points)

Complete any **two** of the following:

- **A.** Calculate the month-over-month percentage change in revenue (`pct_change`) and show positive and negative changes in different colors on a bar chart.
- **B.** Compute the correlation matrix of the numeric columns and draw a heatmap using `imshow`. Write the values inside the cells.
- **C.** Calculate weekly revenue (`resample('W')`) and plot it together with a 4-week rolling average (`rolling`) on one chart.
- **D.** Use NumPy to fit a linear trend (`np.polyfit`) to monthly revenue and forecast revenue for January 2026.
- **E.** Wrap the entire analysis in a single function: `analyze(file_name, branch=None)` — if a branch is given, it should output the key metrics and 2 charts for that branch only.

---

## 5. Grading Criteria

| Stage | Points |
|---|---|
| 1. Exploring the data | 10 |
| 2. Data cleaning | 20 |
| 3. New columns with NumPy | 15 |
| 4. Pandas analysis | 25 |
| 5. Matplotlib visualization | 20 |
| 6. Report and recommendations | 10 |
| **Total** | **100** |
| Bonus | +10 |

**Additional requirements** (points deducted if not met):

- The code must run without errors from start to finish (`Restart & Run All`) — **−10 points**
- Each stage must be separated by a Markdown heading — **−5 points**
- Variable names must be meaningful (not `a`, `x1`, `df2`) — **−5 points**
- Charts without a title or axis labels — **−1 point** each

---

## 6. Files to Submit

```
LastName_FirstName_project/
├── project.ipynb             # main notebook
├── sales_2025_clean.csv      # cleaned data
└── charts/
    ├── 01_monthly_revenue.png
    ├── 02_branches.png
    ├── ...
    └── 08_dashboard.png
```

Compress the folder into a `.zip` archive and submit it.

---

## 7. Helpful Tips

- Import the required libraries before you start:
  ```python
  import numpy as np
  import pandas as pd
  import matplotlib.pyplot as plt
  ```
- To make large numbers easier to read, convert them to **millions of UZS** (`/ 1_000_000`).
- After each step, check the result with `head()`, `shape`, or `info()`.
- Use the `figsize` parameter to make charts larger.
- To avoid damaging the original table, do your cleaning on a copy: `df_clean = df.copy()`.

**Good luck! 🚀**
