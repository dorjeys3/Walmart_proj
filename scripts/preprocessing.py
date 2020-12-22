# for processing string values
def clean_text(text):
    text.replace("\\n"," ")
    text =  ' '.join(re.sub("([^A-Za-z \t])"," ",text).split())
    return text.lower()

def tokenize(text):
    return nltk.word_tokenize(text)

def remove_stopwords(text):
    return [word for word in text if word not in stop_words]

def lemmatize_text(text):
    return [lemmatizer.lemmatize(word) for word in text]
