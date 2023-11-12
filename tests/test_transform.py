import pandas as pd

from src.pipeline.transfom import concatenate_dataframes

df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df2 = pd.DataFrame({'col1': [7, 9], 'col2': [10, 11]})


def test_concatenacao_da_lista_de_dataframes():

    list_df = [df1, df2]
    df = pd.concat(list_df, ignore_index=True)

    act = concatenate_dataframes(list_df)

    assert act.shape == (4, 2)
    assert act.equals(df)
