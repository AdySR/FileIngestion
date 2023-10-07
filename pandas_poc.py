import pandas as pd

organization_df = pd.read_csv(r'C:\programs\pyprojects\FileIngestion\misc\organizations_1.csv',sep=',')

print(organization_df)
print(organization_df.info())

