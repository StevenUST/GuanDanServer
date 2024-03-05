import numpy as np

from enum import IntEnum

from Message import Message

class PlayerType(IntEnum):
    RULE_BASE = 0
    GUANDAN_AI = 1
    OTHER = 2

class Player(object):
    
    def __init__(self, player_id : int, player_type : PlayerType):
        self.player_id = player_id
        self.player_type = player_type
        
    def receive_message(self, message : Message):
        pass