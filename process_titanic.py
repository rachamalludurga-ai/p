import pandas as pd

df = pd.read_csv('titani-testdata.csv')
print(df.head())

males = df[df['Sex'] == 1].copy()
females = df[df['Sex'] == 0].copy()

# 2. Write to separate CSV files
# index=False prevents pandas from adding an extra column for the row numbers
males.to_csv('males.csv', index=False)
females.to_csv('females.csv', index=False)

print("Files created successfully.")