import pandas as pd
import os
from pathlib import Path
import io


current_directory = os.getcwd()

filename_1= r'clean_datasets\cleaned_data.csv'
filename_2= r'clean_datasets\cleaned_data_GD.csv'

ofertas = os.path.join(current_directory, filename_1)
glass = os.path.join(current_directory, filename_2)

df =  pd.read_csv(ofertas)
df2 = pd.read_csv(glass)

print(df.info())
print(df2.info())


print(df['salary_max'])
print(df2['salary/max'])