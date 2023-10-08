filepath =r'C:\programs\pyprojects\FileIngestion\dir_source\organizations_1.csv'

import pandas as pd

df_or = pd.read_csv(filepath, sep =',')
# print(df_or.info())

column_datatype_dict = df_or.dtypes.apply(lambda x: x.name).to_dict()
print('column datatype list-',column_datatype_dict)

# sep , column list , column data type , column data type 


import csv

with open(filepath)as fp:
    reader = csv.reader(fp)
    headers = next(reader)        # The header row is now consumed
    ncol = len(headers)
    nrow = sum(1 for _ in reader)


print('header-',headers)

sniffer = csv.Sniffer()
dialect = sniffer.sniff(str(headers))
print('seperator-',dialect.delimiter)
