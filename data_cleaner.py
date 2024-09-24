import pandas as pd

data = pd.read_csv('data.csv')
cleaned_data = data.dropna()
cleaned_data.to_csv('cleaned_data.csv', index=False)
