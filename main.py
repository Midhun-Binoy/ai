import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("titanic.csv")

print(data)

data.fillna({"Age": data["Age"].mean()}, inplace=True)
print(data["2urvived"].value_counts(normalize=True))
print(data.groupby(["Sex", "Pclass"])["2urvived"].mean())

sns.barplot(x="Sex", y="2urvived", data=data)
plt.title("Survival rate by gender")
plt.show()
