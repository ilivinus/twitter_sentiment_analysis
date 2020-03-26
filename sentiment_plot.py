import tweet as tw

import matplotlib.pyplot as plt
#visualization

plt.rcParams['figure.figsize'] = [10,8]

for index, Tweets in enumerate(tw.df.index):
    x = tw.df.polarity.loc[Tweets]
    y = tw.df.subjectivity.loc[Tweets]
    plt.scatter(x,y, color ="Red")

plt.title('Elon Musk Sentiment analysis', fontsize=20)
plt.xlabel('<- Negative ----------------Positive ->', fontsize=15)
plt.ylabel('<- Facts--------------------Opinions ->',fontsize=15)
plt.show()
