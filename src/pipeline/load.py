import os

import pandas as pd


def load_as_excel(df: pd.DataFrame, output_path: str, file_name: str) -> str:

    """
    Receber um dataframe e salvar em excel

    args:
        df (pd.DataFrame): dataframe que sera salvo
        output_path (str): onde o arquivo será salvo
        file_name (str): nome do excel que será salvo
    """

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    df.to_excel(f'{output_path}/{file_name}.xlsx', index=False)
    return 'Salvo com sucesso!'
