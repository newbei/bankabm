import pandas as pd

df_rel = pd.read_csv('因果关系梳理.csv', header=0)


def get_by_key(df, key, results, depth):
    results_tmp = [] + results
    results.append(key)
    results_key = list(df[df['Causal'] == key]['Result'].values)

    if len(set(results) & set(results_key)) > 0:
        print(key, set(results) & set(results_key))
        return results

    if depth >= 10:
        return results

    if len(results_key) == 0:
        return results

    result_final = []
    for k in results_key:
        result_final.append(k)
        get_by_key(df, k, results, depth + 1)

    # print(results)
    return results + result_final


# print(get_by_key(df_rel, 'BankEquity_0', [], 1))

def get_dag_by_key(df, key, dags):
    results_key = list(df[df['Causal'] == key]['Result'].values)

    if len(set(dags) & set(results_key)) > 0:
        print(dags + [key] + list(set(dags) & set(results_key)))
        exit()

        # return dags + [key] + list(set(dags) & set(results_key))

    if len(results_key) == 0:
        return dags
    for k in results_key:
        get_dag_by_key(df, k, dags + [key])

    return dags + [key] + results_key


dags = []
for key in df_rel['Causal'].values:
    print('begin', key)
    get_dag_by_key(df_rel, key, [])
