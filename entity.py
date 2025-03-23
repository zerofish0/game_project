
import pygame as pg
import movobj

#Création de la superclasse pour toutes les entités du jeu
class Entity(movobj.MovObj):
    def __init__(self, hspd, vspd, maxspd, x, y, image, entity_type):
        super().__init__(hspd, vspd, maxspd, x, y, image)
        self.entity_type = entity_type

    def get_entity_type(self):
        return self.entity_type

