# Map 1-based optional input ports to variables
dataset1 <- maml.mapInputPort(1) # class: data.frame

dataset1$tweet_id <- seq(1, nrow(dataset1))

maml.mapOutputPort("dataset1");