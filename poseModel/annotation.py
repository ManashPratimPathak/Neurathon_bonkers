import numpy as np
import pandas as pd

data = pd.read_csv('./data/label.csv')

for i in range(12):
    for j in range(17):
        print(data['x'][j + i*17], end=',')
        print(data['y'][j + i*17], end=',')
    print()
