import base_classes
from abc import ABC, abstractmethod

class AnimalCreatorBase(ABC):

    @abstractmethod
    def createanimal(self) -> base_classes.AnimalBase: ...


class DogAnimalCreator(AnimalCreatorBase):
    def createanimal(self) -> base_classes.AnimalBase:
        return base_classes.DogAnimal()


class CatAnimalCreator(AnimalCreatorBase):
    def createanimal(self) -> base_classes.AnimalBase:
        return base_classes.CatAnimal()