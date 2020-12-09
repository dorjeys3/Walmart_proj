# all fucntions for the projects live here


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

cleaning_df["price"]= cleaning_df["price"].apply(remove_dollar)
