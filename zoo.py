def placeanimal(zoo, name)->list:
    animal = {}
    found = False
    for a in(zoo):
        if name in a.keys(): 
            a[name] += 1
            found = True
        
    if not found:
            animal[name] =1
            zoo.append(animal)
    return zoo


zoo = [{"kecske": 1}, {"béka": 1}]
animal = {}
print("This is a Zoo. New animal (1)-Delete one(2)-Exit(0)")
select = None
while select != 0:
    select = int(input("What do you want to do? "))
    if select != 0:
        if select == 1:
            name = input("Name of the animal: ")
            placeanimal(zoo, name)
            
                #else: 
                #    animal[name] = 1
                #    zoo.append(animal)
                #    animal = {}

print(zoo)         
print("Vége a játéknak.")   