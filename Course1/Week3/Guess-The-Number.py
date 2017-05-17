# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

reset = 1;
secret_number = 0;
num_of_guess = 0;


# helper function to start and restart the game
def new_game(range):
    # initialize global variables used in your code here
    global reset;
    global secret_number;
    global num_of_guess;

    if (range == 1000):
        print "****New Game starts with Range [0,1000)****\n";
        num_of_guess = 10;
        reset = 0;
        secret_number = random.randrange(0, 1000);
        print "Number of Remaining Guesses is", num_of_guess;
    elif (range == 100):
        print "****New Game starts with Range [0,100)****\n";
        num_of_guess = 7;
        reset = 1;
        secret_number = random.randrange(0, 100);
        print "Number of Remaining Guesses is", num_of_guess;
    # print secret_number;
    print "\n";


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    print "The Game Range has been changed to Range[0,100)";
    new_game(100);


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    print "The Game Range has been changed to Range[0,1000)";
    new_game(1000);


def input_guess(guess):
    # main game logic goes here
    guess = int(guess);
    global num_of_guess;
    print "Guess was", guess
    if (guess > secret_number):
        num_of_guess = num_of_guess - 1;
        print "Number of Available Guesses is", num_of_guess;
        print "Lower\n";
        if (num_of_guess == 0):
            print "Game Lost,Zero guesses available";
            if (reset == 0):
                new_game(1000);
            else:
                new_game(100);
    elif (guess < secret_number):
        num_of_guess = num_of_guess - 1;
        print "Number of Available Guesses is", num_of_guess;
        print "Higher\n";
        if (num_of_guess == 0):
            print "Game Lost,Zero guesses available";
            if (reset == 0):
                new_game(1000);
            else:
                new_game(100);
    else:
        num_of_guess = num_of_guess - 1;
        print "Number of Available Guesses is", num_of_guess;
        print "Correct\n";
        if (reset == 0):
            new_game(1000);
        else:
            new_game(100);


# create frame
frame = simplegui.create_frame("Guess the number Game", 250, 250);
frame.add_input("Enter the number", input_guess, 100);
frame.add_button("RANGE [0,100)", range100);
frame.add_button("RANGE [0,1000)", range1000);

# register event handlers for control elements and start frame
frame.start();

# call new_game
new_game(100);


# always remember to check your completed program against the grading rubric

