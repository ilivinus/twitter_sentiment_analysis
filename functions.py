import csv
import re


def twitter():
    tweets = []
    with open('elonmusk_tweets.csv',mode='r') as musk_tweets:
        csv_reader = csv.DictReader(musk_tweets,delimiter=',')
        line_count = 0
        for row in csv_reader:
            if(line_count == 0):
                line_count += 1
            else:
                tweets.append(row)
                line_count +=1
    return tweets

def clean(x):
    x = re.sub(r'^RT[\s]+', '', x)
    x = re.sub(r'https?:\/\/.*[\r\n]*', '', x)
    x = re.sub(r'#', '', x)
    x = re.sub(r'b"','',x)
    x = re.sub(r'b\'','',x)
    x = re.sub(r'@[A-Za-z0–9]+', '', x) 
    return x


def ratio(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1
