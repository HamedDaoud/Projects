years = list(range(2011, 2021))
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

movie_dict = {
    'years': years,
    'durations': durations
}

print(movie_dict)

import pandas as pd

durations_df = pd.DataFrame(movie_dict)

print(durations_df)

import matplotlib.pyplot as plt
fig = plt.figure()

plt.plot(durations_df['years'], durations_df['durations'])

plt.title('Netflix Movie Durations 2011-2020')

plt.savefig('Python\\Are Netflix movies getting shorter\\Netflix Movie Durations 2011-2020.png')

netflix_df = pd.read_csv("Python\\Are Netflix movies getting shorter\\datasets\\netflix_data.csv", index_col=0)

print(netflix_df.head())

netflix_df_movies_only = netflix_df[netflix_df["type"] == 'Movie']

netflix_movies_col_subset = pd.DataFrame(netflix_df_movies_only, columns=['title', 'country', 'genre', 'release_year', 'duration'])

print(netflix_movies_col_subset)

fig = plt.figure(figsize=(12, 8))

plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration'])

plt.title("Movie Duration by Year of Release")

plt.show()

short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] < 60]

print(short_movies.head(20))

colors = []

for lab, row in netflix_movies_col_subset.iterrows():
    if row['genre'] == 'Children':
        colors.append('red')
    elif row['genre'] == 'Documentaries':
        colors.append('blue')
    elif row['genre'] == 'Stand-Up':
        colors.append('green')
    else:
        colors.append('black')

print(colors[:10])

plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12, 8))

plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration'], c=colors)

plt.title("Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

plt.show()

are_movies_getting_shorter = 'No'
