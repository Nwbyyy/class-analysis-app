import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler


cols = ["student names", "class year", "major", "GPA"]
ds = pd.read_excel("coding.xlsx", names = cols)
for label in cols[:-1]:
  plt.hist(df[df["GPA"] == 4][label], color='blue',label='4.0', alpha=0.7, density=True)
  plt.hist(df[df["class"]==0][label], color='red',label='hadron', alpha=0.7, density=True)
  plt.title(label)
  plt.ylabel("Probability")
  plt.xlabel(label)
  plt.legend()
  plt.show()
