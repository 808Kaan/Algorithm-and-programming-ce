import random 

number_list=[]

# Random list creation 
for i in range(10):
    selected_number=random.randint(1,100)
    number_list.append(selected_number)

# Printing list for test
print (number_list)


def bubble_sort(liste):
    swapped=False
    for i in range(len(liste) - 1):
        if liste[i] > liste[i+1]:
            liste[i],liste[i+1]=liste[i+1],liste[i]
            swapped=True
    # Recursive call
    if swapped:
        bubble_sort(liste)
    else:
        return liste


bubble_sort(number_list)
print (number_list)         # Sorted list