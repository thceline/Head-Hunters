import pandas as pd
import os
from pathlib import Path
import io


current_directory = os.getcwd()

filename_1= r'ofertas-empleo (1).csv'

ofertas = os.path.join(current_directory, filename_1)

df1 =  pd.read_csv(ofertas)


columnas_inutiles = 'description'

# Use the drop method to eliminate the specified column
df1_limpio = df1.drop(columnas_inutiles, axis=1)

print(df1_limpio.info())

# Perform additional cleaning and processing as needed

# Save the cleaned data to a new CSV file
df1_limpio.to_csv('cleaned_data.csv', index=False)