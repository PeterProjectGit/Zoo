zoo = list()

animal = {}
print("This is a Zoo. New animal (1)-Delete one(2)-Exit(0)")
select = None
while select != 0:
    select = int(input("What do you want to do? "))
    
    if select != 0:
        
        if select == 1:
            
            name = input("Name of the animal: ")
            if name not in animal.keys():
                animal[name] = 1
                zoo.append(animal)
            else: 
                for a in zoo:
                    a[name] += 1
            animal = dict()

for a in zoo:
    print(a)
 
print("Vége a játéknak.")   