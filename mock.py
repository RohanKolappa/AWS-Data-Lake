import pandas as pd
import numpy as np

num_rows = 10000
num_columns = 5

data = np.random.randint(1, 100, size = (num_rows, num_columns))

df = pd.DataFrame(data, columns=[f'Column_{i}' for i in range(1, num_columns + 1)])

df.to_csv('mock_data.csv', index=False)
