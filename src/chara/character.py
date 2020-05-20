# src/chara/character.py
import enum

class C_type(enum.Enum):
    PLAYER = 0
    NPC = 1
    OPPONENT = 2
    BOSS = 3

class Character():

    def __init__(self,name,c_type):
        types = Character.__ty()
        self.name = name
        self.c_type = types[c_type]

    # temporary function
    def identity(self):
        print(str(self.name) + " : " + str(self.c_type))

    # private functions
    def __ty():
        types = {}
        types[C_type.PLAYER] = "player"
        types[C_type.NPC] = "npc"
        types[C_type.OPPONENT] = "opponent"
        types[C_type.BOSS] = "boss"
        return types
