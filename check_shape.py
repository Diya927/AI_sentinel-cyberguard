import pandas as pd

df = pd.read_csv("data/KDDTrain+.txt", header=None)
print(df.shape)