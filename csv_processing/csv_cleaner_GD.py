import pandas as pd
import os
from pathlib import Path
import io


current_directory = os.getcwd()

filename_1= r'dataset_glassdoor-jobs-scraper_2023-02-05_01-07-13-866 (1).csv'

ofertas = os.path.join(current_directory, filename_1)

df1 =  pd.read_csv(ofertas)

columnas_inutiles =["companyDetails/careerOpportunitiesRating","companyDetails/ceoName","companyDetails/ceoName/__typename","companyDetails/ceoName/name","companyDetails/ceoName/photoUrl","companyDetails/companyRating","companyDetails/compensationAndBenefitsRating","companyDetails/cultureAndValuesRating","companyDetails/headquarters","companyDetails/industry","companyDetails/industry/industryId","companyDetails/logo","companyDetails/size","companyDetails/type","companyDetails/website","companyDetails/workLifeBalanceRating","companyDetails/yearFounded","employerRating","id","jobDetails","url"]
# Use the drop method to eliminate the specified column
df1_limpio = df1.drop(columnas_inutiles, axis=1)

print(df1_limpio.info())

# Perform additional cleaning and processing as needed

# Save the cleaned data to a new CSV file
df1_limpio.to_csv('cleaned_data_GD.csv', index=False)