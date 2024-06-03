import pyttsx3
import random
import time
import zmq


def say_word(seconds, engine, word):
    """Reads the sight word aloud"""
    time.sleep(seconds)
    engine.say(word)
    engine.runAndWait()


def title():
    """Displays the program title at initial opening of program"""
    print("""

  _____  _           ___  _        _    _    __      __             _ 
 |_   _|| |_   ___  / __|(_) __ _ | |_ | |_  \ \    / /___  _ _  __| |
   | |  | ' \ / -_) \__ \| |/ _` || ' \|  _|  \ \/\/ // _ \| '_|/ _` |
   |_|  |_||_|\___| |___/|_|\__, ||_||_|\__|   \_/\_/ \___/|_|  \__,_|
             ___  _         |___/_                                    
            / __|| |_   __ _ | || | ___  _ _   __ _  ___              
           | (__ | ' \ / _` || || |/ -_)| ' \ / _` |/ -_)             
            \___||_||_|\__,_||_||_|\___||_||_|\__, |\___|             
                                              |___/                   
    """)


def opening_message():
    """Displays the reason the user may use the program"""
    print("Practice your 2nd Grade sight words!")


def display_options():
    print("COMMANDS:\n"
        "Enter   Hit the Enter key to start the Sight Word game! \n"
        "a       Type a then hit Enter to hear more about this program.\n"
        "c       Type c then hit Enter to check how many times this program has been used.\n"
        "t       Type t then hit Enter to take more time on each word before it is said aloud.\n"
        "q       Type q anytime to exit the program. \n")


def warning():
    """Warns the user about the noise the program creates."""
    print ("WARNING : Check your volume setting.\n"
           "This program displays a word, then says the word aloud after 3 seconds.\n")



def command_entered(socket):
    """
    Parameter: receives a socket for sending and receiving strings.
    This function takes input from user about which feature of the program they want to use
    """
    entry = input('What do you want to do? ')
    if entry == 't':
        socket.send_string('get seconds')
        response = int(socket.recv_string())
        one_game(response)
    elif entry == 'a':
        socket.send_string('show about')
        message = socket.recv_string()
        print(message)
        command_entered(socket)
    elif entry == 'c':
        socket.send_string('show count')
        count = socket.recv_string()
        print(count)
        command_entered(socket)
    elif entry == '':
        one_game(3)
    elif entry == 'q':
        print("Goodbye!")
    else:
        command_entered(socket)


def read_file():
    """Opens and reads the words in words.txt file"""
    with open("words.txt", "r") as infile:
        words = infile.readlines()
    return words


def random_int(num_of_words):
    """ 
    Parameter: integer that is the total number of words in the words.txt file
    Returns: a random integer between 0 and the number of words - 1 in the words.txt file
    """
    rando = random.randint(0, num_of_words - 1)
    return rando


def get_word(word_list, num_of_words):
    """
    Params: list of words, a count of the number of words in the list of words
    Calls random_int to create a random integer, then returns the word at that index in the list
    """
    index = random_int(num_of_words)
    new_word = word_list[index]
    return new_word


def display_word(word_to_display, words_remaining):
    """
    :param word_to_display: word the user will see and hear read to them
    :param words_remaining:
    This function displays word and number of words remaining to finish the game.
    """
    print (f'\n'
           f'{word_to_display}\n'
           f'Words remaining: {words_remaining}'
           f'\n')


def one_game(seconds):
    """
    Parameter: number of seconds the user want to delay from seeing word to hearing it.
    This program plays through one game with either default 3-second delay or user's choice.
    Delay applies to time word appears on screen to when pyttsx3 module says it aloud.
    """
    engine = pyttsx3.init()
    count = 0
    words = read_file()
    number_of_words = len(words)
    choice = input("Press q to quit at anytime.")
    while count < number_of_words:
        new_word = get_word(words, number_of_words)
        display_word(new_word, number_of_words - count)
        say_word(seconds, engine, new_word)
        count += 1
        if count == 10:
            socket.send_string('log')
        if choice == 'q':
            socket.set_string('quit early')
            message = socket.recv_string()
            print(message)
            return
        else:
            continue
    socket.set_string('finished game')
    message = socket.recv_string()


if __name__ == "__main__":
    title()
    opening_message()
    warning()
    display_options()

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:8080")

    command_entered(socket)
