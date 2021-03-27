from survive.controllers.controller import Controller

from survive.models.entity.enemies import Enemy
from survive.models.entity.enemies.hog import Hog


class EnemyController(Controller):
    def __init__(self, player):
        super().__init__(player)
        self._enemy = Enemy()

    def generate_enemy(self):
        return Hog()
