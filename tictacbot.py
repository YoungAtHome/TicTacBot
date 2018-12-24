from __future__ import print_function
from gpiozero import Robot, Motor
from signal import pause

from bluedot import BlueDot

robot = Robot(left=(26, 20), right=(19, 16))

bd = BlueDot()

def move(pos):
  if pos.y > 0:
    #forward
    if pos.x < 0:
      robot.forward(speed=pos.y, curve_left=-pos.x)
    else:
      robot.forward(speed=pos.y, curve_right=pos.x)
  else:
    #backward
    if pos.x < 0:
      robot.backward(speed=-pos.y, curve_left=-pos.x)
    else:
      robot.backward(speed=-pos.y, curve_right=pos.x)
  
  #if pos.top:
  #  robot.forward(pos.distance)
  #elif pos.bottom:
  #  robot.backward(pos.distance)
  #elif pos.left:
  #  robot.left(pos.distance)
  #elif pos.right:
  #  robot.right(pos.distance)

def stop():
  robot.stop()


def main():
  bd.when_pressed = move
  bd.when_moved = move
  bd.when_released = stop
  
  pause()

if __name__ == "__main__":
    main()

