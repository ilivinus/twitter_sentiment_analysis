import tweet as tw

import matplotlib.pyplot as plt
import functions as fn

tw.df['analysis'] = tw.df['polarity'].apply(fn.ratio)
tw.df['analysis'].value_counts().plot(kind='bar')
plt.show()