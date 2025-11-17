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

Let r be the rate of disease.

$sensitivity = sn = TP / r$

$r * sn = TP$

$1 - specificity = 1 - sp = FP/(1 - r)$

$(1 - sp)(1 - r) = FP$

$precision = r * sn / (r * sn + (1 - sp)(1 - r))$

$precision * r * sn + precision * (1 - sp) - precision * (1 - sp) * r = r * sn$

$precision * (1 - sp) = r * (sn - precision * sn + precision * (1 - sp))$

$r = precision * (1 - sp) / (sn - precision * sn + precision * (1 - sp))$

Diagnosis only: When specificity is .712, sensitivity .796, and precision .443, the rate of the condition is 22.35%

Medication only: When specificity is .784, sensitivity .817, and precision .488, the rate of the condition is 20.13%

Medication and Diagnosis only: When specificity is .823, sensitivity .831, and precision .571, the rate of the condition is 22.09%

In the context of this paper it is fairly clear that their reported specificity, sensitivity, and precision values are based on their 1:4 matched cohort rather than the general patient population. This is normally considered bad or misleading practice, especially when trying to advertise a model's capability to be applied to a more general healthcare cohort. Since this paper's purpose is to argue for the model's deployment, I feel that reporting these values instead of those collected from running these models on a general population rate based test set means that the performance reported in Table 2 oversells the model's predictive value. Deployment of the model in its current state would likel result in too many false positives to be clinically valuable. This alongside their poor matching criteria continues to suggest that their evaluation technique is overfitting to general risk factors like age and healthcare interaction complexity rather than identifying truly discernable factors that could see reasonable use in a health system.

As an additional note, I noticed that the imputed rates based on the provided evaluation metrics are not all the same. I did some tests with rounding values and found that the differences do not come from rounding error on the metrics alone. This signals to me that there might be some filtering steps when working with the medication-only group (possibly removing patients without any medications) that is resulting in a difference beetween comparisons. This is just another example of poor reporting quality that further undermines the value of their approach for evaluating model effectiveness.
