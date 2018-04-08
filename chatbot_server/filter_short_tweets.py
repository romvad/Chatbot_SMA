# imports up here can be used to 
import pandas as pd

# The entry point function:
#   Param<dataframe1>: preprocessed and filtered comments
def azureml_main(dataframe1, dataframe2 = None):
    #filter out empty reviews
    #column containg the number of tokens in the 'text_column' column
    num_tokens = [len(str(avis).split()) for avis in dataframe1['text_column']]
    #add the generated token array as a new column
    dataframe1['Tokens'] = num_tokens
    #leave only comments having at least 3 tokens after preprocessing
    output = dataframe1.loc[dataframe1['Tokens'] > 2]
    #remove tokens column
    output = output.drop(['Tokens'], axis = 1)
    return output
