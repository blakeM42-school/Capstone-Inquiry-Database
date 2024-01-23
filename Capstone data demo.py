import pandas as pd

nba = pd.read_csv('C:\\Users\\blake\\Desktop\\Capstone Project\\NBA_Player_Stats.csv')

print(nba.head(10))
x = nba.head(10)

print(nba.columns)

print(x[['Player', 'FG%']])

print(nba.iloc[1:4])

print(nba.iloc[2,1])

for index, row in nba.iterrows():
    print(index, row['Player'])

print(nba.loc[nba['Player'] == "Jamal Murray"])

print(nba.describe())

print(nba.sort_values(['Player', 'PTS'], ascending=[1,0]))

print(nba.loc[nba['PTS'] >= 30.0])