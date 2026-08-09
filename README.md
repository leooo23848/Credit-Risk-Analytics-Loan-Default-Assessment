# Consumer Loan Portfolio Risk Analysis

## Objective

Analyze a consumer loan portfolio to identify borrower risk patterns and provide data-driven lending recommendations.

## Dataset

The dataset contains approximately 38.6K consumer loan records with information on:

- Loan status
- Annual income
- Credit grade
- Loan term
- Loan purpose
- Verification status
- Debt-to-income ratio
- Home ownership

Only loans with final outcomes — Fully Paid and Charged Off — were used for default analysis.

## Tools

- Python(pandas,numpy)
- MySQL
- Kaggle(dataset)

## Approach

--Checked the dataset structure, data types, missing values and basic statistics.

--Filtered the dataset to loans with known final outcomes:

  - Fully Paid = 0
  - Charged Off = 1

--This allowed us to calculate the observed default rate.

--Segmented borrowers based on income and analyzed default rates across income groups.

--Compared 36-month and 60-month loan default rates within each credit grade.

This helped us move beyond simple overall averages and examine the interaction between credit grade and loan tenure.

## Key Insights

### Insight 1 — Income-Based Risk Pattern

Default rates declined from approximately **17.4% for the lowest-income segment to 10.9% for the highest-income segment**, representing approximately a **37% relative reduction**.

**Business implication:** Income can be considered as an additional borrower segmentation variable when assessing lending risk.

### Insight 2 — Loan Tenure & Credit Grade

60-month loans showed higher default rates than 36-month loans across Grades A-F.

For example:

- Grade C: **23.55% vs 14.02%**
- Grade D: **28.68% vs 17.53%**
- Grade E: **29.75% vs 19.70%**

**Business implication:** Loan tenure should be considered alongside credit grade when evaluating lending risk and underwriting policies.

## Conclusion

The analysis shows that default risk varies across borrower characteristics and loan structure. Rather than relying only on credit grade, lenders can use additional segmentation such as income and loan tenure to support more informed lending decisions.
