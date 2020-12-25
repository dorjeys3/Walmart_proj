import pandas as pd
import numpy as np
import re
import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import OneHotEncoder
import gensim
from gensim import corpora, models

lemmatizer = nltk.stem.WordNetLemmatizer()
stop_words=list(set(stopwords.words("english")))
eda_words = list(set(stopwords.words("english")))
eda_stopwords = ["color", "size", "fit", "great", "pair", "right", "x",
"xl", "nd", "de", "u", "la", "tbw", "c", "v", "great", "n", "wal", "wow",
"hi", "hello", "nmbc", "youll", "must", "said", "either", "lol", 'ill',
"six", "goat", "thou", "un", "lb", "pair", "right", "x", "xl", "one",
"way", "definitely", "shirt", "jacket", "daughter", "son" ]
eda_words.extend(eda_stopwords)


# for processing string values
def clean_text(text):
    text.replace("\\n"," ")
    text =  ' '.join(re.sub("([^A-Za-z])"," ",text).split())
    return text.lower()


def tokenize(text):
    return nltk.word_tokenize(text)

def remove_stopwords(text):
    stop_words=list(set(stopwords.words("english")))
    return [word for word in text if word not in stop_words]

def remove_eda_stopwords(text):
    stop_words=list(set(stopwords.words("english")))
    return [word for word in text if word not in eda_words]

def lemmatize_text(text):
    return [lemmatizer.lemmatize(word) for word in text]


def list_to_str(text):
    return ", ".join(text)

def coded_encoder(df, column):
    encoder = OneHotEncoder(handle_unknown="error", drop="first" )
    coded_cat=pd.DataFrame(encoder.fit_transform(df[[column]]).toarray())
    coded_cat.rename(columns={0:"girls'", 1:"men's", 2:"women's"},inplace=True)
    df.drop(columns = column, inplace=True)
    return coded_cat
