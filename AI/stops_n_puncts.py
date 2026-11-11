import pandas as pd

path_to_dataset = "/home/fblthp/PYNLP/NLP/AI/lemmatized.csv"
df = pd.read_csv(path_to_dataset, encoding='UTF8', sep="\t")
print("the data has been read")

df['clear'] = ''
df['clear'] = df['lemm'].str.replace(r'\d+', '', regex=True) 
df['clear'].head()

from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('russian'))

def stopws(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])
# Применим функцию удаления стоп-слов
df["clear"] = df["clear"].apply(stopws)
print(df.head())

#удалим пунктуацию
df["clear"] = df["clear"].str.replace(r'[^\w\s]',' ', regex = True)
#df["clear"].head()

df.to_csv('/home/fblthp/PYNLP/NLP/AI/clear_d.csv',index = False, encoding = 'UTF8', sep = '\t')
