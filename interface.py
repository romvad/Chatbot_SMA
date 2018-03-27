from tkinter import *
from tkinter.font import Font
import os

dirname = os.path.dirname(__file__)

class Interface(Frame):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.vsb=Scrollbar(fenetre)
        #container2 = Frame(fenetre)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.messages=Text(fenetre,wrap=WORD,yscrollcommand=self.vsb.set)
        #self.vsb = Scrollbar(self, command=self.messages.yview, orient="vertical")
        #self.messages.configure(yscrollcommand=self.vsb.set)
        #self.vsb.pack(side=RIGHT, fill=Y)
        self.messages.pack()
        self.vsb.config(command=self.messages.yview)    
        #self.messages.pack(side="left", fill="both", expand=True)
        
        self.typing_notification_text="My bot is typing..."
        self.typing_notification=Label(fenetre,text="")
        self.typing_notification.pack()
        
        container = Frame(fenetre, background="#ffd3d3")
        self.b=Button()
        file_picture=os.path.join(dirname, 'send5.png')
        self.send_picture=PhotoImage(file=file_picture)
        self.b.config(image=self.send_picture,width="50",height="50",background="#48ea5b")
        #self.b.pack(side=LEFT)
        self.input_user = StringVar()
        self.input_field = Entry(fenetre, text=self.input_user)
        #self.input_field.grid(row=0,column=0)
        self.input_field.pack(in_=container, side="left")
        #self.b.grid(row=0,column=1)
        self.b.pack(in_=container, side="right")
        container.pack(side=BOTTOM, fill=X)
        #self.input_field.pack(side=BOTTOM, fill=X)
        self.pack()
        #self.input_field.bind("<Return>", self.Enter_pressed)
        
        #Fonts
        #self.user_label_font=Font(weight="bold",color="#678345")
        #self.bot_label_font=Font(weight="bold",color="#278345")
        #self.normal_font=Font(weight="normal", color="#ffffff")
        self.messages.tag_configure("user_label", foreground="orange")
        self.messages.tag_configure("bot_label", foreground="red")

    def writeOnConversationFrame(self,message,agent):
        if agent=="user":
            displayed_message="me: "+message
            #self.messages.tag_delete("label")
            #self.messages.tag_add("label","current linestart","current linestart + 3 chars")
            #self.messages.tag_config("label",foreground="orange")
            self.messages.insert(INSERT, '%s\n' % displayed_message)
            self.colorLabel()
        
        if agent=="bot":
            displayed_message="My bot: "+message
            #self.messages.tag_delete("label")
            #self.messages.tag_add("label","current","current + 7 chars")
            #self.messages.tag_config("label",foreground="red")
            self.messages.insert(INSERT, '%s\n' % displayed_message)
            self.colorLabel()
        
        #self.input_user.set('')
    
    def colorLabel(self):
        lastline = self.messages.index("end-1c").split(".")[0]
        tag = "user_label"
        for i in range(1, int(lastline)):
            self.messages.tag_add(tag, "%s.0" % i, "%s.0" % (i+1))
            tag = "bot_label" if tag == "user_label" else "user_label"
###############

#messages = Text(window)
#messages.pack()
#b=Button(window, justify=LEFT)
#file_picture=os.path.join(dirname, 'send.png')
#send_picture=PhotoImage(file=file_picture)
#b.config(image=send_picture,width="10",height="10")
#b.pack(side=LEFT)
#input_user = StringVar()
#input_field = Entry(window, text=input_user)
#input_field.pack(side=BOTTOM, fill=X)

    #def Enter_pressed(event):
     #   input_get = input_field.get()
      #  print(input_get)
       # messages.insert(INSERT, '%s\n' % input_get)
        # label = Label(window, text=input_get)
    #    input_user.set('')
        # label.pack()
     #   return "break"

	#frame = Frame(window)  # , width=300, height=300)
	#input_field.bind("<Return>", Enter_pressed)
	#frame.pack()
	#window.mainloop()