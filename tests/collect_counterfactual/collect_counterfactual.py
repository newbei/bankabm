import pandas as pd
import os

BASE_PATH = r'D:\datas\abm\results_v0.0.4_1'
data_path = BASE_PATH + os.sep + 'result'
result_name = 'counterfactual.csv'
counterfactual_file = BASE_PATH + os.sep + 'counterfactual.csv'

for dirpath, dirnames, filenames in os.walk(data_path):
    result = pd.DataFrame()
    for filepath in filenames:
        if filepath == result_name:
            continue
        print(os.path.join(dirpath, filepath))
        file = os.path.join(dirpath, filepath)
        df = pd.read_csv(file)
        if result.shape[0] == 0:
            df.columns = df.columns
        result = result.append(df[df['BankId'] == 1].tail(1))
    result.to_csv(counterfactual_file, index=False)
