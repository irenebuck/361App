# This is Microservice B - About The Game
# If the user requests info about the game, it explains the value of it.


about = ('''
ABOUT
*****
Each summer, kids forget valuable information they learned in their prior school 
year.This program gives 2nd graders a chance to quiz themselves throughout the
summer break. When you return for 3rd Grade in the fall, you won't lose any time 
getting back in to the groove of school and your new teacher won't waste time 
refreshing you on words you already learned. It is recommended to run this 
program once a week throughout summer break. There are about 20 words in the 
program and it automatically stops when you reach 20 words read.
''')
    

while True:
    with open('pipe.txt', 'r') as infile:
        message = infile.readline()
        if message == 'about info':
            with open('pipe.txt', 'w') as outfile:
                outfile.write(about)