from turtle import *

def hexagon(size):
  angle = 360/6
  for i in range(6):
    forward(size)
    left(angle)
  right(360/3)
  forward(size)
  left(angle)
  forward(size)
  left(angle)  
        
#side_length = int(input('How big? '))

# Setup
side_length = 20
pensize(5)
pencolor('gold')
fillcolor('yellow')
bgcolor('lightsteelblue')

# Move top left
penup()
left(180)
forward(180)
right(90)
forward(130)
pendown()

begin_fill()
for m in range(11):
  hexagon(side_length)
end_fill()

#for a in range(3):
#  begin_fill()
#  for i in range(3):
#    hexagon(side_length)
#    right(360/3)
#  end_fill()
#  angle=360/6
#  size=side_length
#  forward(size)
#  right(angle)
#  forward(size)
#  left(angle)
#  forward(size)
#  left(angle)
#  forward(size)
#  right(angle)
  
