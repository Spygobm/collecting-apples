import pgzrun
import random

HEIGHT = 600
WIDTH = 800

center_x = WIDTH // 2
center_y = HEIGHT // 2

final_level = 7
current_level = 1
start_speed = 10

game_over = False
game_complete = False

item_options= ["bag","car","headphones","phone","table"]

items = []

animations = []



def draw():
    screen.blit("background",(0,0))



pgzrun.go()

