import factory
import creator_classes

factory = factory.AnimalFactory(creator_classes.DogAnimalCreator())

i = 0

while i < 1:
    animal = factory.createanimal()
    print('Animal', i, animal.species, animal.Sound, animal.Hunt)
    i = i+1
