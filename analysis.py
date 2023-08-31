import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# loads csv file 'Tracks' and stores an object of the dataset
df_tracks = pd.read_csv('C:\\Users\Administrator\\Documents\\damn! 4 years\\ukhad liya kuch\\SEM 4 projects\\Python\Data Analysis\\Tracks.csv')
# returns first 5 tracks from the dataset 'Tracks'
df_tracks.head()

# null values
pd.isnull(df_tracks).sum()

# gives all the rows and columns in the dataset with the total values and data type of the column
df_tracks.info()

# gives 10 least popular songs in the dataset
sorted_df = df_tracks.sort_values('popularity', ascending = True).head(10)
sorted_df

# descriptive staistics of each column in the dataset
df_tracks.describe().transpose()

# top 10 songs in the dataset which has popularity > 90
most_popular = df_tracks.query('popularity>90', inplace = False).sort_values('popularity',ascending = False)
most_popular[:10]

# converting string date to datetime format
df_tracks.set_index("release_date",inplace=True)
df_tracks.index=pd.to_datetime(df_tracks.index)
df_tracks.head()

# specifies the artist at the 18th row in the dataset
df_tracks[["artists"]].iloc[18]

# convert duration of milliseconds into seconds
df_tracks["duration"]= df_tracks["duration_ms"].apply(lambda x: round(x/1000))
df_tracks.drop("duration_ms", inplace=True, axis=1)

#checks the converted duration column for first 5 tracks
df_tracks.duration.head()

# visualisation 

# correlation map between all of the columns except for the columns 'key','mode','explicit' using a heatmap
corr_df=df_tracks.drop(["key","mode","explicit"],axis=1).corr(method="pearson")
plt.figure(figsize=(14,6))
heatmap=sns.heatmap(corr_df,annot=True,fmt=".1g",vmin=-1, vmax=1, center=0, cmap="inferno", linewidths=1, linecolor="Black")
heatmap.set_title("correlation HeatMap Between Variable")
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=90)

# sampling the overall dataframe by 0.4% 
sample_df = df_tracks.sample(int(0.004*len(df_tracks)))
print(len(sample_df))

# visualisation on the sample dataframe we have created above

# correlation between loudness and energy 
plt.figure(figsize=(10,6))
sns.regplot(data = sample_df, y = "loudness", x = "energy", color = "c").set(title = "Loudness vs Energy Correlation")

# correlation between popularity and acousticness
plt.figure(figsize=(10,6))
sns.regplot(data = sample_df, y = "popularity",x = "acousticness", color = "b").set(title = "Popularity vs Acousticness Correlation")

# converts string release_dates into years and stores the year of release in 'years'
df_tracks['dates']=df_tracks.index.get_level_values('release_date')
df_tracks.dates=pd.to_datetime(df_tracks.dates)
years=df_tracks.dates.dt.year

#distribution graph on total number of songs in each year
sns.displot(years,discrete=True,aspect=2,height=5 ,kind="hist").set(title="Number of songsper year")

# duration of songs over the years using barplot
total_dr = df_tracks.duration
fig_dims = (18,7)
fig, ax = plt.subplots(figsize=fig_dims)
fig = sns.barplot(x = years, y = total_dr, ax=ax, errwidth = False).set(title="Year vs Duration")
plt.xticks(rotation=90)

# duration of songs over the years using lineplot
# total_dr=df_tracks.duration
# sns.set_style(style = "whitegrid")
# fig_dims = (10, 5)
# fig, ax = plt.subplots(figsize=fig_dims)
# fig=sns.lineplot(x=years, y=total_dr,ax=ax).set(title="Year vs Duration")
# plt.xticks(rotation=60)

# loads csv file 'SpotifyFeatures' and stores an object of the dataset
df_genre=pd.read_csv('C:\\Users\\Administrator\\Documents\\damn! 4 years\\ukhad liya kuch\\SEM 4 projects\\Python\\Data Analysis\\SpotifyFeatures.csv')

# returns first 5 tracks from the dataset 'SpotifyFeatures'
df_genre.head()

# Duration of the songs in Different Genres using Barplot
plt.title("Duration of the songs in Different Genres")
sns.color_palette("rocket",as_cmap= True)
sns.barplot(y='genre', x='duration_ms', data=df_genre)
plt.xlabel("Duration in milli seconds")
plt.ylabel("Geners")

# Top 5 Genres by Popularity using Barplot
sns.set_style(style = "darkgrid")
plt.figure(figsize=(10,5))
famous = df_genre.sort_values("popularity", ascending = False).head(10)
sns.barplot(y='genre', x='popularity', data = famous).set(title="Top 5 Genres by Popularity")