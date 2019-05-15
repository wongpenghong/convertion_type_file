import pandas as pd
import csv

a = pd.read_csv("data_sentiment.csv")
b = pd.read_csv("negative.csv")

merged = a.append(b)

print(merged.describe())

#print(merged.index)

#with open('final_data.csv', 'w', encoding='utf-8') as f:
 #   merged.to_csv(f, index=False)
