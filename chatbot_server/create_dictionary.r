# Map 1-based optional input ports to variables
dataset <- maml.mapInputPort(1) # class: data.frame
##################################################
# Determine the following input parameters:-
# minimum length of a word to be included into the dictionary. 
# Exclude any word if its length is less than *minWordLen* characters.
minWordLen <- 3

# maximum length of a word to be included into the dictionary. 
# Exclude any word if its length is greater than *maxWordLen* characters.
maxWordLen <- 25

# minimum document frequency of a word to be included into the dictionary. 
# Exclude any word if it appears in less than *minDF* documents.
minDF <- 9

# maximum document frequency of a word to be included into the dictionary. 
# Exclude any word if it appears in greater than *maxDF* documents.
maxDF <- Inf
##################################################
# we assume that the text is the second column in the input data frame
document <- dataset[[1]]

# Contents of optional Zip port are in ./src/
source("src/text.preprocessing.R");

# the output dictionary includes each word, its DF and its IDF
input.voc <- create.vocabulary(document, minWordLen, 
	maxWordLen, minDF, maxDF)
 
# the output dictionary includes each word, its DF and its IDF 
data.set <- calculate.IDF (input.voc, minDF, maxDF)

# Select the dictionary to be sent to the output Dataset port
maml.mapOutputPort("data.set")