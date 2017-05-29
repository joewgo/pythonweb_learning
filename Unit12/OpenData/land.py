import pandas as pd

res = pd.read_csv('./opendata/A_LVR_LAND_C.CSV', encoding='big5')

print(res.describe())
print(res.mean())

with open('./statistic.csv', 'w') as f:
    f.write(res.describe().to_csv())
