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

#creates grid
grid = [[" " for i in range(20)] for p in range(10)]
#fills population
population=[character(species_types[random.randint(0,25)],random.randint(0,100),random.randint(0,19),random.randint(0,9)) for i in range(10)]
#adds population to grid
for i in population:
    while True:
        if grid[i.pos_y][i.pos_x]==" ":
            grid[i.pos_y][i.pos_x]=i
            break
        else:
            i.pos_x,i.pos_y=random.randint(0,19),random.randint(0,9)
        

for i in range (len(population)):
    print(population[i].details())


#display grid
while True:
    for i in population:
        grid[i.pos_y][i.pos_x]=" "
        while True:
            move=random.randint(0,3)
            if move==0 and i.pos_x>0:
                if grid[i.pos_y][i.pos_x-1]==" ":
                    i.pos_x-=1
                    break
            elif move==1 and i.pos_x<19:
                if grid[i.pos_y][i.pos_x+1]==" ":
                    i.pos_x+=1
                    break
            elif move==2 and i.pos_y>0:
                if grid[i.pos_y-1][i.pos_x]==" ":
                    i.pos_y-=1
                    break
            elif move==3 and i.pos_y<9:
                if grid[i.pos_y+1][i.pos_x]==" ":
                    i.pos_y+=1
                    break
        grid[i.pos_y][i.pos_x]=i

    clear()
    print ("▓"*(len(grid[0])+2))

    for iy in range (0,len(grid)):
        line=""
        for ix in range (0,len(grid[iy])):
            if grid[iy][ix]==" ":
                line+=" "
            else:
                line+=grid[iy][ix].name
        print("▓"+line+"▓")

    print ("▓"*(len(grid[0])+2))

    input("next step:")




