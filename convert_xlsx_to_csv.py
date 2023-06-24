import pandas as pd

def xlsx_to_csv(xlsx_file, csv_file):

    df = pd.read_excel(xlsx_file)
    
    df.to_csv(csv_file, index=False)

xlsx_file = 'tez.xlsx' 
csv_file = 'your_dataset.csv' 

xlsx_to_csv(xlsx_file, csv_file)
