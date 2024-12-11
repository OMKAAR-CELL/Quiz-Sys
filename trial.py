import pandas as pd

# Load the CSV file
df = pd.read_csv('Quiz-Sys/users.csv')
print(df)
print(len(df))
df.loc[2]=['xyz','456787']
print(df)
df.to_csv('Quiz-Sys/users.csv', index=False)