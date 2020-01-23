import pandas as pd
data_frame = pd.read_csv('example.csv')
print(type(data_frame))
print(data_frame.head(3))
print(data_frame.describe())