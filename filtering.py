import glob
import os
import os.path
import sys
import csv 
import nltk
from nltk.tokenize import word_tokenize
import pandas as pd 

import csv



def filter_words():
    filter_words = ["Headache","Stomach","Flu","Fever","Nausea","Nauseous","Ill","Sick","Diarrhea","Pneumonia"]
    filtered_tweets = []
    with open('Microblogs.csv',encoding = "ISO-8859-1") as fp:
        for line in fp:
            for word in line.split():
                if word in filter_words:
                    filtered_tweets.append(line)

    df = pd.DataFrame(filtered_tweets)
    df.to_csv('filtered.csv', index=False, header=False)






filter_words()