# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:16:31 2025
@author: LEGION
"""

import pandas as pd


# Load dataset
df = pd.read_csv(r"C:\Users\User\Downloads\Data_Demand_.csv")

# Basic Info
print(df.info())
print(df.describe())
print(df.head())
print("Initial shape:", df.shape)

# Check for nulls and duplicates
print("Missing values:\n", df.isnull().sum())
print("Duplicate records:", df.duplicated().sum())

# Convert 'Date' column
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')

# Fill missing Order_ID (if any)
df['Order_ID'] = df['Order_ID'].fillna("Unknown")

# Backfill missing dates
df['Date'] = df['Date'].bfill()

# Fill categorical columns with mode
cat_cols = ['Warehouse', 'Dealer', 'Customer_ID', 'Machine_ID', 'Machine_Type',
            'Production_Status', 'Change_Type', 'Order_Volatility']

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Fill numerical columns with median
num_cols = ['Order_Quantity', 'Inventory_Level', 'Lead_Time_Days', 'Delay_Days']
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Drop duplicates
df.drop_duplicates(inplace=True)

# Final check for missing values
print("After cleaning - Missing values:\n", df.isnull().sum())
print("Final shape:", df.shape)



# Save cleaned dataset
cleaned_path = r"C:\Elevate labs Task 1\Cleaned_Data_Demand_Dataset.csv"
df.to_csv(cleaned_path, index=False)
print(f"✅ Cleaned data saved to: {cleaned_path}")

