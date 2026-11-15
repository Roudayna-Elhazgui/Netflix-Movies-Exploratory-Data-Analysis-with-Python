# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce 

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
movies_90s = netflix_df[
    (netflix_df["release_year"] >= 1990) &
    (netflix_df["release_year"] < 2000) &
    (netflix_df["type"] == "Movie")
]

# Find the most frequent movie duration
duration = int(movies_90s["duration"].mode()[0])

# Count short action movies (less than 90 minutes)
short_movie_count = len(
    movies_90s[
        (movies_90s["duration"] < 90) &
        (movies_90s["genre"] == "Action")
    ]
)

print(duration)
print(short_movie_count)
