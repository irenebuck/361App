# This is Microservice B - About The Game
# If the user requests info about the game, it explains the value of it.

import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8080")


about = ("\nABOUT\n*****\nEach summer, kids forget valuable information they learned in their prior school year.\n"
           "This program gives 2nd graders a chance to quiz themselves throughout the summer break. \n"
           "When you return for 3rd Grade in the fall, you won't lose any time getting back in to \n"
           "the groove of school and your new teacher won't waste time refreshing you on words you \n"
           "already learned. \n\n"
           "It is recommended to run this program once a week throughout summer break. There are \n"
           "about 250 words in the program and it automatically stops when you reach 250 words read.\n\n")
    

while True:
    message = socket.recv_string()
    if message == 'show about':
        socket.send_string(about)
    else:
        continue