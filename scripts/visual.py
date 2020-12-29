
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from wordcloud import WordCloud

from sklearn.metrics import confusion_matrix, plot_confusion_matrix


def tokenize(text):
    return nltk.word_tokenize(text)

def corr_plot(df):
    corr=df.corr()
    fig, ax = plt.subplots(figsize=(14,6))
    sns.heatmap(corr, cmap='RdBu', vmin=-1,vmax=1);


def violin_plot(df, x_columns, y_columns, title=None,
 x_label=None, y_label=None, tick_labels = None):
    fig, ax = plt.subplots(figsize=(14,6))
    sns.violinplot(ax= ax, x=df[x_columns], y=df[y_columns])
    plt.title(title, fontsize=25)
    plt.xlabel(x_label, fontsize=20)
    plt.ylabel(y_label, fontsize=20)
    ax.set_yticklabels(ax.get_yticks(), size=15)
    if tick_labels:
        ax.set_xticklabels(tick_labels, size=15);

def bar_plot(x, y, data=None, hue=None,title=None,
 x_label=None, y_label=None, tick_labels = None):
    fig, ax= plt.subplots(figsize=(14,6))
    sns.barplot(x=x, y=y, hue=hue, data=data)
    plt.title(title, fontsize = 25)
    plt.xlabel(x_label, fontsize=20)
    plt.ylabel(y_label, fontsize=20)
    ax.set_yticklabels(ax.get_yticks(), size=15)
    if tick_labels:
        ax.set_xticklabels(tick_labels, size=15);

def dist_plot(df, column, title=None, x_label=None, y_label=None):
    fig, ax = plt.subplots(figsize=(14,6))
    fig = sns.distplot(df[column])
    plt.title(title, fontsize=25)
    plt.ylabel(y_label, fontsize=20)
    plt.xlabel(x_label, fontsize=20)
    ax.set_xticklabels(ax.get_xticks(), size=15)
    ax.set_yticklabels(ax.get_yticks(), size=15);

def count_plot(df, column, title=None, x_label=None, y_label=None, tick_labels=None):
    fig, ax = plt.subplots(figsize=(14,6))
    fig = sns.countplot(x=df[column])
    plt.title(title, fontsize=25)
    plt.ylabel(y_label, fontsize=20)
    plt.xlabel(x_label, fontsize=20)
    ax.set_yticklabels(ax.get_yticks(), size=15)
    if tick_labels:
        fig.set_xticklabels(tick_labels, fontsize = 15);

def fdist(df, column):
    corpus = " ".join([" ".join(text) for text in df[column].to_list()])
    corpus = tokenize(corpus)
    fdist=FreqDist(corpus)
    plt.figure(figsize=(10, 6))
    fdist.plot(20)
    print(f"Number of words in corpus: {len(fdist)}");

def neg_cloud(df, column):
    no_rec = df[df[column] == 0]
    no_rec_text = no_rec["lemma_words"].values
    no_rec_text = "".join(" ".join(word) for word in no_rec_text)
    fig, ax = plt.subplots(figsize=(12,17))
    wordcloud = WordCloud(max_words=100,collocations=False, width=1000, height=700, background_color="lightgray", random_state=0).generate(no_rec_text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Wordcloud for Non Recommended items", fontsize = 35)

def pos_cloud(df, column):
    yes_rec = df[df[column] == 1]
    yes_rec_text = yes_rec["lemma_words"].values
    yes_rec_text = "".join(" ".join(word) for word in yes_rec_text)
    fig, ax = plt.subplots(figsize=(12,17))
    wordcloud = WordCloud(max_words=100,collocations=False, width=1000, height=700, background_color="lightgray", random_state=0).generate(yes_rec_text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Wordcloud for Recommended items", fontsize = 35)

def con_mat(classifier, X, y, title=None):
    disp1 = plot_confusion_matrix(classifier, X, y, cmap=plt.cm.Blues)
    disp1.ax_.set_title(f"{title}")
    plt.show()
