import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("dataset.csv")

print(data.info())
print(data.isnull().sum())

data.hist(figsize=(10,6))
plt.show()

sns.boxplot(data=data.select_dtypes(include=['int64']))
plt.show()

numeric_data = data.select_dtypes(include=['int64'])
sns.heatmap(numeric_data.corr(), annot=True)
plt.show()