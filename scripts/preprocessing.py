import re
import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = nltk.stem.WordNetLemmatizer()
# for processing string values
def clean_text(text):
    text.replace("\\n"," ")
    text =  ' '.join(re.sub("([^A-Za-z \t])"," ",text).split())
    return text.lower()

def tokenize(text):
    return nltk.word_tokenize(text)

def remove_stopwords(text):
    stop_words=list(set(stopwords.words("english")))
    return [word for word in text if word not in stop_words]

def lemmatize_text(text):
    return [lemmatizer.lemmatize(word) for word in text]
