# implementation of card game - Memory

import simplegui
import random

numberlist = []
exposedList = []
cardclicked = []
state = 0
prevcardindex1 = None
prevcardindex2 = None
turns = 0


# helper function to initialize globals
def new_game():
    global numberlist, exposedList, cardclicked, prevcardindex1, prevcardindex2, turns, state
    turns = 0
    exposedList = []
    numberList = []
    cardclicked = []
    prevcardindex1 = None
    prevcardindex2 = None
    state = 0
    label.set_text("Turns = "+ str(turns))
    #create list in the range [0,8)
    list1 = range(0,8)
    list2 = range(0,8)
    numberlist = list1 + list2
    for number in numberlist:
        exposedList.append(False)
    storeCardCoordinates()
    random.shuffle(numberlist)
    return

                             
# cards are logically 50x100 pixels in size    
def draw(canvas):
    drawCards(canvas)
    return

def drawCards(canvas):
    y1 = 0
    y2 = 100
    x1 = 0
    index = 0
    for number in numberlist:
        x2 = x1 + 50
        if exposedList[index] == True:
            canvas.draw_polygon([[x1, y1], [x2, y1], [x2, y2], [x1, y2]], 1,'Black', 'White')
            canvas.draw_text(str(number), ( (x1 + x2)/2, (y1 + y2)/2), 20, 'Blue')
        else:
            canvas.draw_polygon([[x1, y1], [x2, y1], [x2, y2], [x1, y2]], 1,'Black', 'Green')
        x1 = x1 + 50
        index += 1
    return
        
def storeCardCoordinates():
    x1 = 0
    x2 = 0
    for number in numberlist:
        x2 = x1 + 50
        cardclicked.append((x1,x2))
        x1 += 50
    return
    
    
def mouseclick(pos):
    global state,prevcardindex1, prevcardindex2, turns
    
    index = 0
    for lists in cardclicked:
        if lists[0] <= pos[0] and lists[1] >= pos[0]:
            if exposedList[index] == False:
                exposedList[index] = True
            elif exposedList[index] == True:
                return
            if state == 0:
                state = 1
                prevcardindex1 = index
            elif state == 1:
                state = 2
                prevcardindex2 = prevcardindex1
                prevcardindex1 = index
            else:
                state = 1
                if numberlist[prevcardindex1] != numberlist[prevcardindex2]:
                    exposedList[prevcardindex1] = False
                    exposedList[prevcardindex2] = False
                   
                    
                else:
                    exposedList[prevcardindex1] = True
                    exposedList[prevcardindex2] = True
                    
                prevcardindex1 = index
                turns = turns + 1
                label.set_text("Turns = "+ str(turns))
                
        index = index + 1
    
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = "+ str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric