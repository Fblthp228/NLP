import numpy as np
import pandas as pd
import re
import nltk
import string

#  читаем наш датасетик
path_to_dataset = "/home/fblthp/PYNLP/NLP/AI/reviews.csv"
df = pd.read_csv(path_to_dataset, encoding='UTF8', sep="\t")
print("the data has been read")


def hatred_chars(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    url_pattern.sub(r'', string)
    #perenosi = re.compile(r'[\n\t]*')
    #perenosi.sub(r' ', string)
    #string = re.sub(r"[\n\t]+", " ", string) #почему-то не работает или плохо работает
    string = "".join(string.splitlines()) #такой способ удаления переносов сработал
    return emoji_pattern.sub(r'', string)
#passing the emoji function to 'text_rare'
df['review'] = df['review'].apply(hatred_chars)


#берём колонку с отзывами, ищем в ней отзывы без русских символов

reviews = df["review"]
#print(reviews)

ruski = re.compile('[а-яА-ЯёЁ]')

netu_ruskih = list()

for i in range(0,len(reviews)):
    #reviews[i].strip()
    #reviews[i] = re.sub(r"  ", " ", reviews[i])
    #reviews[i] = re.sub(r"\n", " ", reviews[i])
    #reviews[i] = re.sub(r"\t", " ", reviews[i])
    if(ruski.search(reviews[i]) == None):
        #print("***************************")
        #print(i)
        #print(reviews[i])
        netu_ruskih.append(i)

print(netu_ruskih[:10])
print(len(netu_ruskih))

ommitrevs = df.drop(netu_ruskih)
ommitrevs.to_csv('/home/fblthp/PYNLP/NLP/AI/ommited.csv',index = False, encoding = 'UTF8', sep = '\t')
print(len(df['review']))
print(len(ommitrevs['review']))




path_to_dataset = "/home/fblthp/PYNLP/NLP/AI/ommited.csv"
omitedf = pd.read_csv(path_to_dataset, encoding='UTF8', sep="\t")
print(df['review'][180:210])
print("****************")
print(omitedf['review'][180:210])