import pandas as pd
import matplotlib.pyplot as pot

df = pd.read_csv("game-ratings-by-top-10-genres.csv")

#Group by metrics
df_follow = df.groupby(["genre_name"])["follow_count"].sum().reset_index()

df_follow = df_follow.rename(columns = {"follow_count" : "total_follows"})

df_hype = df.groupby(["genre_name"])["hype_count"].sum().reset_index()

df_hype = df_hype.rename(columns = {"hype_count" : "total_hypes"})

#Analyze Data through visualization
bar_width = .4

pot.bar(df_follow.index - bar_width / 2, df_follow["total_follows"], color = "blue", label = "number of follows", width = bar_width)

pot.bar(df_hype.index + bar_width / 2, df_hype["total_hypes"], color = "red", label = "number of hypes", width = bar_width)

pot.xticks(df_follow.index, df_follow["genre_name"])

pot.legend(loc = "upper left")

pot.show()
