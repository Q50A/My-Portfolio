import simpleguitk as simplegui
import random


r = random.randint(0,255)
g = random.randint(3,233)
b = random.randint(5,210)
def draw_handler(canvas): 
    backg = "RGB( " + str(r) + ", " + str(g) + ", " + str(b)  + ")"
    canvas.draw_text("Home Portfolio Page", (100, 100), 36, "white") 
    frame.set_canvas_background(backg)
frame = simplegui.create_frame("Python", 500, 400) 
frame.set_draw_handler(draw_handler) 
frame.start()