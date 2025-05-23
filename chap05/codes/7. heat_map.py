# import pandas, numpy, and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.width', 53)
pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv", parse_dates=["lastdate"])

# generate a correlation matrix
corr = covidtotals.corr(numeric_only=True)
corr[['total_cases','total_deaths',
  'total_cases_pm','total_deaths_pm']]

# show scatter plots
fig, axes = plt.subplots(1,2, sharey=True)
sns.regplot(x="median_age", y="total_cases_pm", data=covidtotals, ax=axes[0])
sns.regplot(x="gdp_per_capita", y="total_cases_pm", data=covidtotals, ax=axes[1])
axes[0].set_xlabel("Median Age")
axes[0].set_ylabel("Cases Per Million")
axes[1].set_xlabel("GDP Per Capita")
axes[1].set_ylabel("")
plt.suptitle("Scatter Plots of Age and GDP with Cases Per Million")
plt.tight_layout()
fig.subplots_adjust(top=0.92)
plt.show()

# generate a heat map
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, cmap="coolwarm")
plt.title('Heat Map of Correlation Matrix')
plt.tight_layout()
plt.show()

