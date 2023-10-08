filepath =r'C:\programs\pyprojects\FileIngestion\dir_source\organizations_1.csv'

import pandas as pd

df_or = pd.read_csv(filepath, sep =',')

print(df_or)
df_columns_list = df_or.columns.to_list()
print(df_columns_list)

df_columns_str = str(df_columns_list)
print(df_columns_str)

import csv

sniffer = csv.Sniffer()
dialect = sniffer.sniff(df_columns_str)
print(dialect.delimiter)


