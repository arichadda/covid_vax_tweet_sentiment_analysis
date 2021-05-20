import openai
import json
import pandas as pd
import numpy as np
# import plotly.express as px

'''
Uses OpenAI's GPT-3 to classify sentiment of tweets

1. Dev docs: https://beta.openai.com/docs/introduction
2. Dataset: https://www.kaggle.com/gpreda/all-covid19-vaccines-tweets
3. Strip out Countries: https://github.com/grammakov/USA-cities-and-states

You will probably have to pip install: `openai`

TODO's:
1. Preprocessing
    - Strip out all non-US data from dataset
    - Get entire tweet strings
    - Link tweets to a specific vaccine
    - Decide what to do about #'s and @'s (thinking remove #'s + text
    after and just strip out @'s)
    - Remove scraping realated characters (\n, etc.)

2. Model Run
    - Decide if we want to add some of our own training examples
    - Run for other labels too (hopeful, fearful, neutral)

3. Postprocessing
    - Output .csv will have sentiments mapped to each but need to decide
    what to visualize
'''

openai.api_key = open('./GPT_SECRET_KEY.txt', 'r').readline().rstrip()

df = pd.read_csv('./vaccination_all_tweets.csv')
df["sentiment"] = ""

# remove .head() when we run for real...
for idx, row in df.head().iterrows():
    if row["text"] != np.nan:
        data = " ".join(row["text"].split(" ")[:-1])
        response_json = openai.Classification.create(
            model="davinci",
            query=data,
            labels=["Positive", "Negative", "Neutral"],
            examples=[["The movie is so interesting.", "Positive"],
            ["It is quite awful.", "Negative"],
            ["It is okay.", "Neutral"]]
        )
        df.at[idx,"sentiment"] = response_json["label"]
print(df["sentiment"].head())

df.to_csv('./results.csv')
