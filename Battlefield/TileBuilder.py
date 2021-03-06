from Wall import Wall
from Grass import Grass
from Mountain import Mountain
from Water import Water
from Sand import Sand


class TileBuilder():

    @staticmethod
    def build(key):
        if key[0] == "G":
            if len(key) > 1:
                return Grass(key[1])
            else:
                return Grass(None)
        if key[0] == "M":
            if len(key) > 1:
                return Mountain(key[1])
            else:
                return Mountain(None)
        if key[0] == "W":
            if len(key) > 1:
                return Wall(key[1])
            else:
                return Wall(None)
        if key[0] == "~":
            if len(key) > 1:
                return Water(key[1])
            else:
                return Water(None)
        if key[0] == "S":
            if len(key) > 1:
                return Sand(key[1])
            else:
                return Sand(None)