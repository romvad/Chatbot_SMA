# Chatbot_SMA
The project is composed of the cloud service and the desktop client

#Desktop client

#Cloud Server
The cloud server applies LDA (Latent Dirichlet Allocation) to the open source tweeter dataset with 16 topics. 
After clustering all the documents in the topics the newly generated dataset is used as the training set for text classifier. 
The classification part reproduces the steps listed in the Microsoft's tutorial (https://gallery.azure.ai/Experiment/Text-Classification-Step-1-of-5-data-preparation-3). 
The model has been trained using the ngram feature hashing and gives the following result 
Overall accuracy
0.553335
Average accuracy
0.944167
Micro-averaged precision
0.553335
Macro-averaged precision
0.539218
Micro-averaged recall
0.553335
Macro-averaged recall
0.523317

After evaluation the trained model has been deployed as the web service that returns the potential topis of the user request. The client looks for the topic in the clusterized 
tweeter base and selects a random tweet having the same topic as the user's one. This tweet is considered to a response to the user.