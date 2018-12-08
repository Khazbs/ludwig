from ludwig import *

dog = Object()
air = Object()
bark = Relation(dog, air, Interaction("cause vibration of"))
barking = Event([bark])
barks = Fact([barking])
world = World([barks])
