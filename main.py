import pygame as pg
import settings as sg
from menu import Menu

pg.init()

# Configuration de la fenêtre
screen = pg.display.set_mode((sg.WINDOWS_WIDTH, sg.WINDOWS_HEIGHT))
pg.display.set_caption(sg.WINDOWS_TITLE)

menu = Menu(screen)

state = str()
while state != "exit" : 
	state = menu.runMenu()
	print(state)
