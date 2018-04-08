# The script MUST contain a function named azureml_main
# which is the entry point for this module.

# imports up here can be used to 
import pandas as pd

# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
docs = []
topics = []
def azureml_main(dataframe1, dataframe2 = None):
    for index, row in dataframe1.iterrows():
        docs.append (row['document'])
        topics.append(row['topic'].split(';')[0])
    output = pd.DataFrame({'document': docs, 'topic': topics})
    return output