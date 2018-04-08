from threading import Thread

class ThreadRequestHandlerCaller(Thread):

    """ This thread is called by the chatbot-launch.py program. It permits to compute the bot's response without blocking the evolution of the UI (display of user's message...)"""

    def __init__(self,request_handler,interface,input):
        Thread.__init__(self)
        self.request_handler=request_handler
        self.interface=interface
        self.input=input
    
    def run(self):
        
        #We get the bot's answer
        answer=self.request_handler.getResponseFromChatBot(self.input)
        
        #We display the bot's answer in the conversation window
        self.interface.writeOnConversationFrame(answer,"bot")
        
        #We hide the "My bot is typing..." notification
        self.interface.typing_notification["text"]=""