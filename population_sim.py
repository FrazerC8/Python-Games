import random
species_types=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

class character():
    def __init__(self,species,power,pos_x,pos_y):
        self.name=species
        self.power=power
        self.pos_x=pos_x
        self.pos_y=pos_y
    def details(self):
        return self.name, self.power, self.pos_x, self.pos_y

def clear():
    for i in range(15):
        print()

grid = [[' ' for i in range(20)] for p in range(10)]
population=[character(species_types[random.randint(0,25)],random.randint(0,100),random.randint(0,20),random.randint(0,10)) for i in range(10)]

for i in range (len(population)):
    print(population[i].details())

#wip fix this
while True:
    clear()
    print ("▓"*(len(grid[0])+2))
    for iy in range (0,len(grid)):
        line=""
        for ix in range (0,len(grid[iy])):
            line+=grid[iy][ix]
        print("▓"+line+"▓")
    print ("▓"*(len(grid[0])+2))

    input("nex step:")




