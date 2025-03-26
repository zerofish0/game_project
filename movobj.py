import pygame as pg

# Création de la superclasse pour tout les objets mobiles
class MovObj:
    def __init__(self, hspd, vspd, maxspd, x, y, image):
        self.hspd = hspd #horizontale speed
        self.vspd = vspd #verticale speed
        self.maxspd = maxspd
        self.image = image
        self.rect = self.image.get_rect(x=x, y=y)

    def moov(self):
        """Déplace l'objet"""
        self.rect.moov_ip(self.hspd, self.vspd)

    def draw(self, screen):
        """Affiche l'objet"""
        screen.image.blit(self.image,self.rect)

    def get_hspd(self):
        return self.hspd

    def get_vspd(self):
        return self.vspd

    def get_maxspd(self):
        return self.maxspd
    
