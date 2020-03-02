import pandas as pd

data = pd.read_excel('./raw_data/pensum_is_io.xlsx')

for index, row in data.iterrows():
    print(index, row['Asignatura'])