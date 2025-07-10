import pandas as pd
import os
import pyreadr

os.chdir(r"c:\Surfdrive\Data Science Textbook\data")
for file in os.listdir():
    if file.endswith('.RData'):
        filename=str(file).split('.')[0]
        result = pyreadr.read_r(file)
        df=pd.DataFrame(result[filename])
        df.columns= [col.replace('.','_').replace(' ','_').lower() for col in df.columns]
        filename=filename.lower()
        df.to_csv(f'csv\\{filename}.csv', index=False)
        df.to_pickle(f'pickle\\{filename}.pkl')
        df.to_parquet(f'parquet\\{filename}.parquet')

#Separately convert the corona dataset
df = pd.read_excel('COVID-19-geographic-disbtribution-worldwide.xlsx')
df.columns= [col.replace('.','_').replace(' ','_').lower() for col in df.columns]
df.to_csv('csv\\corona.csv', index=False)
df.to_pickle('pickle\\corona.pkl')
df.to_parquet('parquet\\corona.parquet')