import pandas as pd
import openpyxl

df = pd.read_csv('C:\project\python\data\cities.csv', sep=",")
df.to_excel('C:\project\python\data\cities.xlsx', index=1)


