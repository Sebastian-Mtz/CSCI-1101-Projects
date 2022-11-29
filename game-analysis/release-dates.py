import pandas as pd
import matplotlib.pyplot as pot

df = pd.read_csv("game-ratings-by-release-dates.csv")

# Cleaning up data
df["first_release_date"] = pd.to_datetime(df["first_release_date"])

#Analyze data through visualization
pot.scatter(df["first_release_date"], df["critic_rating_value"], color = "blue", label = "critic ratings")
pot.scatter(df["first_release_date"], df["user_rating_value"], color = "red", label = "user ratings")


pot.legend(loc = "upper left")

pot.show()


