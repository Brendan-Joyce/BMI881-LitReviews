import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

raw_df = pd.read_csv('feigin2014_table1_mortality.csv')

strata1_col = 'age_group'
strata2_col = 'income_group'
xCol = 'year'
heightCol = 'mortality_rate'

i = 0
maxVal = -1
fig, axes = plt.subplots(1, len(raw_df[strata2_col].unique()),figsize = (12,3.5))
for strata1_val in raw_df[strata1_col].unique():
    j = 0
    for strata2_val in raw_df[strata2_col].unique():
        strata_df = raw_df[(raw_df[strata1_col] == strata1_val) & (raw_df[strata2_col] == strata2_val)].sort_values(xCol).copy()
        axes[i].bar(np.arange(strata_df.shape[0]) + .3 * (j-1),strata_df[heightCol],
                        yerr = (strata_df[heightCol] - strata_df['interval_low'],
                                strata_df['interval_high'] - strata_df[heightCol]),
                        label=strata2_val,
                        width = .3)
        axes[i].set_xticks(np.arange(strata_df.shape[0]), strata_df['year']);
        axes[i].set_xlabel('year')
        axes[i].set_yscale('log')
        val = axes[i].get_ylim()[1]
        if(val > maxVal):
            maxVal = val
        j = j + 1
    axes[0].set_ylabel('Mortality Rate [log(patients per million)]')
    axes[-1].legend(bbox_to_anchor=(1.65,.65),title='Income Group')
    axes[i].set_title(f'Ages {strata1_val}')
    i = i + 1
for ax in axes:
    ax.set_ylim(bottom = 10, top = maxVal)
plt.tight_layout()
plt.savefig('./MortalityRateVisualization.png', bbox_inches='tight')
plt.close()