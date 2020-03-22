import pandas as pd
import numpy as np
import textblob as TextBlob
import functions as fn

search = fn.twitter()
#converting into data frame
df = pd.DataFrame([tweet['text'] for tweet in search[:500]],columns=["Tweets"])
df.head(500)

#cleaning the tweets
df["Tweets"] = df["Tweets"].apply(fn.clean)

#sentiment analysis
polarity = lambda x: TextBlob.TextBlob(x).sentiment.polarity
subjectivity = lambda x : TextBlob.TextBlob(x).sentiment.subjectivity

df['polarity'] = df["Tweets"].apply(polarity)
df['subjectivity'] = df["Tweets"].apply(subjectivity)