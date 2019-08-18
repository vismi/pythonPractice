import numpy as np
import pandas as pd

from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc("font", size=14)
import seaborn as sns
sns.set(style="white") #white background style for seaborn plots
sns.set(style="whitegrid", color_codes=True)

# Setting test and train Data Frames
titanic_df = pd.read_csv("train.csv")

test_df = pd.read_csv("test.csv")

titanic_df.head(5)