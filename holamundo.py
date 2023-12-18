import pandas as pd
import os
from pathlib import Path

#Obtiene el path relativo del archivo
current_directory = os.getcwd()



#guardamos los nombres de los documentos a cargar
filename_1= r'ofertas-empleo (1).csv'

filename_2= r'ofertas-de-empleo-sample (1).csv'

filename_3= r'dataset_glassdoor-jobs-scraper_2023-02-05_01-07-13-866 (1).csv'

#obtenemos el path del documento juntando el path del archivo con el nombre de cada documento.csv  
ofertas = os.path.join(current_directory, filename_1)

sample = os.path.join(current_directory, filename_2)

glassdoor = os.path.join(current_directory, filename_3)



df1 =  pd.read_csv(ofertas)
df2 =  pd.read_csv(sample)
df3 =  pd.read_csv(glassdoor)


#print(df1.info())
#print(df2.info())
print(df3.head())


name = df3['companyDetails/careerOpportunitiesRating']
print(name)

