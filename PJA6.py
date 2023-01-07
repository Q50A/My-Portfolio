def PJA6():
  import simplegui
  import random
  
  # Getting a starting point for all the changing variables
  
  lw = 50
  cr = 1
  bb = 50
  bb1 = 550
  gg = 1
  f1 = 1000
  mouse = 1000
  bee = 0
  
  r1 = random.randint(-20,20)
  r2 = random.randint(-20,20)
  r3 = random.randint(-20,20)
  r4 = random.randint(-20,20)
  r5 = random.randint(-20,20)
  
  def draw_handler(canvas):
  
     #global variable declarations
     global lw
     global cr
     global bb
     global bb1
     global gg
     global f1
     global bee
  
     #Animation
  
     #snowman
     canvas.draw_circle((100,bb1),bb,1,"red","white")
     canvas.draw_circle((100,bb1-bb*1.5),bb/1.5,1,"blue","white")
     canvas.draw_circle((100,bb1-bb*2.5),bb/2,1,"black","green")
  
     #grass
     for i in range(1,600,4):
         canvas.draw_line((i,950),(i, 950-gg),2,"blue")
  
     #snow
     canvas.draw_line((0,600),(600,600),lw,"yellow")
  
     #sun
     canvas.draw_circle((600,0),cr, 4,"orange", "yellow")
  
     #flowers
     for j in range(15,600,57):
         canvas.draw_line((j+25,f1),(j,f1+25),10,"red")
         canvas.draw_line((j,f1),(j+25,f1+25),10, "red")
         canvas.draw_line((j-5,f1+12),(j-30,f1-12),10, "blue")
         canvas.draw_line((j+12,f1),(j+12,605),6,"pink")
         canvas.draw_line((j+12,f1-5),(j-12,f1-30),10,"purple")
  
     #bees
     canvas.draw_polygon([(bee,520+r1),(bee-5,523+r1),(bee-8,528+r1),(bee-10,524+r1),(bee-13,523+r1),(bee-13,521+r1),(bee-15,520+r1),(bee-13,517+r1),(bee-10,516+r1),(bee-8,512+r1),(bee-5,517+r1)], 1, "black", "orange")
     canvas.draw_polygon([(bee-100,520+r2),(bee-105,523+r2),(bee-108,528+r2),(bee-110,524+r2),(bee-113,523+r2),(bee-113,521+r2),(bee-115,520+r2),(bee-113,519+r2),(bee-113,517+r2),(bee-110,514+r2),(bee-108,512+r2),(bee-105,517+r2)], 1, "black", "orange")
     canvas.draw_polygon([(bee-200,520+r3),(bee-205,523+r3),(bee-208,528+r3),(bee-210,524+r3),(bee-213,523+r3),(bee-213,521+r3),(bee-215,520+r3),(bee-213,519+r3),(bee-213,517+r3),(bee-210,516+r3),(bee-208,512+r3),(bee-205,517+r3)], 1, "black", "orange")
     canvas.draw_polygon([(bee-300,520+r4),(bee-305,523+r4),(bee-308,528+r4),(bee-310,524+r4),(bee-313,523+r4),(bee-313,521+r4),(bee-313,519+r4),(bee-313,517+r4),(bee-310,516+r4),(bee-308,512+r4),(bee-305,517+r4)], 1, "black", "orange")
     canvas.draw_polygon([(bee-400,520-r5),(bee-405,523-r5),(bee-408,528-r5),(bee-410,524-r5),(bee-413,523-r5),(bee-413,521-r5),(bee-415,520-r5),(bee-413,519-r5),(bee-413,517-r5),(bee-410,516-r5),(bee-408,512-r5),(bee-405,517-r5)], 1, "black", "orange")
  
     #Declarations to change variables and cause growth/shrinking
     lw -= 1
     cr += 1
     bb -+ 2
     bb1 += 0.5
     gg += 1
     f1 -= 1
  
     #Checks for reaching the end
  
     if (lw <=1):
         lw= 1
  
     if (cr >=150):
         cr = 150
  
     if (bb <= 1):
         bb = 1
         canvas.draw_circle((100,600),20, 1, "aqua","aqua")
  
     if (bb1 >= 900):
         bb1 = 900
  
     if (gg >=375):
         gg = 375
  
     if (f1 <= 520):
         f1 = 520
         bee += 0.3
  
     if (bee >= 600):
         bee = 0
  
  frame = simplegui.create_frame('Bring on the Sun', 600, 600)
  frame.set_canvas_background("black")
  frame.set_draw_handler(draw_handler)
  frame.start()