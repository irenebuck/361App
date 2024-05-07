import pyttsx3
import random
import time


def say_word(engine, word):
    """Reads the sight word aloud"""
    time.sleep(3)
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


def openingMessage():
    """Reason the user may use the program"""
    print ("Practice your 2nd Grade sight words!")


def display_options():
    print  ("COMMANDS:\n"
           "Enter   Hit the Enter key to start the Sight Word game! \n"
           "a       Type a then hit Enter to hear more about this program.\n"
           "t       Type t then hit Enter to take more time on each word before it is said aloud.\n"
           "q       Type q then hit Enter to exit the program. \n")


def warning():
    """Warns the user about the noise the program creates."""
    print ("WARNING : Check your volume setting.\n"
           "This program displays a word, then says the word aloud after 3 seconds.\n")


def about():
    """Explains the purpose of the site"""
    print ("\nABOUT\n*****\nEach summer, kids forget valuable information they learned in their prior school year.\n"
           "This program gives 2nd graders a chance to quiz themselves throughout the summer break. \n"
           "When you return for 3rd Grade in the fall, you won't lose any time getting back in to \n"
           "the groove of school and your new teacher won't waste time refreshing you on words you \n"
           "already learned. \n\n"
           "It is recommended to run this program once a week throughout summer break. There are \n"
           "about 250 words in the program and it automatically stops when you reach 250 words read.\n\n")


def command_entered():
    prompt = "What do you want to do? "
    entry = input(prompt)
    if entry == 't':         # this is the equivalent of hitting enter
        command_entered()
        pass                # time extended for a stutterer
    elif entry == 'a':
        about()
        command_entered()
    elif entry == 'q':
        print ("Goodbye!")
    else:
        one_game()

def teacher_message():
    """ The user, a 2nd grade graduate, gets this message at the end of the program. It is from
    their 2nd grade teacher. """
    print ("Great job! I'm so proud of you!\n" 
           "Practicing your sight words every week will help you stay ready for 3rd Grade.\n\n"
           "I miss seeing your sweet face everyday. Enjoy your summer break and see you back here next week! \n\n"
           "Love,\n\n"
           "Mrs. Lake")


def read_file():
    """Opens and reads the words in words.txt file"""
    with open("words.txt", "r") as infile:
        words = infile.readlines()
    return words


def random_int(num_of_words):
    words = read_file()
    rando = random.randint(0, num_of_words)
    return rando


def get_word(word_list, num_of_words):
    index = random_int(num_of_words)
    new_word = word_list[index]
    return new_word


def display_word(word_to_display, words_remaining):
    print (f'\n'
           f'{word_to_display}\n'
           f'Words remaining: {words_remaining}'
           f'\n')


def one_game():
    count = 0
    words = read_file()
    number_of_words = len(words)
    while count != number_of_words:
        new_word = get_word(words, number_of_words)
        display_word(new_word, number_of_words)
        say_word(engine, new_word)
        count += 1
        number_of_words -= 1
    teacher_message()


if __name__ == "__main__":
    engine = pyttsx3.init()
    title()
    openingMessage()
    warning()
    display_options()
    command_entered()