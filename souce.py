import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#from sklearn.preprocessing import StandardScaler
#from imblearn.over_sampling import RandomOverSampler

#pip install xlrd


def read_file():
    ds = pd.read_excel("coding.xlsx")
    ds.head()
