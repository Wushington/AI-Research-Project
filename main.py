import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Load the data
data = pd.read_csv('data//FinalData.csv')

data_features = data[['Project', 'Quiz', 'Exam']]
X = data[data_features]
y = data.Homework

plt.subplot(2, 1, 1)
plt.scatter(X['Project'], y)
plt.subplot(2, 1, 2)
plt.scatter(X['Quiz'], y)
plt.subplot(2, 1, 3)
plt.scatter(X['Exam'], y)

# def loss_function(m, b, points):
#     totalError = 0
#     for i in range(0, len(points)):
#         x = points[i, 0]
#         y = points[i, 1]
#         totalError += (y - (m * x + b)) ** 2
#     return totalError / float(len(points))