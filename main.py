import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
data = pd.read_csv('data//Combined Data.csv')
data


# def loss_function(m, b, points):
#     totalError = 0
#     for i in range(0, len(points)):
#         x = points[i, 0]
#         y = points[i, 1]
#         totalError += (y - (m * x + b)) ** 2
#     return totalError / float(len(points))