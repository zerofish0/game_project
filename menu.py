###[Menu du jeu]###
#Importations : 
import pygame as pg
import settings as sg
class Menu : 
	def __init__(self,screen) : 
		self.screen = screen
		self.button_play = pg.Rect(250, 250, 200, 70)
		self.button_quit = pg.Rect(238, 390, 200, 70)
		self.logo_rect = sg.MENU_LOGO_TEXTURE.get_rect(center=(sg.WINDOWS_WIDTH // 2, 120))

	def drawMenu(self):
		"""Affiche le menu avec les boutons"""
		self.screen.blit(sg.MENU_BACKGROUND,(0,0)) # affiche l'arriere plan
		self.screen.blit(sg.MENU_LOGO_TEXTURE,self.logo_rect.topleft)

		self.screen.blit(sg.MENU_PLAY_TEXTURE, self.button_play.topleft) # affiche le bouton jouer
		self.screen.blit(sg.MENU_QUIT_TEXTURE, self.button_quit.topleft) # affiche le bouton quitter

		pg.display.flip()

	def runMenu(self) : 
		running = "NOP"
		while running== "NOP" : 
			self.drawMenu()
			for event in pg.event.get() : 
				if event.type == pg.QUIT : 
					running = "exit"

				elif event.type == pg.MOUSEBUTTONDOWN : 
					x,y = event.pos
					if self.button_play.collidepoint(x,y) : 
						running = "play"
					elif self.button_quit.collidepoint(x,y) : 
						running = "exit"
		return running



