from enum import Enum

class Species(Enum):
    Dog = 0
    Cat = 1


class Sound(Enum):
    bark = 0,
    meow = 1


class Hunt(Enum):
    SmallGame = 0,
    BigGame = 1