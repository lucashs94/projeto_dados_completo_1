from typing import List
import pandas as pd 


"""
funcao para concatenar todos os dataframes de uma lista
em um unico arquivo consolidado
"""


def concatenate_dataframes(df_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(df_list, ignore_index=True)