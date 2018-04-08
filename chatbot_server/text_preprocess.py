import pandas as pd
import nltk
import string
import re
import sys 

# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(dataframe1, dataframe2 = None):
    #preparing replacement table for punctuation marks
    table = string.maketrans("","")
    #copy dataset that is returned by this module
    output = dataframe1
    #replacing punctutation
    output['text_column'] = output['text_column'].apply(lambda comment: str(comment).translate(table, string.punctuation))
    #switching to the lower case
    output['text_column'] = output['text_column'].apply(lambda comment: str(comment).lower())
    #removing words shorter than 3
    output['text_column'] = output['text_column'].apply(lambda comment: re.sub(r'\b\w{1,2}\b', '', str(comment)))
    return output