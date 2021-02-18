import pandas as pd

df = pd.read_csv('sample.csv', sep=",")
df.to_excel('excel.xlsx', index=1)


