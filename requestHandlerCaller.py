from threading import Thread

class ThreadRequestHandlerCaller(Thread):

    def __init__(self,request_handler,interface,input):
        Thread.__init__(self)
        self.request_handler=request_handler
        self.interface=interface
        self.input=input
    
    def run(self):
        print(self.input)
        answer=self.request_handler.getResponseFromChatBot(self.input)
        #print("answer" +answer)
        self.interface.writeOnConversationFrame(answer,"bot")
        self.interface.typing_notification["text"]=""