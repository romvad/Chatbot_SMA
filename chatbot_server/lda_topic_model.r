library(tm)
library(topicmodels)

dataset1 <- maml.mapInputPort(1) # class: data.frame

Encoding(dataset1$'text_column')  <- "UTF-8"

corp <- Corpus(VectorSource(c(dataset1$'text_column') ))
dtm <- DocumentTermMatrix(corp)
#convert rownames to filenames
rownames(dtm) <- dataset1$'tweet_id'
#Number of topics
k <- 16

#Run LDA using Gibbs sampling
ldaOut <-LDA(dtm,k, method="Gibbs")

ldaOutTerms <- as.data.frame(terms(ldaOut,20))
gammaDF <- as.data.frame(ldaOut@gamma)
names(gammaDF) <- names (ldaOutTerms)

# Now for each doc, find just the top-ranked topic   
toptopics <- data.frame(cbind(document = rownames(dtm), 
topic = apply(gammaDF,1,function(x) names(gammaDF)[which(x==max(x))])))

toptopics$topic <- sapply(toptopics$topic,function (x) paste(unlist(x), collapse = ';'))

toptopics$document <- sapply(toptopics$document,function (x) unlist(x)[1])

maml.mapOutputPort("toptopics");