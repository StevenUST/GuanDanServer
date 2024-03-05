import numpy as np

from typing import List
from enum import IntEnum

from Card import Card

class MessageType(IntEnum):
    NOTIFY = 0
    PLAYCARD = 1
    TRIBUTE = 2

class Message(object):
    
    def __init__(self, message_type : MessageType, src_player_id : int, dsct_player_id : int, cards : List[Card]):
        self.message_type = message_type