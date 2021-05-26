# Tweet Sentiment using GPT-3

1. Dev docs: https://beta.openai.com/docs/introduction
2. Dataset: https://www.kaggle.com/gpreda/all-covid19-vaccines-tweets
3. Strip out Countries: https://github.com/grammakov/USA-cities-and-states

You will probably have to pip install: `openai`

### TODO's:
1. Preprocessing
    - ~~Strip out all non-US data from dataset~~
    - ~~Get entire tweet strings~~
    - Get rid of newlines, link to tweet
    - Link tweets to a specific vaccine: string match by vaccine name (pfizer, moderna, j&j, AZ) and use one-hot encoding basically every vaccine has a column in the DF and then 0 if not or 1 if present

2. Model Run
    - ~~Decide if we want to add some of our own training examples~~
    - ~~Run for other labels too (hopeful, fearful, neutral)~~

3. Postprocessing
    - Output .csv will have sentiments mapped to each but need to decide
    what to visualize
