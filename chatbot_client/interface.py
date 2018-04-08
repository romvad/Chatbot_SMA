from tkinter import *
from tkinter.font import Font
import os

dirname = os.path.dirname(__file__)

class Interface(Frame):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        
        #Design of the conversation frame
        self.vsb=Scrollbar(fenetre)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.messages=Text(fenetre,wrap=WORD,yscrollcommand=self.vsb.set)
        self.messages.pack()
        self.vsb.config(command=self.messages.yview)    
        
        #Definition of the notification below the conversation frame
        self.typing_notification_text="My bot is typing..."
        self.typing_notification=Label(fenetre,text="")
        self.typing_notification.pack()
        
        #Design of the text field user input and send button
        container = Frame(fenetre, background="#ffd3d3")
        self.b=Button()
        file_picture=os.path.join(dirname, 'send5.png')
        self.send_picture=PhotoImage(file=file_picture)
        self.b.config(image=self.send_picture,width="50",height="50",background="#48ea5b")
        self.input_user = StringVar()
        self.input_field = Entry(fenetre, text=self.input_user)
        self.input_field.pack(in_=container, side="left")
        self.b.pack(in_=container, side="right")
        container.pack(side=BOTTOM, fill=X)
        self.pack()
        
        #Definition of the tags corresponding the user's message and the bot's message for the font-color
        self.messages.tag_configure("user_label", foreground="orange")
        self.messages.tag_configure("bot_label", foreground="red")

    def writeOnConversationFrame(self,message,agent):
        """ Method that writes user's message or bot's message according to 'agent' input parameter. For a user message, chatbot-launch.py calls this method.
        For a bot message, the requestHandlerCaller thread calls this method """
        
        if agent=="user":
            displayed_message="me: "+message
            self.messages.insert(INSERT, '%s\n' % displayed_message)
            self.colorLabel()
        
        if agent=="bot":
            displayed_message="My bot: "+message
            self.messages.insert(INSERT, '%s\n' % displayed_message)
            self.colorLabel()
        
        
    
    def colorLabel(self):
        """ Method that set up the correct label for the correct message. Called at each call of writeOnConversationFrame method. """
        
        lastline = self.messages.index("end-1c").split(".")[0]
        tag = "user_label"
        for i in range(1, int(lastline)):
            self.messages.tag_add(tag, "%s.0" % i, "%s.0" % (i+1))
            tag = "bot_label" if tag == "user_label" else "user_label"