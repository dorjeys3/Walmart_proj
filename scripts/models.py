
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt



# functions for modeling
def model_metrics(y_test, y_pred):

    '''Shows Accuracy, Precision, Recall, and F1-Score evaluation metrics'''

    print('Evaluation Metrics:')
    print('Accuracy: ' + str(metrics.accuracy_score(y_test, y_pred)))
    print('Precision: ' + str(metrics.precision_score(y_test, y_pred)))
    print('Recall: ' + str(metrics.recall_score(y_test, y_pred)))
    print('F1: ' + str(metrics.f1_score(y_test, y_pred)));


def cross_validation(model, X_tarin, y_train, cv=10, n_jobs=-1):
    '''Prints cross-validation metrics for evaluation'''

    score = cross_val_score(model, X_tarin, y_train, cv=cv, scoring = "f1", n_jobs=n_jobs)
    print('Cross-Validation F1 Scores:', score)
    print('Mean F1 Scores: ', round(score.mean(), 5))
    print('Standard Deviation:',  round(score.std(), 5));


def con_mat(y_test, y_pred, title=None):
    '''Plots the confusion_matrix'''

    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize = (6,4))
    sns.heatmap(cm, annot=True, fmt='d', ax=ax, cmap='Blues')
    plt.title(title, fontsize = 20)
    ax.set_xticklabels(['Not Rec', 'Rec'], fontsize=12)
    ax.set_yticklabels(['Not Rec', 'Rec'], fontsize=12)
    ax.set_ylabel('Actual', size=15)
    ax.set_xlabel('Predicted', size=15)
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom + 0.5, top - 0.5)
    return plt.show();


def get_coef_name(fit_model, df):
    '''Creates a sorted list of coefficients'''
    temp = (list(zip(fit_model.coef_[0], df.columns)))
    return sorted(temp,key = lambda x: x[0], reverse=True)


def get_feats_name(fit_model, df):
    '''Creates a sorted list of feature importances'''
    temp = (list(zip(fit_model.best_estimator_.feature_importances_, df.columns)))
    return sorted(temp,key = lambda x: x[0], reverse=True)
