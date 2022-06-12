import base_classes
import creator_classes


class AnimalFactory:
    def __init__(self, creator: creator_classes.AnimalCreatorBase):
        self.creator = creator

    def createanimal(self) -> base_classes.AnimalBase:
        return self.creator.createanimal()