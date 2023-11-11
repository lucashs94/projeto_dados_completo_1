import os
import glob
from typing import List
import pandas as pd

"""
Funcão para ler arquivos excel de uma pasta e retornar
uma lista de dataframes

args: path(str): caminho da pasta 

return: list: lista de dataframes
"""

path = 'data/input'

def extract_from_path(path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path, '*.xlsx'))
    
    df_list = []
    for file in all_files:
        df_list.append(pd.read_excel(file))
        
    return df_list


if __name__ == '__main__':
    df_list = extract_from_path(path)
    print(df_list)