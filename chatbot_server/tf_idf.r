# Map 1-based optional input ports to variables
dataset <- maml.mapInputPort(1) # class: data.frame
input.dictionary <- maml.mapInputPort(2) # class: data.frame
##################################################
# Determine the following input parameters:-
# minimum length of a word to be included into the dictionary. 
# Exclude any word if its length is less than *minWordLen* characters.
minWordLen <- 3

# maximum length of a word to be included into the dictionary. 
# Exclude any word if its length is greater than *maxWordLen* characters.
maxWordLen <- 25
##################################################

# we assume that the text is the second column in the input data frame
topic <- dataset[[2]]
document <- dataset[[1]]

# Contents of optional Zip port are in ./src/
source("src/text.preprocessing.R");
data.set <- calculate.TFIDF(document, input.dictionary, 
	minWordLen, maxWordLen)
data.set <- cbind(topic, data.set)

#data.set <- as.data.frame(cbind(topic, document))

# Select the document unigrams TF-IDF matrix to be sent to the output Dataset port
maml.mapOutputPort("data.set")