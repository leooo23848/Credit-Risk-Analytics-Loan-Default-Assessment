import pandas as pd
import numpy as np

df = pd.read_excel("financial_loan.xlsx")

print("Dataset Shape:", df.shape)
print(df.head())

# Keep only loans with a final outcome
analysis_df = df[
    df["loan_status"].isin(["Fully Paid", "Charged Off"])
].copy()

# Create default flag
analysis_df["default"] = (
    analysis_df["loan_status"] == "Charged Off"
).astype(int)

print("\nTotal Loans Analyzed:", len(analysis_df))

# Overall default rate
default_rate = analysis_df["default"].mean() * 100

print("Overall Default Rate:", round(default_rate, 2), "%")




analysis_df["income_group"] = pd.qcut(
    analysis_df["annual_income"],
    5,
    labels=["Very Low", "Low", "Medium", "High", "Very High"]
)

income_result = (
    analysis_df
    .groupby("income_group", observed=False)["default"]
    .mean() * 100
)

print("\nDefault Rate by Income Group:")
print(income_result.round(2))


# Calculate relative reduction
low_income_rate = income_result.iloc[0]
high_income_rate = income_result.iloc[-1]

reduction = (
    (low_income_rate - high_income_rate)
    / low_income_rate
) * 100

print(
    "\nRelative reduction from lowest to highest income:",
    round(reduction, 2),
    "%"
)

grade_term_result = (
    analysis_df
    .groupby(["grade", "term"])["default"]
    .mean() * 100
)

print("\nDefault Rate by Credit Grade and Loan Term:")
print(grade_term_result.round(2))

