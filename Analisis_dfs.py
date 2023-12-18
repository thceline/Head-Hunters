import pandas as pd
import os
from pathlib import Path

#Obtiene el path relativo del archivo
current_directory = os.getcwd()

#guardamos los nombres de los documentos a cargar

a = r'ofertas-empleo (1).csv'

b = r'ofertas-de-empleo-sample (1).csv'

c = r'dataset_glassdoor-jobs-scraper_2023-02-05_01-07-13-866 (1).csv'

#creamos variables con los paths

ofertas = os.path.join(current_directory, a)

sample = os.path.join(current_directory, b)

glassdoor = os.path.join(current_directory, c)

#creamos los df

df_ofertas =  pd.read_csv(ofertas)
df_sample =  pd.read_csv(sample)
df_glassdoor =  pd.read_csv(glassdoor)

print(df_ofertas.head())