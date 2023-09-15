import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('top1000billionaires.csv')  

# Boxplot

plt.figure(figsize=(10, 6))
sns.boxplot(x='Country of Citizenship', y='Net Worth', data=data)
plt.title('Boxplot of Net Worth by Country')
plt.xticks(rotation=45)
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x="Country of Citizenship", shrink=.8)
plt.title('Histogram of Billionares per Country')
plt.xticks(rotation=90)
plt.xlabel('Country of Citizenship')
plt.ylabel('Amount')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=data, x="Age", y="Net Worth", shrink=.8)
plt.title('Histogram of Age x Net Worth')
plt.xticks(rotation=90)
plt.xlabel('Age')
plt.ylabel('Net Worth')
plt.show()

# Heatmap
correlation_matrix = data.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()