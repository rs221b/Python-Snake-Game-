#Snake Game
import simplegui
import random
import time

#global variables
queue_x = [400, 395, 390, 385, 380, 375, 370, 365, 360, 355, 350]
queue_y = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250]
food_x = 100 
food_y = 100
height = 400
width = 600
pixel_size = 10
direction = "right"
speed = 0.05
score = 0

# key press
def keydown(key):
    global direction, speed
    if key==simplegui.KEY_MAP["down"] and (direction == 'left' or direction == 'right'):
        direction = 'up'
    elif key==simplegui.KEY_MAP["up"] and (direction == 'left' or direction == 'right'):
        direction = 'down'
    elif key==simplegui.KEY_MAP['left'] and (direction == 'down' or direction == 'up'):
        direction = 'left'
    elif key==simplegui.KEY_MAP['right'] and (direction == 'down' or direction == 'up'):
        direction = 'right'
    elif key==simplegui.KEY_MAP['s'] :
        speed = 0.05
    elif key==simplegui.KEY_MAP['m'] :
        speed = 0.03
    elif key==simplegui.KEY_MAP['h'] :
        speed = 0.01


# check if new food is at empty spot
def check_position(x,y):
    for (a,b) in zip(queue_x, queue_y):
        if a == x and b == y:
            return False
    return True

# check for self biting
def self_biting(x,y):
    for (a,b) in zip(queue_x[1:], queue_y[1:]):
        if a == x and b == y:
            return False
    return True

# new food
def new_food():
    global queue_x, queue_y, height, width, pixel_size, food_x, food_y
    x = random.randint(0+pixel_size,width-pixel_size)
    x = int(x/pixel_size) * pixel_size
    y = random.randint(0+pixel_size,height-pixel_size)
    y = int(y/pixel_size) * pixel_size
    food_at_empty_spot = check_position(x,y)
    if food_at_empty_spot == False:
        new_food()
    else :
        food_x = int(x)
        food_y = int(y)

def new_game():
    global queue_x, queue_y, direction, height, width, pixel_size, food_x, food_y, score
    queue_x = [400, 395, 390, 385, 380, 375, 370, 365, 360, 355, 350]
    queue_y = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250]
    food_x = 100
    food_y = 100
    score = 0
    direction = 'right'

def draw(canvas):
    global queue_x, queue_y, direction, height, width, pixel_size, food_x, food_y, speed, score
    
    # move ahead
    if direction == 'right':    
        queue_x.insert(0, queue_x[0] + pixel_size)
        queue_y.insert(0, queue_y[0])
        if queue_x[0] == food_x and queue_y[0] == food_y:
            new_food()
            score+=1
        else:
            queue_x.pop(len(queue_x)-1)
            queue_y.pop(len(queue_y)-1)
    elif direction == 'left':
        queue_x.insert(0, queue_x[0] - pixel_size)
        queue_y.insert(0, queue_y[0])
        if queue_x[0] == food_x and queue_y[0] == food_y:
            new_food()
            score+=1
        else:
            queue_x.pop(len(queue_x)-1)
            queue_y.pop(len(queue_y)-1)
    elif direction == 'up':
        queue_x.insert(0, queue_x[0])
        queue_y.insert(0, queue_y[0] + pixel_size)
        if queue_x[0] == food_x and queue_y[0] == food_y:
            new_food()
            score+=1
        else:
            queue_x.pop(len(queue_x)-1)
            queue_y.pop(len(queue_y)-1)
    elif direction == 'down':
        queue_x.insert(0, queue_x[0])
        queue_y.insert(0, queue_y[0] - pixel_size)
        if queue_x[0] == food_x and queue_y[0] == food_y:
            new_food()
            score+=1
        else:
            queue_x.pop(len(queue_x)-1)
            queue_y.pop(len(queue_y)-1)


    # check if game over
    if queue_x[0] > width - pixel_size and direction == 'right':
        time.sleep(2)
        print (len(queue_x))
        new_game()
    elif queue_x[0] < pixel_size and direction == 'left':
        time.sleep(2)
        print (len(queue_x))
        new_game()
    elif queue_y[0] > height - pixel_size and direction == 'up':
        time.sleep(2)
        print (len(queue_x))
        new_game()
    elif queue_y[0] < pixel_size and direction == 'down':
        time.sleep(2)
        print (len(queue_x))
        new_game()
    elif self_biting(queue_x[0], queue_y[0]) == False:
        time.sleep(2)
        print (len(queue_x))
        new_game()

    time.sleep(speed)

    # draw snake and food
    canvas.draw_text("Score: " + str(score),[width/4,height/2],100,'grey')
    canvas.draw_polygon([[food_x - pixel_size/2, food_y - pixel_size/2],[food_x + pixel_size/2, food_y - pixel_size/2],[food_x + pixel_size/2 , food_y + pixel_size/2],[food_x - pixel_size/2 ,food_y + pixel_size/2]],1,"CYAN","CYAN")
    for (a,b) in zip(queue_x, queue_y):
        canvas.draw_polygon([[a - pixel_size/2, b - pixel_size/2],[a + pixel_size/2, b - pixel_size/2],[a + pixel_size/2 , b + pixel_size/2],[a - pixel_size/2 ,b + pixel_size/2]],1,"MAGENTA","MAGENTA")


# create frame
frame = simplegui.create_frame("Snake Game", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()
new_game()
