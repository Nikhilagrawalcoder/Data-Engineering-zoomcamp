import sys
import pandas as pd

# print('arguments',sys.argv)

# month=int(sys.argv[1])

df = pd.DataFrame({"Day": [1, 2], "No_passenger": [3, 4]})
df.to_parquet(f"test file");
print(df)
# print(f'Hello piplein Month={month}')
