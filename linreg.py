import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_xlsx('Combined Data.xlsx')
print(df)