from tkinter import *
from interface import Interface
import os
from requestHandler import RequestHandler
from requestHandlerCaller import ThreadRequestHandlerCaller

window = Tk()
#messages=Text(window)
#messages.pack()
window.geometry('{}x{}'.format(768, 576))
window.title("EISTI Chatbot - Alibek, Rémi, Romain")
interface = Interface(window)
request_handler= RequestHandler()

def Enter_Or_Button_pressed(event):
    input_get = interface.input_field.get()
    print(input_get)
    interface.typing_notification["text"]=interface.typing_notification_text
    #interface.messages.insert(INSERT, '%s\n' % input_get)
    ##label = Label(window, text=input_get)
    interface.input_user.set('')
    interface.writeOnConversationFrame(input_get,"user")
    #request_handler= RequestHandler()
    #answer=request_handler.getResponseFromChatBot("My bonnie lies over the ocean")
    #answer=request_handler.getResponseFromChatBot(input_get)
    #print("answer" +answer)
    #interface.writeOnConversationFrame(answer,"bot")
    caller=ThreadRequestHandlerCaller(request_handler,interface,input_get)
    caller.start()
    #interface.typing_notification_text=""
    #interface.typing_notification["text"]=""
    #label.pack()
    return "break"

#interface = Frame(window)  # , width=300, height=300)
interface.input_field.bind("<Return>", Enter_Or_Button_pressed)
interface.b.bind("<Button-1>", Enter_Or_Button_pressed)
#interface.pack()
window.mainloop()


# ##########


