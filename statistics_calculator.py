import numpy as np
from scipy import stats

def calculator(data):
  # computing
  mean = np.mean(data)
  median = np.median(data)
  mode = stats.mode(data, keepdims=True).mode[0]
  variance = np.var(data)
  std_dev = np.std(data)
  min = np.min(data)
  max = np.max(data)
  percentiles = np.percentile(data, [25, 50, 75])

  # printing
  print("\n📊 Basic Statistics Report:")
  print(f"Mean: {mean:.2f}")
  print(f"Median: {median:.2f}")
  print(f"Mode: {mode}")
  print(f"Variance: {variance:.2f}")
  print(f"Standard Deviation: {std_dev:.2f}")
  print(f"Min: {min}, Max: {max}")
  print(f"25th Percentile: {percentiles[0]:.2f}")
  print(f"50th Percentile (Median): {percentiles[1]:.2f}")
  print(f"75th Percentile: {percentiles[2]:.2f}")

data = list(map(int, input("Enter the data seperated by spaces: ").strip().split()))
calculator(data)