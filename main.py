#   a123_apple_1.py
import turtle as trtl
import random
import string
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
score = 0
score_writer =  trtl.Turtle()
score_writer.penup()
score_writer.goto(150,100)
letter = random.choice(string.ascii_lowercase)
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
apple.penup()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple,letter):
  apple.clear()
  wn.tracer(False)
  apple.goto(apple.pos()-(18,50))
  apple.write(letter, font=("Arial", 55, "bold"))
  apple.goto(apple.pos()+(18,50))
  wn.update()
  active_apple.shape(apple_image)

def update_score():
  global score
  score_writer.clear()
  score+=1
  score_writer.write(score,font=("Arial", 55, "bold"))

def apple_fall():
  global apple
  global letter
  wn.onkeypress(None,letter)
  letter = random.choice(string.ascii_lowercase)
  if  apple.ycor()>=-115:
    apple.goto(apple.xcor(),apple.ycor()-25)
  else:
    apple.goto(random.randint(-200,200),random.randint(0,50))
    update_score()
  draw_apple(apple, letter)
  wn.update()
  wn.onkeypress(apple_fall,letter)
  wn.listen 
#-----function calls-----
draw_apple(apple,letter)
wn.onkeypress(apple_fall,letter)
wn.listen()
wn.bgpic("background.gif")
wn.mainloop()