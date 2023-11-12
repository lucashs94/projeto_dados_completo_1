from typing import List

import pandas as pd


def concatenate_dataframes(df_list: List[pd.DataFrame]) -> pd.DataFrame:

    """
    funcao para concatenar todos os dataframes de uma lista
    em um unico arquivo consolidado

    args:
        df (List(pd.DataFrame)): lista de DataFrames
    """

    return pd.concat(df_list, ignore_index=True)
