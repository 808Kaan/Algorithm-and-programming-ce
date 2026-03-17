import random 
import math

sayi_listesi=[]    

n=int(input("How many numbers would you like to be generated ?"))

for i in range(n):
    sayi=random.randint(1,1000)
    sayi_listesi.append(sayi)

sayi_listesi.sort()
print (sayi_listesi)

target_value=random.choice(sayi_listesi)
print (target_value)


def jump_search(lst, target):
    n = len(lst)
    step = int(math.sqrt(n))   
    prev = 0

    while lst[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

# linear search in current block        
    while lst[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if lst[prev] == target:
        return prev

    return -1


sonuc = jump_search(sayi_listesi, target_value)

if sonuc != -1:
    print("Number finded:", sonuc)
else:
    print("Number cannot be found")
    
