import pygame as pg
import entity

#Création du Player
class Player(entity.Entity):
    def __init__(self, hspd, vspd, maxspd, x, y, image, entity_type):
        super().__init__(hspd,vspd, maxspd, x, y, image, entity_type)
        ## Pour ses caractéristiques à définir

        pass
