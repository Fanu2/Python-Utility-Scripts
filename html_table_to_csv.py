import pandas as pd

html_file = 'table.html'
csv_file = 'table.csv'

tables = pd.read_html(html_file)
df = tables[0]
df.to_csv(csv_file, index=False)
