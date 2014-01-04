# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pas = [0,0]
ball_vel = [0,0]
paddle1_pos = 200
paddle2_pos = 200
paddle1_vel = 0
paddle2_vel = 0
left_score = 0
right_score = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == LEFT:
        ball_vel[0] = - random.randrange(120, 240) / 60
        ball_vel[1] = - random.randrange(60, 180) / 60
    if direction == RIGHT:
        ball_vel[0] = random.randrange(120, 240) / 60
        ball_vel[1] = - random.randrange(60, 180) / 60


# define event handlers
def new_game():
    left_score = 0
    right_score = 0
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global x,y  # position of the ball.
    spawn_ball(LEFT)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel, left_score, right_score
 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
     # collide and reflect off of top of canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    # collide and reflect off of bottom of canvas
    if ball_pos[1] >= (HEIGHT - 1 - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    
     
    # check if ball collides with left gutter
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH :
        if ((paddle1_pos-HALF_PAD_HEIGHT) < ball_pos[1] < (paddle1_pos + HALF_PAD_HEIGHT)) :
            ball_vel[0] = - ball_vel[0] - (ball_vel[0] * 0.1)
            #print "left bounce"
        else:
            left_score += 1
            spawn_ball(RIGHT)
            #increase rightscore
            #print "left gutter"
            
    # check if ball collides with right gutter
    if ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS:
        if ((paddle2_pos-HALF_PAD_HEIGHT) < ball_pos[1] < (paddle2_pos + HALF_PAD_HEIGHT)) :
            ball_vel[0] = - ball_vel[0] - (ball_vel[0] * 0.1)
        else:
            right_score += 1
            spawn_ball(LEFT)
            #increase leftscore
            
            
    # draw ball
    drawball(c)
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if (paddle1_pos - HALF_PAD_HEIGHT) <= 0 :
        paddle1_pos = HALF_PAD_HEIGHT
    if (paddle2_pos - HALF_PAD_HEIGHT) <= 0:
        paddle2_pos = HALF_PAD_HEIGHT
    if (paddle1_pos + HALF_PAD_HEIGHT) >= (HEIGHT -1) :
        paddle1_pos  = (HEIGHT - 1) - HALF_PAD_HEIGHT
    if (paddle2_pos + HALF_PAD_HEIGHT) >= (HEIGHT -1) :
        paddle2_pos = (HEIGHT - 1) - HALF_PAD_HEIGHT
    
    
    # draw paddles
    drawpaddle(c)
    
    # draw scores
    c.draw_text("Score: " + str(right_score), (20, 20), 20, 'White')
    c.draw_text("Score: " + str(left_score), (300, 20), 20, 'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = paddle1_vel - 3
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle1_vel + 3
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 3
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 3      
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = paddle1_vel + 3
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle1_vel - 3
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= 3
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel += 3 
    
def drawball(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, 'Red', 'White')
    
def drawpaddle(canvas):
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, HALF_PAD_HEIGHT + paddle1_pos], PAD_WIDTH, 'White')
    canvas.draw_line([WIDTH-HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH-HALF_PAD_WIDTH, HALF_PAD_HEIGHT + paddle2_pos], PAD_WIDTH, 'White')
     
def restart():
    global left_score, right_score
    left_score = 0
    right_score = 0
    new_game()


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restartbutton = frame.add_button('Restart', restart)


# start frame
frame.start()
new_game()
