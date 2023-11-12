from pipeline.extract import extract_from_path
from pipeline.load import load_as_excel
from pipeline.transfom import concatenate_dataframes

if __name__ == '__main__':
    df_list = extract_from_path('data/input')
    df = concatenate_dataframes(df_list)
    load_as_excel(df, 'data/output', 'output')
