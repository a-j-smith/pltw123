#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
apple.penup()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def apple_fall():
  global apple
  if  apple.ycor()>=-150:
    apple.goto(apple.xcor(),apple.ycor()-10)
#-----function calls-----
draw_apple(apple)
wn.onkeypress(apple_fall,"a")
wn.listen()
wn.bgpic("background.gif")
wn.mainloop()