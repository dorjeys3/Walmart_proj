# all fucntions for the projects live here


# for processing noisy contineous values
def convertor(x):
    '''Converts string to a list and returns index 0'''
    #used to clean raw price column and num_rating column
    x = list(x.split(" "))
    return x[0]


def remove_perc(x):
     '''Converts string to a list and returns index 0'''
    #used to clean raw price column and num_rating column
    x = list(x.split("%"))
    return x[0]

def remove_dollar(x):
    x = list(x.split("$"))
    return x[1]


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

def fdist(df, column):
    corpus = " ".join([" ".join(text) for text in df[column].to_list()])
    corpus = tokenize(corpus)
    fdist=FreqDist(corpus)
    print(f"Number of words in corpus: {len(fdist)}")
    fdist.plot(20);
