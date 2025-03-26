#Mettre toutes les valeurs constantes ici
#puis importer avec import settings as sg
import pygame as pg

pg.init()
pg.font.init()

GAME_NAME = "Projet jeu"
#Paramètres de la fenetre
WINDOWS_HEIGHT = 600
WINDOWS_WIDTH = 800
WINDOWS_TITLE = GAME_NAME


#Paramètres des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
FONT = pg.font.Font(None, 50) # police d'ecriture

#Paramètres du menu
MENU_QUIT_TEXTURE = pg.image.load("assets/exit.png")
MENU_PLAY_TEXTURE = pg.image.load("assets/play.png")

MENU_LOGO_TEXTURE = pg.image.load("assets/logo.png")
MENU_LOGO_TEXTURE = pg.transform.scale(MENU_LOGO_TEXTURE, (300, 200)) 
MENU_BACKGROUND = pg.image.load("assets/menu_background.png")
MENU_BACKGROUND = pg.transform.scale(MENU_BACKGROUND, (WINDOWS_WIDTH, WINDOWS_HEIGHT))