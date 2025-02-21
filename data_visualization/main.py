import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
# generate data
data = np.random.randint(0, 101, 1000)

# compute statistical measures
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
variance = np.var(data)
# print(mean, median, std_dev, variance)

# visualization
plt.hist(data, bins=10, color='skyblue', edgecolor='black')
plt.axvline(mean - 0.5, color='red', linestyle='dashed', linewidth=3, label="Mean")  
plt.axvline(median + 0.5, color='green', linestyle='dashed', linewidth=3, label="Median")  
plt.legend()
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Distribution of Student Scores")
plt.show()