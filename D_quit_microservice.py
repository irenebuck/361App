# This is Microservice D - Quit
# The user enters q to end the program.


teacher_message = ("""
Great job! I'm so proud of you! 

Practicing your sight words every week will help you stay ready for 3rd Grade.
Enjoy your summer break and see you back here next week!

Love,
Mrs. Lake

""")


while True:
    with open('pipe.txt', 'r') as infile:
        message = infile.readline()
    if message == 'q':
        print("Goodbye!")
    elif message == 'get teacher message':
        with open('pipe.txt', 'w') as outfile:
            outfile.write(teacher_message)
    else:
        continue
