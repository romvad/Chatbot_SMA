from tkinter import *
from interface import Interface
import os
from requestHandler import RequestHandler
from requestHandlerCaller import ThreadRequestHandlerCaller

#Set up of the window et instanciation of the Interface class to define the general design
window = Tk()
window.geometry('{}x{}'.format(768, 576))
window.title("EISTI Chatbot - Alibek, Rémi, Romain")
interface = Interface(window)

#Instanciation of the requestHandler that contains the methods to get bot's response to the user's message
request_handler= RequestHandler()

def Enter_Or_Button_pressed(event):
    """ Implementation of the listener on the send button and on the "enter" key, touched when the user send a message """
    #We store the user's message into a variable
    input_get = interface.input_field.get()
    
    #We display the bot typing notification
    interface.typing_notification["text"]=interface.typing_notification_text
    
    #We reset the text field where the user types his message
    interface.input_user.set('')
    
    #We instantly display the user's message in the conversation window with the correct label 
    interface.writeOnConversationFrame(input_get,"user")
    
    #We instanciate the thread that manages the bot response (we use a thread in order not to bloch either the display of the user's message or the display of the notification
    caller=ThreadRequestHandlerCaller(request_handler,interface,input_get)
    caller.start()
    
    return "break"

#Set up of the listener
interface.input_field.bind("<Return>", Enter_Or_Button_pressed)
interface.b.bind("<Button-1>", Enter_Or_Button_pressed)

window.mainloop()