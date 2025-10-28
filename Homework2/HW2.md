# Homework 2
1.	If a test has sensitivity = 80% and specificity 80% and the prevalence of the disease is 9/100,000, what is the positive predictive value (aka “precision”) of the test?

$TP + FN = 9 per 100,000$

$TN + FP = 1 – (9/100,000) = 99,991 per 100,00$

Going forward the denominator (100,000) will be removed from all calculations as the units will be implicitly “patients per 100,000”.

| | | 
|---|---|
| $Sensitivity = .8 = TP / (TP + FN)$ | $Specificity = .8 = TN / (FP + TN)$ |
| $.8 = TP / 9$ | $1 - Specificity = 1 - .8 = FP / 99,991$ |
| $7.2 = TP$ | $19,998.2 = FP$ |


$Precision = 7.2 / (7.2 + 19,998.2) = .000360$ or **.0360%**

2.	Suppose sensitivity = specificity. What would they have to be to achieve positive predictive value = 50% when prevalence is 9/100,000?

$Sensitivity = Specificity = p$

$p = TP/9$

$9p = TP$

$(1 - p) = FP / 99,991$

$(1 – p) * 99,991 = FP$

$Precision = 9p / (9p + (1 – p) * 99,991) = .5$

$18p = 9p + (1 – p) * 99,991$

$9p = 99,991 - 99,991p$

$100,000p = 99,991$

$p = .99991$

Specificity and Sensitivity must be **99.991%** to achieve a precision of 50%

3.	Comment on these results in relation to the precision values provided in Table 2 of Wang et al. (2019).
