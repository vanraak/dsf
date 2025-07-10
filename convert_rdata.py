import pandas as pd
import os
import pyreadr

data_dir = os.path.join(os.getcwd(), "sourcedata")

for file in os.listdir(data_dir):
    if file.endswith('.RData'):
        filename = os.path.splitext(file)[0]
        file_path = os.path.join(data_dir, file)
        result = pyreadr.read_r(file_path)
        df=pd.DataFrame(result[filename])
        df.columns= [col.replace('.','_').replace(' ','_').lower() for col in df.columns]
        filename=filename.lower()
        df.to_csv(f'csv\\{filename}.csv', index=False)
        df.to_pickle(f'pickle\\{filename}.pkl')
        df.to_parquet(f'dsf\\data\\{filename}.parquet')

#Separately convert the corona dataset
df = pd.read_excel(data_dir+'/COVID-19-geographic-disbtribution-worldwide.xlsx')
df.columns= [col.replace('.','_').replace(' ','_').lower() for col in df.columns]
df.to_csv('csv\\corona.csv', index=False)
df.to_pickle('pickle\\corona.pkl')
df.to_parquet('dsf\\data\\corona.parquet')