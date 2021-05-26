import openai
import pandas as pd
import numpy as np
import tweepy
import webbrowser

# import plotly.express as px

'''
Uses OpenAI's GPT-3 to classify sentiment of tweets

1. Dev docs: https://beta.openai.com/docs/introduction
2. Dataset: https://www.kaggle.com/gpreda/all-covid19-vaccines-tweets
3. Strip out Countries: https://github.com/grammakov/USA-cities-and-states

TODO's:
1. Preprocessing
    - Link tweets to a specific vaccine
    - Decide what to do about #'s and @'s (thinking remove #'s + text
    after and just strip out @'s)
    - Remove scraping realated characters (\n, etc.)

2. Model Run
    - Run

3. Postprocessing
    - Output .csv will have sentiments mapped to each but need to decide
    what to visualize
'''

openai.api_key = open('./GPT_SECRET_KEY.txt', 'r').readline().rstrip()

df = pd.read_csv('./vaccination_all_tweets.csv')

# strip out non-us tweets
cities_file = open('./us_cities_states_counties.csv', 'r')
states_list = set()

for line in cities_file:
    abrev = "".join(line.split("|")[1:2]).lower()

    if len(abrev) == 2:
        states_list.add(abrev)

states_list = list(states_list)

to_drop = []
for idx, row in df.iterrows():
    try:
        curr = row["user_location"].lower().split(" ")[-1]
        if curr not in states_list and curr[:3] != "usa" and curr != "america":
            to_drop.append(idx)

    except:
        to_drop.append(idx)

print(len(df) - len(to_drop))
df = df.drop(to_drop)
print(len(df))

# get tweet string from link if the whole string is not included
twitter_consumer_key = open('./TWITTER_KEY.txt', 'r').readline().rstrip()
twitter_consumer_secret = open('./TWITTER_SECRET_KEY.txt', 'r').readline().rstrip()

callback_uri = 'oob'
auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url()
webbrowser.open(redirect_url)

user_pint_input = input("Pin? ")
auth.get_access_token(user_pint_input)
api = tweepy.API(auth)

to_drop = []

for idx, row in df.iterrows():
    curr = row["id"]
    try:
        tweet = api.get_status(curr, tweet_mode="extended")
        print(tweet.full_text)
        df.at[idx,"text"] = tweet.full_text
    except:
        to_drop.append(idx)

print(len(df) - len(to_drop))
df = df.drop(to_drop)
print(len(df))

df.to_csv('./data.csv')


# df["sentiment"] = ""
# df["clssification"] = ""
#
# # remove .head() when we run for real...
# for idx, row in df.head().iterrows():
#     if row["text"] != np.nan:
#         data = " ".join(row["text"].split(" ")[:-1])
#         sentiment_json = openai.Classification.create(
#             model="davinci",
#             query=data,
#             labels=["Positive", "Negative", "Neutral"],
#             examples=[["Happy and relieved to have the #PfizerBioNTech #Covidvaccine – amazing work from all at @MHRAgovuk and @NHSuk since it’s less than 2 weeks since CHM recommended that it be approved in the UK. #GetVaccinated!", "Positive"],
#             ["The trump administration failed to deliver on vaccine promises, *shocker* #COVIDIOTS #coronavirus #CovidVaccine", "Negative"],
#             ["Will you be taking the COVID-19 vaccine once available to you? #COVID19 #Pfizer #BioNTech #vaccine #PfizerBioNTech", "Neutral"]]
#         )
#         df.at[idx,"sentiment"] = sentiment_json["label"]
#         classification_json = openai.Classification.create(
#             model="davinci",
#             query=data,
#             labels=["Hopeful", "Fearful", "Neutral"],
#             examples=[["Finally, #vaccine started in all the EU. #vaccineday is truly historic bringing hope and relief to millions of people. Thanks to #EU for supporting it and buying it for us. 🙏 to #PfizerBioNTech #AstraZeneca #Moderna. Now, most people should do it for everyone to be safe. I will.", "Hopeful"],
#             ["And this is the state of the poor quality #Sinovac. Even friendly countries are scared about it", "Fearful"],
#             ["Will you be taking the COVID-19 vaccine once available to you? #COVID19 #Pfizer #BioNTech #vaccine #PfizerBioNTech", "Neutral"]]
#         )
#         df.at[idx,"classification"] = classification_json["label"]
# print(df["sentiment"].head())
# print(df["classification"].head())

# df.to_csv('./results.csv')
