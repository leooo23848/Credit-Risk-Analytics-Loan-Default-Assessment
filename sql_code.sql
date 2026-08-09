-- Consumer Loan Portfolio Risk Analysis

-- 1. Default rate by loan term and credit grade
SELECT
    grade,
    term,
    COUNT(*) AS loans,
    ROUND(
        AVG(loan_status = 'Charged Off') * 100, 2
    ) AS default_rate
FROM loan_data
WHERE loan_status IN ('Fully Paid', 'Charged Off')
GROUP BY grade, term
ORDER BY grade, term;


-- 2. Default rate by income
SELECT
    CASE
        WHEN annual_income < 40000 THEN 'Very Low'
        WHEN annual_income < 60000 THEN 'Low'
        WHEN annual_income < 80000 THEN 'Medium'
        WHEN annual_income < 100000 THEN 'High'
        ELSE 'Very High'
    END AS income_group,

    COUNT(*) AS loans,

    ROUND(
        AVG(loan_status = 'Charged Off') * 100, 2
    ) AS default_rate

FROM loan_data
WHERE loan_status IN ('Fully Paid', 'Charged Off')
GROUP BY income_group
ORDER BY default_rate DESC;
