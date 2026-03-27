import random 

number_list=[]

# Random list creation 
for i in range(10):
    selected_number=random.randint(1,100)
    number_list.append(selected_number)

# Printing list for test
print (number_list)


def selection_sort(liste):
    l = len(liste)

    for i in range(l):
        min_index=i
        # Scan for remaining list
        for j in range(i+1,l):
            if liste[j] < liste[min_index]:
                min_index=j
        liste[i],liste[min_index]=liste[min_index],liste[i]

    return liste

selection_sort(number_list)
print (number_list)         # Sorted list

    