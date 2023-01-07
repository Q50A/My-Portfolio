import play
w=300
h=300
@play.when_program_starts
def do():
  play.screen.width =w
  play.screen.height =h

box = play.new_box(
  color=(255,233,200),
  x=150,
  y=150,
  width= w,
  height= h,
)

play.set_backdrop((110,0,0))


v_head = play.new_circle(
  color = "blue",
  x = 50,
  y = 40,
  radius = 50,
)
eye_V_dye=play.new_circle(
  color = "yellow",
  x=30,
  y=50,
  radius=5,
)
eye_V_dye=play.new_circle(
  color = "yellow",
  x=70,
  y=50,
  radius=5,
)
nose_V_dye=play.new_circle(
  color = "yellow",
  x=50,
  y=40,
  radius=5,
)
mouth_V_dye=play.new_box(
  color = "orange",
  x= 50,
  y=15,
  width = 30,
  height = 35,
)
text= play.new_text(
  color="blue",
  words="Why is dog food so bad,",
  x=227,
  y=287,
  font_size=20,
)
@play.repeat_forever
async def speak_slowly():
  await play.timer(seconds=3)
  text.words= "No its not my dog likes the food"

mouse_text = play.new_text(
  color="blue",
  words="blank",
  x=0,
    y=0,
    font_size=20,
  )
@play.repeat_forever
def mouse_coords():
  mouse_text.go_to(play.mouse)
  mouse_text.words =str(int(play.mouse.x))+ "," + str(int(play.mouse.y))
play.start_program()