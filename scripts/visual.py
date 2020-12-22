
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.probability import FreqDist

def violin_plot(df, x_columns, y_columns, title=None,
 x_label=None, y_label=None, tick_labels = None):
    fig, ax = plt.subplots(figsize=(14,6))
    sns.violinplot(ax= ax, x=df[x_columns], y=df[y_columns])
    plt.title(title, fontsize=25)
    plt.xlabel(x_label, fontsize=15)
    plt.ylabel(y_label, fontsize=15)
    ax.set_yticklabels(ax.get_yticks(), size=12)
    if tick_labels:
        ax.set_xticklabels(tick_labels, size=12);

def bar_plot(x, y, data=None, hue=None,title=None, x_label=None, y_label=None):
    fig, ax= plt.subplots(figsize=(14,6))
    sns.barplot(x=x, y=y, hue=hue, data=data)
    plt.title(title, fontsize = 25)
    plt.xlabel(x_label, fontsize=15)
    plt.ylabel(y_label, fontsize=15);

def dist_plot(df, column, title=None, x_label=None, y_label=None):
    fig, ax = plt.subplots(figsize=(14,6))
    fig = sns.distplot(df[column])
    plt.title(title, fontsize=25)
    plt.ylabel(y_label, fontsize=15)
    plt.xlabel(x_label, fontsize=15);

def count_plot(df, column, title=None, x_label=None, y_label=None, tick_labels=None):
    fig, ax = plt.subplots(figsize=(14,6))
    fig = sns.countplot(x=df[column])
    plt.title(title, fontsize=25)
    plt.ylabel(y_label, fontsize=15)
    plt.xlabel(x_label, fontsize=15)
    if tick_labels:
        fig.set_xticklabels(tick_labels, fontsize = 10);

def fdist(df, column):
    corpus = " ".join([" ".join(text) for text in df[column].to_list()])
    corpus = tokenize(corpus)
    fdist=FreqDist(corpus)
    print(f"Number of words in corpus: {len(fdist)}")
    fdist.plot(20);
