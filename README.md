# Tweet Sentiment using Pre-Trained RoBERTa 
### Also includes GPT-3 Sentiment analsyis Script
### Ari Chadda, Nina Herman, Matt Schnell

0. Pre-Trained Models: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment, https://huggingface.co/cardiffnlp/twitter-roberta-base-emotion
1. Dev docs: https://beta.openai.com/docs/introduction
2. Dataset: https://www.kaggle.com/gpreda/all-covid19-vaccines-tweets
3. Strip out Countries: https://github.com/grammakov/USA-cities-and-states

Sentiment analysis of ~10K U.S. COVID-19 Vaccine tweets using pre-trained RoBERTa models hosted by HuggingFace. Scripts for pre-processing data, running the model, and graphing outputs can be found in `tweet_sentimet.ipynb`. 

We also wrote a script for GPT-3 to perform the same analysis using OpenAI's API, but the analsyis was beyond our economic means for this project which can be found in `tweet_sentiment.py`. 

You will need your own `tweepy` API key and/or `OpenAI` API key to run portions of this project. You can also simply use the `data.csv` or `finalfinalscores.csv` and pickup where those files are loaded in `tweet_sentimet.ipynb`.
