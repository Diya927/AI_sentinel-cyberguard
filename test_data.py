from src.data_preprocessing import load_data

df = load_data("data/KDDTrain+.txt")

print(df.head())
print(df.shape)