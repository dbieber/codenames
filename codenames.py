import random

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

TRANSPARENT = (0, 0, 0, 0)
WHITE = (255, 255, 255)
LIGHT = (205, 205, 205)
BLACK = (0, 0, 0)
RED = (222, 0, 0)
GREEN = (0, 222, 0)
BLUE = (0, 0, 222)
SNOW = (255, 250, 250)
YELLOW = (222, 222, 0)
DARK = (30, 30, 30)


x = range(25)
random.shuffle(x)
first_player = random.randint(0, 1)

num_blue = 8 + first_player
num_red = 9 - first_player
blue = x[:num_blue]
red = x[num_blue:num_blue + num_red]
assassin = x[num_blue+num_red]
neutral = x[num_blue+num_red+1:]


def new_image_draw(size):
  image = Image.new(
    'RGBA',
    size=tuple(s + 1 for s in size),
    color=(0, 0, 0, 0))
  draw = ImageDraw.Draw(image)
  return image, draw


w = 60

def square(draw, r, c, color):
  draw.rectangle((r * w, c * w, (r + 1) * w, (c + 1) * w), fill=color, outline=DARK)

def generate():
  image, draw = new_image_draw((5*w, 5*w))
  for row in range(5):
    for col in range(5):
      index = 5 * row + col
      if index == assassin:
        square(draw, row, col, BLACK)
      elif index in red:
        square(draw, row, col, RED)
      elif index in blue:
        square(draw, row, col, BLUE)
      elif index in neutral:
        square(draw, row, col, SNOW)

  image.save('codenames.png')

if __name__ == '__main__':
  generate()