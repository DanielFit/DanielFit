import enum_classes
from abc import ABC, abstractmethod

class AnimalBase(ABC):
    @property
    @abstractmethod
    def species(self) -> enum_classes.Species: ...

    @property
    def Sound(self) -> enum_classes.Sound: ...


class DogAnimal(AnimalBase):
    @property
    def species(self): return enum_classes.Species.Dog

    @property
    def Sound(self): return enum_classes.Sound.bark

    @property
    def Hunt(self): return enum_classes.Hunt.SmallGame


class CatAnimal(AnimalBase):
    @property
    def species(self): return enum_classes.Species.Cat

    @property
    def Sound(self): return enum_classes.Sound.meow
