import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
 
resourcesPath = 'resources/'
fileName = 'exampleData.xlsx'



df = pd.read_excel(resourcesPath + fileName, header=[1,2], sheet_name='test', encoding='utf-8')


# df_parsed= pd.concat(df.values(), axis=0)
 
print("Column headings:")
print(df)
print(df.columns)
print(df.columns.levels)
# print(df_parsed.columns)