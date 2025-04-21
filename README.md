# Data-Cleaning-Demand-Dataset
This repository contains a data cleaning project on a demand and supply dataset using Python and Pandas.

# Data Cleaning Project – Demand and Supply Management Dataset
This project focuses on cleaning a raw dataset related to demand and supply management. It involves identifying and handling missing values, duplicates, inconsistent data formats, and ensuring data quality. The cleaned dataset is ready for further analysis, visualization, or modeling.

# Objective

To prepare a clean, structured dataset by applying essential data preprocessing techniques using Python and Pandas.

---
# Files Included

| File Name                             | Description                                         
|--------------------------------------|-----------------------------------------------------
| `Data_Demand_.csv`                   | Raw dataset containing missing values and duplicates 
| `Cleaned_Data_Demand_Dataset.csv`    | Final cleaned and processed dataset                
| `Data_cleaning.py`            | Python script used for data cleaning               
| `README.md`                          | Project documentation      

---
# Technologies Used

- Python
- Pandas

---
# Data Cleaning
- Converted `Date` column to datetime format (`dd-mm-yyyy`)
- Filled missing `Order_ID` with "Unknown"
- Backfilled missing values in `Date`
- Filled missing values in categorical columns with the mode
- Filled missing values in numerical columns with the median
- Removed duplicate records

---
# Exploratory Stats
Performed statistical analysis on key numeric fields:
- Mean, Median, Mode
- Variance, Standard Deviation, Range
- Skewness and Kurtosis

---
# Final Output

- All missing values handled appropriately
- Duplicate entries removed
- Data types standardized
- Cleaned dataset saved as `Cleaned_Data_Demand_Dataset.csv`

---
# Learnings

This task improved my hands-on skills in:
- Data cleaning using Pandas
- Handling null values and duplicates
- Understanding data distribution using statistical metrics
- Preparing datasets for analysis
