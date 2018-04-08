# Chatbot_SMA

** CLIENT SIDE **
*Chatbot's interface launch*
Only one thing: you have to type the following command line to open the conversation interface:
- python path/to/chatbot-launch

The interface is made of:
- a window that successively display the user's messages et the bot's messages (one font-color for each);
- a text field in which the user types his message.

*Explanation of the functioning of the client slide of the application*
- The chatbot is launched by the execution of chatbot-launch.py. This program:
    - instanciates the Interface class that defines the UI design; 
    - instanciates the RequestHandler class, that is below described more in detail;
    - implements the listeners on the send button and the "enter" key;
    - takes charge of the display of the "My bot is typing..." notification between the sending od the user's message and the bot's response;
    - delete the typed text of the user text field ;
    - instantly display le sent user's message in the conversation window (by calling the writeOnConversationFrame function of the Interface instance) and **parallel** instanciates RequestHandlerCaller thread so that the retrieving of the bot's response doesn't block either the display of the user's message or the "My bot is typing ..." notification

- The file interface.py contains the Interface class, that is instanciated by chatbot-launch.py:
    - interface's general design is executed inside the __init__  method that is called during the instanciation of Interface class
    - Two methods are implemented:
        - writeOnConversationFrame, that takes the message to display and the agent (user or bot) that says this message, display the message with the corresponding label ("me" or "My bot")
        - colorLabel, that is systematically called by the writeOnConversationFrame method, sets the color of the messages according to their label

- The file requestHandler.py contains the RequestHandler class that is instanciated at the beginning of the chatbot-launch.py program. Here is the structure of this class:
    - the __init__ method retrieves the datagram containing all the possibles messages, each message being associated to one of the 16 topics  (two columns in the datagram: "text_column"(the message) and "topic"). This datagram is retrieved one time at the launch of the chatbot;
    - the getScoredTopics method, that send a request to the web service set up in the server side: the web service will compute the probabilities of correspondance for each topics and will return a JSON with all the probabilities. The method retrieves the value of "Scored Label" et return it.
    - the getFinalAnswer method, that is called with the topic as input, return a random message belonging to the topic from the datagram retrieved in the __init__ method;
    - the getResponseFromChatBot method, that is called with the user's message as input, successively calls the getScoredTopics method and the getFinalAnswer method in order to return the message of the bot

- the file requestHandlerCaller.py contains the ThreadRequestHandlerCaller class that extends Thread. This thread is instanciated by chatbot-launch.py as soon as the user sends his message, in order not to block the display of the messahe and the "My bot is typing..." notification. Here is its content:
    - This thread is instanciated with the interface and the requestHandler instances, as well as the message typed by the user (cf. the __init__ method);
    - in the run method, the getResponseFromChatBot method of the requestHandler instance is called, the returned bot message is written by calling the writeOnConversationFrame method of the interface instance and the text notification attribute is reset to "" to end the display of "My bot is typing..."

    