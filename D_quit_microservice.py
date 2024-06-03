# This is Microservice D - Quit
# The user enters q to end the program. 

import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8080")


teacher_message ="Great job! I'm so proud of you!\n" 
"Practicing your sight words every week will help you stay ready for 3rd Grade.\n\n"
"I miss seeing your sweet face everyday. Enjoy your summer break and see you back here next week! \n\n"
"Love,\n\n"
"Mrs. Lake"


while True:
    message = socket.recv_string()
    if message == 'quit early':
        socket.send_string('Goodbye!')
    elif message == 'finished game':
        socket.send_string(teacher_message)
    else:
        continue
