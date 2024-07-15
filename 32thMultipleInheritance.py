class Prey:

    def flee(self):
        print("This animal flees")


class Predator:

    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator): #THIS CLASS IS DERIVED FROM MORE THAN ONE PARENT CLASS BECAUSE FISH HUNTS SMALL FISH AND FLEES TO A BIGGER FISH
    pass

rabbit = Rabbit()

hawk = Hawk()

fish = Fish()

#rabbit.flee()
#hawk.hunt()

fish.flee()
fish.hunt()