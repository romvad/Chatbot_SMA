import urllib.request
import json
from azureml import Workspace

class RequestHandler:

    def __init__(self):
        """ In the init method (called at the laucnh of the chabot, we retrieve the datagram containing all the possible responses of the bot and their related topic. """
        ws = Workspace(
        workspace_id='7b1591095a27421eb716eca8aa6a9f96',
        authorization_token='RvNpB8Nnr6EIQnwiwOCVRglAWsYk+kDnc6KLoxRn0/ex68i9azNE6Z+TRlBaLZI+vXsudFXeXmqyaqV0aSUb5Q==',
        endpoint='https://studioapi.azureml.net'
        )
        experiment = ws.experiments['7b1591095a27421eb716eca8aa6a9f96.f-id.11507323972c4a2db878aaf1d7bbef39']
        ds = experiment.get_intermediate_dataset(
        node_id='10448e92-eed8-4052-8072-319538e5855b-49687',
        port_name='Results dataset',
        data_type_id='GenericTSV'
        )
        self.frame = ds.to_dataframe()

    def getScoredTopics(self,text_input):
        """ Method that returns the topic with the higher probability according to the user's message, thanks to request to a web service """
        data = {
                "Inputs": {
                        "input1":
                        [
                            {
                                    'document': text_input,   
                            }
                        ],
                },
            "GlobalParameters":  {
            }
        }

        body = str.encode(json.dumps(data))

        url = 'https://ussouthcentral.services.azureml.net/workspaces/7b1591095a27421eb716eca8aa6a9f96/services/64d002daf84148a59fa3bb50b5fce69a/execute?api-version=2.0&format=swagger'
        api_key = '4Z9MDm5V3YxROdl0MykEHfgkXRSDMFrDtgH7z7IdseV4HhHic58hhCX7XvX9n1Qh7/IoiW/aFMAB9v8hSth4Ag=='
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib.request.Request(url, body, headers)

        try:
            response = urllib.request.urlopen(req)
            result = json.loads(response.readline().decode('utf-8'))
            scored_topics = result['Results']['output1'][0]['Scored Labels']
            
            return(scored_topics)
            
        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())
            print(json.loads(error.read().decode("utf8", 'ignore')))
            
    def getFinalAnswer(self,scored_topics):
        """ Method that return a random message for the topic passed in input parameter. This method is called after getting the topic with the higher probability"""
        
        tmp=self.frame.loc[self.frame['topic'] == scored_topics]
        tmp2=tmp.loc[:,'text_column']
        
        return tmp2.sample(n=1).item()

    def getResponseFromChatBot(self,text_input):
        """ This is the main method of this class. It first calls the getScoredTopics to get the most probable topic and then calls getFinalAnswer method in passing this topic in input parameter"""
        scored_topics=self.getScoredTopics(text_input)
        
        return self.getFinalAnswer(scored_topics)

