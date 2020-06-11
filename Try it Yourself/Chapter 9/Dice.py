from random import randint

x = randint(1, 6)


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        roll = randint(1, self.sides)
        print(roll)


die_0 = Die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()

die_1 = Die(10)
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()

die_2 = Die(20)
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
