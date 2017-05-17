# template for "Stopwatch: The Game"
import math
import simplegui


# define global variables
successcount = 0;
totalstopcount = 0;
count = 0;
T = True;
F = True;


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = str(t // 600);
    tem = (t // 10);
    tem = (tem) % 60;
    B = str(tem // 10);
    C = str(tem % 10);
    D = str(t % 10);
    return A + ":" + B + C + "." + D;


# define event handlers for buttons; "Start", "Stop", "Reset"
def stop():
    global successcount, totalstopcount, T;
    timer.stop();
    if (T == True):
        if (F == False):
            totalstopcount = totalstopcount + 1;
        T = False;
        if ((count % 10 == 0) and (count != 0)):
            successcount = successcount + 1;


def start():
    global T, F;
    T = True;
    F = False;
    timer.start();


def reset():
    global successcount, totalstopcount, count, F;
    count = 0;
    successcount = 0;
    totalstopcount = 0;
    F = True;


# define event handler for timer with 0.1 sec interval
def tick():
    global count;
    count = count + 1;


# define draw handler
def draw(canvas):
    global count;
    canvas.draw_text(format(count), [250, 250], 40, "red");
    canvas.draw_text(str(successcount) + "/" + str(totalstopcount), [400, 100], 30, "orange");


# create frame
frame = simplegui.create_frame("Stopwatch", 500, 500);
frame.add_button("START", start);
frame.add_button("STOP", stop);
frame.add_button("RESET", reset);

# register event handlers
frame.set_draw_handler(draw);
timer = simplegui.create_timer(100, tick)

# start frame
frame.start();

# Please remember to review the grading rubric

