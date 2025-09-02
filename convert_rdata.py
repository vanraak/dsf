import pandas as pd
import os
import pyreadr
os.chdir(r'C:\GitHub\dsf')
data_dir = os.path.join(os.getcwd(), "sourcedata")

for file in os.listdir(data_dir):
    if file.endswith('.RData'):
        filename = os.path.splitext(file)[0]
        file_path = os.path.join(data_dir, file)
        result = pyreadr.read_r(file_path)
        df=pd.DataFrame(result[filename])
        df.columns= [col.replace('.','_').replace(' ','_').lower() for col in df.columns]
        filename=filename.lower()
        df.to_csv(os.path.join('csv', f'{filename}.csv'), index=False)
        df.to_pickle(os.path.join('dsf', 'data', f'{filename}.pkl'))
        df.to_parquet(os.path.join('parquet', f'{filename}.parquet'))

for file in os.listdir(data_dir):
    if file.endswith('.csv'):
        file_path = os.path.join(data_dir, file)
        filename = os.path.splitext(file)[0].lower()
        df=pd.read_csv(file_path)
        df.to_csv(os.path.join('csv', f'{filename}.csv'), index=False)
        df.to_pickle(os.path.join('dsf', 'data', f'{filename}.pkl'))
        df.to_parquet(os.path.join('parquet', f'{filename}.parquet'))

#Separately convert the corona dataset
df = pd.read_excel(data_dir+'/COVID-19-geographic-disbtribution-worldwide.xlsx')
df.columns= [col.replace('.','_').replace(' ','_').lower() for col in df.columns]
df.to_csv('csv\\corona.csv', index=False)
df.to_pickle('dsf\\data\\corona.pkl')
df.to_parquet('parquet\\corona.parquet')