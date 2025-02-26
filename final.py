import pandas as pd

# Use the raw GitHub URL and specify the engine
url = 'https://raw.githubusercontent.com/tasawar301/final_year_ocular/main/dataset/ODIR-5K/ODIR-5K/data.xlsx'
df = pd.read_excel(url, engine='openpyxl')

# Check the first few rows of the dataframe
print(df.head())
